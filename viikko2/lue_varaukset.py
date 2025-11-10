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

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    #tietojen jako
    varausId = varaus.split('|')

    #päivämäärän tuonti
    from datetime import datetime

    #tietotyyppien määritys
    varausId = int(varausId[0])
    varausId = str(varausId[1])
    #muunnetaan päivämäärät ja kellonajat
    varausId[2] = datetime.strptime(varausId[2], "%d.%m.%Y").date()
    varausId[3] = datetime.strptime(varausId[3], "%H.%M").time()
    varausId[4] = int(varausId[4])      
    varausId[5] = float(varausId[5])
    #lasketaan kokonaishinta
    varausId[6] = varausId[4] * varausId[5]
    #lisätään listaan
    varausId.insert(6, varausId[6])
    #IF/ELSE lauseke 
    varausId[7] = "Kyllä" if varausId[7] == "1" else "Ei"
    varausId[8] = str(varausId[8])
    varausId[9] = str(varausId[9])  
    varausId[10] = str(varausId[10])

    #tendään kopio ID listoista ja lisätään euron merkit tulosteeseen
    tuloste - varausId.copy()

    tuloste[5] = f"{tuloste[5]} €"
    tuloste[6] = f"{tuloste[6]} €"

    #otsikot
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

    # Tulostetaan varaus konsoliin



    """
    # Kokeile näitä
    #print(varaus.split('|'))
    #varausId = varaus.split('|')[0]
    #print(varausId)
    #print(type(varausId))
    """
    Edellisen olisi pitänyt tulostaa numeron 123, joka
    on oletuksena tekstiä.

    Voit kokeilla myös vaihtaa kohdan [0] esim. seuraavaksi [1]
    ja testata mikä muuttuu
    """

if __name__ == "__main__":
    main()