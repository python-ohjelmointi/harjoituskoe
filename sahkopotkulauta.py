"""
Sähköpotkulaudan vuokraus

Kirjoita funktio sahkopotkulaudan_vuokra, joka laskee ja palauttaa sähköpotkulaudan
vuokrauksen hinnan aloitus- ja lopetusaikojen perusteella.

Kellonajat annetaan merkkijonoina muodossa "h:mm" ja ne ovat aina kelvollisia kellonaikoja.

Hinta koostuu 1 € aloitusmaksusta ja 0,25 € minuuttikohtaisesta veloituksesta.

Mikäli vuokrauksen lopetusaika on aikaisemmin kuin alkuaika, vuokraus on tapahtunut
vuorokausirajan yli. Esimerkiksi aikavälillä 23:30 - 1:15 tapahtunut vuokraus on ylittänyt
vuorokausirajan ja kestänyt 105 minuuttia. Mahdollisia yli 24 tunnin vuokrauksia ei
tarvitse ottaa ohjelmassa huomioon.

Esimerkit:

Tasan tunnin pituinen vuokra maksaa 1 € + 60 * 0,25 €:

    >>> sahkopotkulaudan_vuokra("0:00", "1:00")
    16.0

Vuokraus kestää 90 minuuttia, joten hinta on 1 € + 90 * 0,25:

    >>> sahkopotkulaudan_vuokra("10:00", "11:30")
    23.5

Vuokraus kestää 1 minuutin, joten hinta on 1,25 €:

    >>> sahkopotkulaudan_vuokra("9:59", "10:00") == 1.25
    True

Aloitus ja lopetus menevät vuorokausirajan yli ja vuokraus kestää 1h 45 min:

    >>> sahkopotkulaudan_vuokra("23:30", "1:15")
    27.25


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
-lohkon sisään. Voit halutessasi suorittaa yllä esitetyt doctest-
testit komennolla:

python3 -m doctest --verbose sahkopotkulauta.py
"""



def sahkopotkulaudan_vuokra(aloitusaika: str, lopetusaika: str) -> float:
    """
    Toteuta logiikka, joka hyödyntää merkkijonoina annettuja kellonaikoja
    ja laskee sekä palauttaa vuokrauksen hinnan.
    """


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
