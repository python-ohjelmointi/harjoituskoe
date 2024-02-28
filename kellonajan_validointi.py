"""
Ajan validointi

Tehtäväsi on toteuttaa funktio `validoi_aika`, joka tarkistaa, onko sille
annettu aika kelvollinen.

Ajat annetaan merkkijonoina ja niiden tulee olla muodossa "h:mm", missä h on
tunnit ja mm on minuutit. Ajan tulee olla kelvollinen 24 tunnin muodossa.

Mikäli annettu aika on kelvollinen, funktion tulee palauttaa True. Muussa
tapauksessa sen tulee palauttaa False. Funktio ei saa aiheuttaa poikkeusta,
vaikka annettu merkkijono olisi epäkelpo.

Esimerkit:

Seuraavat ajankohdat ovat kelvollisia, joten funktion tulee palauttaa True:

    >>> validoi_aika("0:10")
    True

    >>> validoi_aika("23:59")
    True


Seuraaville kellonajoille palautetaan False, koska ne ovat epäkelpoja:

    >>> validoi_aika("30:30")
    False

    >>> validoi_aika("12:61")
    False


Funktio ei saa aiheuttaa virhettä, vaikka annettu muoto olisi virheellinen
tai puutteellinen:

>>> validoi_aika("0:1")
False

>>> validoi_aika("10")
False

>>> validoi_aika(":")
False

>>> validoi_aika("10:01:")
False


Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
-lohkon sisään. Voit halutessasi suorittaa yllä esitetyt doctest-
testit komennolla:

python3 -m doctest --verbose kellonajan_validointi.py
"""



def validoi_aika(aika: str) -> bool:
    """
    Toteuta logiikka, joka tarkastaa onko merkkijonona annettu aika
    kelvollinen. Palauta funktiosta joko True tai False.
    """


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """
