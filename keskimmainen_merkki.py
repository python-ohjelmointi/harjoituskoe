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
"""


def keskimmainen_merkki(merkkijono: str) -> str:
    """
    Toteuta logiikka, joka palauttaa annetusta merkkijonosta keskimmäisen
    merkin. Jos merkkejä on parillinen määrä, voit palauttaa kumman tahansa
    keskimmäisistä merkeistä.
    """


if __name__ == "__main__":
    """
    Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
    -lohkon sisään. Voit myös halutessasi poistaa tämän if-lohkon.

    Lisäksi suosittelemme hyödyntämään myös tehtävänantoon sisältyviä doctest-
    testejä. Alla olevat rivit suorittavat testit, kun tämä tiedosto ajetaan:
    """
    import doctest
    doctest.testmod(verbose=True)
