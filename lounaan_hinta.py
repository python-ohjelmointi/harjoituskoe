def lounaan_hinta(ika: int) -> float:
    """
    Laske lounaan hinta annetun henkilön iän perusteella ja palauta
    tulos liukulukuna.
    """
    if ika <= 12:
        return 0.5 * ika
    else:
        return 12.9


if __name__ == "__main__":
    # Omia testejä
    print(lounaan_hinta(25))  # 12.9
    print(lounaan_hinta(7))   # 3.5
    print(lounaan_hinta(12))  # 6.0
    print(lounaan_hinta(0))   # 0.0, 0-vuotiaan lounas

