def keskimmainen_merkki(merkkijono: str) -> str:
    """
    Palauttaa annetusta merkkijonosta keskimmäisen merkin. Jos merkkejä on
    parillinen määrä, palautetaan kumman tahansa keskimmäisistä merkeistä.
    """
    pituus = len(merkkijono)
    return merkkijono[pituus // 2]  # Palautetaan keskimmäinen merkki
