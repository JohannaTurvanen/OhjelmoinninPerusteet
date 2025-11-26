"""
Ohjelma joka tulostaa tiedostosta luettujen varausten alkiot ja niiden tietotyypit

varausId | nimi | sähköposti | puhelin | varauksenPvm | varauksenKlo | varauksenKesto | hinta | varausVahvistettu | varattuTila | varausLuotu
------------------------------------------------------------------------
201 | Muumi Muumilaakso | muumi@valkoinenlaakso.org | 0509876543 | 2025-11-12 | 09:00:00 | 2 | 18.50 | True | Metsätila 1 | 2025-08-12 14:33:20
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
202 | Niiskuneiti Muumilaakso | niisku@muumiglam.fi | 0451122334 | 2025-12-01 | 11:30:00 | 1 | 12.00 | False | Kukkahuone | 2025-09-03 09:12:48
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
203 | Pikku Myy Myrsky | myy@pikkuraivo.net | 0415566778 | 2025-10-22 | 15:45:00 | 3 | 27.90 | True | Punainen Huone | 2025-07-29 18:05:11
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
204 | Nipsu Rahapulainen | nipsu@rahahuolet.me | 0442233445 | 2025-09-18 | 13:00:00 | 4 | 39.95 | False | Varastotila N | 2025-08-01 10:59:02
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
205 | Hemuli Kasvikerääjä | hemuli@kasvikeraily.club | 0463344556 | 2025-11-05 | 08:15:00 | 2 | 19.95 | True | Kasvitutkimuslabra | 2025-10-09 16:41:55
int | str | str | str | date | time | int | float | bool | str | datetime
------------------------------------------------------------------------
"""
from datetime import datetime

def muunna_varaustiedot(varaus: list) -> list:
    # Tähän tulee siis varaus oletustietotyypeillä (str)
    # Varauksessa on 11 saraketta -> Lista -> Alkiot 0-10
    # Muuta tietotyypit haluamallasi tavalla -> Seuraavassa esimerkki ensimmäisestä alkioista
    muutettu_varaus = []
    # poistetaan kenttien ympäriltä välilyönnit
    varaus = [v.strip() for v in varaus]

#1) varausId: str -> int
    muutettu_varaus.append(int(varaus[0]))

#2) nimi: str
    muutettu_varaus.append(varaus[1])

#3) sähköposti: str
    muutettu_varaus.append(varaus[2])

#4) puhelin: str
    muutettu_varaus.append(varaus[3])

#5) varauksenPvm: "2025-11-12" -> datetime.date
    muutettu_varaus.append(datetime.strptime(varaus[4], "%Y-%m-%d").date())

#6) varauksenKlo: "09:00" -> datetime.time
    muutettu_varaus.append(datetime.strptime(varaus[5], "%H:%M").time())

#7) varauksenKesto: str -> int
    muutettu_varaus.append(int(varaus[6]))

#8) hinta: "18.50" -> float
    muutettu_varaus.append(float(varaus[7]))

#9) varausVahvistettu: "true"/"false" -> bool
    val = varaus[8].lower()
    muutettu_varaus.append(val in ("true", "kyllä", "yes", "1"))

#10) varattuTila: str
    muutettu_varaus.append(varaus[9])

#11) varausLuotu: "2025-08-12 14:33:20" -> datetime.datetime
    muutettu_varaus.append(datetime.strptime(varaus[10], "%Y-%m-%d %H:%M:%S"))
    return muutettu_varaus
 

def hae_varaukset(varaustiedosto: str) -> list:
    # HUOM! Tälle funktioille ei tarvitse tehdä mitään!
    # Jos muutat, kommentoi miksi muutit
    varaukset = []
    varaukset.append(["varausId", "nimi", "sähköposti", "puhelin", "varauksenPvm", "varauksenKlo", "varauksenKesto", "hinta", "varausVahvistettu", "varattuTila", "varausLuotu"])
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def main():
    # HUOM! seuraaville riveille ei tarvitse tehdä mitään osassa A!
    # Osa B vaatii muutoksia -> Esim. tulostuksien (print-funktio) muuttamisen.
    # Kutsutaan funkioita hae_varaukset, joka palauttaa kaikki varaukset oikeilla tietotyypeillä
    varaukset = hae_varaukset("varaukset.txt")
    print(" | ".join(varaukset[0]))
    print("------------------------------------------------------------------------")

    # 1) vahvistetut varaukset
    print("1) Vahvistetut varaukset:")
    vahvistetut_varaukset = [v for v in varaukset[1:] if v[8] is True]
    for v in vahvistetut_varaukset:
        print(f"- {v[1]}, {v[9]}, {v[4].strftime('%d.%m.%Y')} klo {v[5].strftime('%H.%M')}")
    print("------------------------------------------------------------------------")

        # 2) ei-vahvistetut varaukset
    print("2) Ei vahvistetut varaukset:")
    ei_vahvistetut_varaukset = [v for v in varaukset[1:] if v[8] is False]
    for v in ei_vahvistetut_varaukset:
        print(f"- {v[1]}, {v[9]}, {v[4].strftime('%d.%m.%Y')} klo {v[5].strftime('%H.%M')}")
    print("------------------------------------------------------------------------")

    # 3) pitkat varaukset (yli 3h)
    print("3) pitkat varaukset (yli 3h):")      
    pitkat = [v for v in varaukset[1:] if v[6] >= 3]
    if pitkat:
        for v in pitkat:
            print(f"- {v[1]}, {v[9]}, {v[4].strftime('%d.%m.%Y')} klo {v[5].strftime('%H.%M')} ({v[6]}h)")
    print("------------------------------------------------------------------------")

        # 4) varausten vahvistusstatus
    print("4) Varausten vahvistusstatus:")
    for v in varaukset[1:]:
        status = "Vahvistettu" if v[8] else "Ei vahvistettu"
        print(f"- {v[1]}: {status}")
    print("------------------------------------------------------------------------")

    # 5) Yhteenveto varauksista
    print("5) Yhteenveto varauksista:")
    vahvistetut_count = len(vahvistetut_varaukset)
    ei_vahvistetut_count = len(ei_vahvistetut_varaukset)
    print(f"- Vahvistettuja varauksia: {vahvistetut_count} kpl, Ei vahvistettuja varauksia: {ei_vahvistetut_count} kpl")
    print("------------------------------------------------------------------------")

        #




if __name__ == "__main__":
    main()  
