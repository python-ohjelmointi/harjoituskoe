def validoi_aika(aika: str) -> bool:
    """
    Tarkistaa, onko annettu aika kelvollinen 24 tunnin kellonajan muodossa.
    
    Palauttaa True, jos aika on kelvollinen, muuten False.
    """
    if len(aika) < 4 or len(aika) > 5:
        return False
    if ':' not in aika:
        return False
    osat = aika.split(':')
    if len(osat) != 2:
        return False
    
    tunti, minuutti = osat
    
    if not tunti.isdigit() or not minuutti.isdigit():
        return False

    tunti = int(tunti)
    minuutti = int(minuutti)
    if 0 <= tunti <= 23 and 0 <= minuutti <= 59:
        return True
    return False

if __name__ == "__main__":

    print(validoi_aika("0:10"))   # True
    print(validoi_aika("23:59"))  # True
    print(validoi_aika("30:30"))  # False
    print(validoi_aika("12:61"))  # False
    print(validoi_aika("0:1"))    # False
    print(validoi_aika("10"))     # False
    print(validoi_aika(":"))      # False
    print(validoi_aika("10:01:")) # False

