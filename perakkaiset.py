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

Luvut saavat olla missä vain järjestyksessä, eli myös tämä tapaus sallitaan:

    >>> tarkista_perakkaiset([1, 3, 2, 5, 4])
    True

Yksikään luku ei kuitenkaan saa puuttua, eikä esiintyä useammin kuin kerran:

    >>> tarkista_perakkaiset([5, 3, 1])
    False

    >>> tarkista_perakkaiset([5, 3, 2, 2, 1])
    False
"""



def tarkista_perakkaiset(numerot: list) -> bool:
    """
    Toteuta logiikka, joka tarkastaa annetun `numerot`-listan ja
    palauttaa tehtävänannon mukaisesti totuusarvon True tai False.
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
