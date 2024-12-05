def sahkopotkulaudan_vuokra(aloitusaika: str, lopetusaika: str) -> float:
    """
    Laskee ja palauttaa sähköpotkulaudan vuokrauksen hinnan aloitus- ja lopetusaikojen perusteella.
    """
    def aika_minuutteina(aika: str) -> int:
        tunteja, minuutteja = map(int, aika.split(":"))
        return tunteja * 60 + minuutteja
    
    aloitus_minuutit = aika_minuutteina(aloitusaika)
    lopetus_minuutit = aika_minuutteina(lopetusaika)
    
    if lopetus_minuutit < aloitus_minuutit:
        lopetus_minuutit += 24 * 60  # Lisätään 24 tuntia minuutteina
    
    vuokrausaika = lopetus_minuutit - aloitus_minuutit
    
    hinta = 1 + vuokrausaika * 0.25
    
    return hinta


if __name__ == "__main__":
    """
    Kirjoita mahdolliset omat testit ja kokeilut tähän lohkoon.
    Voit myös halutessasi poistaa tämän if-lohkon.
    """

    print(sahkopotkulaudan_vuokra("0:00", "1:00"))  # 16.0
    print(sahkopotkulaudan_vuokra("10:00", "11:30"))  # 23.5
    print(sahkopotkulaudan_vuokra("9:59", "10:00"))  # 1.25
    print(sahkopotkulaudan_vuokra("23:30", "1:15"))  # 27.25
