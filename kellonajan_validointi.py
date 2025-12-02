"""
Kellonajan validointi

Tehtäväsi on toteuttaa uusi funktio `validoi_aika`, joka tarkistaa, onko sille
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
"""



# Toteuta tänne uusi funktio, jonka nimi, parametrit ja paluuarvot
# noudattavat tehtävänantoa.


if __name__ == "__main__":
    """
    Jos kirjoitat omia testejä tai kokeiluja, toteuta ne if __name__
    -lohkon sisään. Voit myös halutessasi poistaa tämän if-lohkon.

    Lisäksi suosittelemme hyödyntämään myös tehtävänantoon sisältyviä doctest-
    testejä. Alla olevat rivit suorittavat testit, kun tämä tiedosto ajetaan:
    """
    import doctest
    doctest.testmod(verbose=True)
