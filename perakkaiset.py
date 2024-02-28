"""
Peräkkäisten numeroiden tarkistus

Tehtäväsi on toteuttaa tarkista_perakkaiset-funktio, joka tarkistaa,
sisältääkö sille annettu järjestämätön kokonaislukujen lista peräkkäisiä
numeroita. Numerot saavat olla missä tahansa järjestyksessä, kunhan ne
muodostavat yhdessä peräkkäisten lukujen sarjan. Yksikään luku ei saa
esiintyä enempää kuin kerran, ja voit olettaa, että annettu lista ei ole
koskaan tyhjä.

Esimerkki:

    >>> tarkista_perakkaiset([1, 2, 3, 4, 5])
    True

    >>> tarkista_perakkaiset([5, 4, 3, 2, 1])
    True

Luvut saavat olla missä vain järjestyksessä:

    >>> tarkista_perakkaiset([1, 3, 2, 5, 4])
    True

Yksikään luku ei saa puuttua, eikä esiintyä useammin kuin kerran:

    >>> tarkista_perakkaiset([5, 3, 1])
    False

    >>> tarkista_perakkaiset([5, 3, 2, 2, 1])
    False

Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
-lohkon sisään. Voit halutessasi suorittaa yllä esitetyt doctest-
testit komennolla:

python3 -m doctest --verbose perakkaiset.py
"""



def tarkista_perakkaiset(nums: list) -> bool:
    """
    Toteuta ratkaisusi tänne.
    """

if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
