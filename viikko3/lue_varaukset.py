"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen fuktioita. 
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,90 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

""" 


def hae_varausnumero(varaus): ...
def hae_varaaja(varaus): ...
def hae_paiva(varaus): ...
def hae_aloitusaika(varaus): ...
def hae_tuntimaara(varaus): ...
def hae_tuntihinta(varaus): ...
def laske_kokonaishinta(varaus): ...
def hae_maksettu(varaus): ...
def hae_kohde(varaus): ...
def hae_puhelin(varaus): ...
def hae_sahkoposti(varaus): ...
def laske_kokonaishinta(varaus): ...

# Varaus tallennetaan sanakirjaan
varaus = {
    "varausnumero": 123,
    "varaaja": "Anna Virtanen",
    "paivamaara": "31.10.2025",
    "aloitusaika": "10.00",
    "tuntimaara": 2,
    "tuntihinta": 19.95,
    "maksettu": True,
    "kohde": "Kokoustila A",
    "puhelin": "0401234567",
    "sahkoposti": "anna.virtanen@example.com"
}

# Funktiot

def hae_varausnumero(varaus):
    return varaus["varausnumero"]
def hae_varaaja(varaus):
    return varaus["varaaja"]

def hae_paiva(varaus):
    return varaus["paivamaara"]

def hae_aloitusaika(varaus):
    return varaus["aloitusaika"]

def hae_tuntimaara(varaus):
    return varaus["tuntimaara"]

def hae_tuntihinta(varaus):
    return varaus["tuntihinta"]

def laske_kokonaishinta(varaus):
    return varaus["tuntimaara"] * varaus["tuntihinta"]

def hae_maksettu(varaus):
    return varaus["maksettu"]

def hae_kohde(varaus):
    return varaus["kohde"]

def hae_puhelin(varaus):
    return varaus["puhelin"]

def hae_sahkoposti(varaus):
    return varaus["sahkoposti"]


# Tulostus täsmälleen annetussa muodossa
print(f"Varausnumero: {hae_varausnumero(varaus)}")
print(f"Varaaja: {hae_varaaja(varaus)}")
print(f"Päivämäärä: {hae_paiva(varaus)}")
print(f"Aloitusaika: {hae_aloitusaika(varaus)}")
print(f"Tuntimäärä: {hae_tuntimaara(varaus)}")
print(f"Tuntihinta: {hae_tuntihinta(varaus)} €")
print(f"Kokonaishinta: {laske_kokonaishinta(varaus):.2f} €")
print(f"Maksettu: {'Kyllä' if hae_maksettu(varaus) else 'Ei'}")
print(f"Kohde: {hae_kohde(varaus)}")
print(f"Puhelin: {hae_puhelin(varaus)}")
print(f"Sähköposti: {hae_sahkoposti(varaus)}")
