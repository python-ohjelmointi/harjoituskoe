"""
Lounaan hinta

Toteuta funktio lounaan_hinta, joka laskee ja palauttaa kuvitteellisen lounasravintolan
annoksen hinnan annetun henkilön iän perusteella. Lounas maksaa normaalisti 12,90 €,
mutta lapset maksavat lounaasta 0,5 € per ikävuosi 12:een ikävuoteen asti.

6-vuotiaan lounas maksaa siis 3 euroa ja 12-vuotiaan lounas 6 euroa.

Esimerkki:

    >>> lounaan_hinta(25)
    12.9

    >>> lounaan_hinta(7)
    3.5

    >>> lounaan_hinta(12)
    6.0

    >>> lounaan_hinta(12) == 6.0  # Tulos pitää palauttaa, ei tulostaa
    True

Voit olettaa annetun iän olevan aina kelvollinen.

Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
-lohkon sisään. Voit halutessasi suorittaa yllä esitetyt doctest-
testit komennolla:

python3 -m doctest --verbose lounaan_hinta.py
"""



def lounaan_hinta(ika: int) -> float:
    """
    Laske lounaan hinta annetun henkilön iän perusteella ja palauta
    tulos liukulukuna.
    """


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
