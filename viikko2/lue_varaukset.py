"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    from datetime import datetime

    try:
        with open(varaukset, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Tiedostoa '{varaukset}' ei löydy. Varmista että tiedosto on samassa kansiossa.")
        return

    otsikot = [
        "Varausnumero:",
        "Varaaja:",
        "Päivämäärä:",
        "Aloitusaika:",
        "Tuntimäärä:",
        "Tuntihinta:",
        "Kokonaishinta:",
        "Maksettu:",
        "Kohde:",
        "Puhelin:",
        "Sähköposti:"
    ]

    for line in lines:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 10:
            print(f"Virheellinen rivi (odotettiin vähintään 10 kenttää): {line}")
            continue

        # Parsitaan kentät
        try:
            varausnumero = int(parts[0])
        except ValueError:
            varausnumero = parts[0]

        varaaja = parts[1]

        # päivämäärän ja ajan parsinta: yritetään useampaa formaattia
        try:
            paiva = datetime.strptime(parts[2], "%Y-%m-%d").date()
        except ValueError:
            try:
                paiva = datetime.strptime(parts[2], "%d.%m.%Y").date()
            except ValueError:
                paiva = parts[2]

        try:
            alku = datetime.strptime(parts[3], "%H:%M").time()
        except ValueError:
            try:
                alku = datetime.strptime(parts[3], "%H.%M").time()
            except ValueError:
                alku = parts[3]

        try:
            tuntimaara = int(parts[4])
        except ValueError:
            tuntimaara = parts[4]

        try:
            tunttihinta = float(parts[5])
        except ValueError:
            tunttihinta = parts[5]

        # maksettu-kenttä: hyväksytään '1', 'true', 'yes' jne.
        maksettu_raw = parts[6].strip().lower()
        maksettu = "Kyllä" if maksettu_raw in ("1", "true", "t", "yes", "y") else "Ei"

        kohde = parts[7]
        puhelin = parts[8]
        sahkoposti = parts[9]

        # lasketaan kokonaishinta jos numerot kunnossa
        try:
            kokonaishinta = float(tuntimaara) * float(tunttihinta)
        except Exception:
            kokonaishinta = "-"

        arvot = [
            varausnumero,
            varaaja,
            paiva,
            alku,
            tuntimaara,
            f"{tunttihinta:.2f} €" if isinstance(tunttihinta, float) else tunttihinta,
            f"{kokonaishinta:.2f} €" if isinstance(kokonaishinta, float) else kokonaishinta,
            maksettu,
            kohde,
            puhelin,
            sahkoposti,
        ]

        # Tulostetaan siistissä muodossa
        for otsikko, arvo in zip(otsikot, arvot):
            print(f"{otsikko} {arvo}")
        print()



    """
    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(varausId))
    """
    #Edellisen olisi pitänyt tulostaa numeron 123, joka on oletuksena tekstiä.

    #Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1] ja testata mikä muuttuu

if __name__ == "__main__": main()