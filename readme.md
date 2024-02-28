# Python-ohjelmointi -kurssin harjoituskoe

Tämä harjoituskoe sisältää viisi tehtävää. Kukin tehtävänanto löytyy `.py`-tiedostosta, johon myös ratkaisu tulee toteuttaa.

Voit tallentaa tehtävät itsellesi joko yksitellen, kloonata projektin Gitin avulla tai ladata kaikki tiedostot yhtenä [zip-pakettina](https://github.com/python-ohjelmointi/harjoituskoe/archive/refs/heads/main.zip).


## Tehtävien testaaminen

Tehtävänannot sisältävät [doctest-testejä](https://docs.python.org/3/library/doctest.html), joiden avulla voit testata ohjelmasi toimintaa. Doctest-testit saat suoritettua oletuksena komennolla `python3 -m doctest --verbose tiedosto.py`. Mikäli Python on asennettuna sinulla eri nimellä, komento voi olla vaihtoehtoisesti esim. `py -m doctest --verbose tiedosto.py` tai `python -m doctest --verbose tiedosto.py`.

Mikäli et saa doctest-testejä suoritettua harjoituskokeessa pyydä asiaan apua kurssin ohjaajilta tai muilta osallistujilta. Varsinaisen kokeen testit tulevat noudattamaan samaa mallia.


## Muutokset, tulosteet ja syötteet

Huomaa, että automaattisen arvioinnin vuoksi **et saa muuttaa funktioiden nimiä etkä niiden parametreja**. Ratkaisusi eivät saa myöskään kysyä käyttäjältä tietoja tai tehdä tulosteita, ellei näin ole ohjeistettu tehtävänannossa. Mikäli toteutat omia testejä ja kokeiluja, toteuta ne tehtäväpohjissa oleviin `if __name__ == "__main__":`-lohkoihin.


## Tehtävät

Harjoituskoe koostuu seuraavista tehtävistä, jotka ovat esitetty suuntaa-antavasti haastavuuden mukaan kasvavassa järjestyksessä:

1. [Lounaan hinta](./lounaan_hinta.py)
2. [Keskimmäinen merkki](./keskimmainen_merkki.py)
3. [Kellonajan validointi](./kellonajan_validointi.py)
4. [Peräkkäisten numeroiden tarkistus](./perakkaiset.py)
5. [Sähköpotkulaudan vuokraus](./sahkopotkulauta.py)


## Tyyppivihjeet

Näissä tehtäväpohjissa on hyödynnetty [tyyppivihjeitä (type hint)](https://docs.python.org/3/library/typing.html), jotka auttavat koodin ymmärtämisessä ja virheiden välttämisessä. Jos tyyppivihjeet sekoittavat sinua tai aiheuttavat ongelmia, voit poistaa ne tehtävistä. Tyyppivihjeiden tarkoituksena on helpottaa tehtävän ratkaisua, mutta niiden käyttö ei ole pakollista.
