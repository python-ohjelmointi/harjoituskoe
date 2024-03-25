"""
Keskimmäinen merkki

Tehtäväsi on toteuttaa funktio keskimmainen_merkki, joka palauttaa annetusta
merkkijonosta keskimmäisen merkin. Jos merkkejä on parillinen määrä, funktio
voi palauttaa kumman tahansa keskimmäisistä merkeistä. Voit olettaa, että
annettu merkkijono ei ole koskaan tyhjä.

Esimerkki:

    >>> keskimmainen_merkki("vs code")
    'c'

    >>> keskimmainen_merkki("koe")
    'o'

Ohjelman tulee toimi myös muilla kuin kirjainmerkeillä:

    >>> keskimmainen_merkki("C++")
    '+'

Jos merkkejä on parillinen määrä, voit palauttaa kumman tahansa keskimmäisistä:

    >>> keskimmainen_merkki("Abba")
    'b'


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
-lohkon sisään. Voit halutessasi suorittaa yllä esitetyt doctest-
testit komennolla:

python3 -m doctest --verbose keskimmainen_merkki.py
"""


def keskimmainen_merkki(merkkijono: str) -> str:
    """
    Toteuta logiikka, joka palauttaa annetusta merkkijonosta keskimmäisen
    merkin. Jos merkkejä on parillinen määrä, voit palauttaa kumman tahansa
    keskimmäisistä merkeistä.
    """


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
