# Määrittelydokumentti

## Opinto-ohjelma

Tietojenkäsittelytieteen kandidaatti (TKT).

## Dokumentaation kieli

Erillisen dokumentaation kieli on suomi. Koodikommentoinnin kieli on englanti.

## Ohjelmointikieli

Python (versio 3.12).

## Ohjelmointikielet vertaisarviointiin

Tällä kurssilla yleisimmiksi oletetuista kielistä (Python, Java ja C#) vain Pythonista on oikeasti osaamista. Kahta muuta ei ole paljoa tullut käytettyä, mutta ovat sen verran tuttuja, että vertaisarviointi sujunee tyydyttävästi. JavaScriptista on paljonkin kokemusta, mutta sitä tuskin kurssilla paljoa käytetään.

## Harjoitustyön kuvaus

Työssä tutkitaan musiikin generointia Markovin ketjujen eri asteilla, eli käytännössä trie-rakenne on keskiössä. Tavoitteena on tarkastella generoidun musiikin laatua ja mielekkyyttä sekä osuvuutta syötedataan nähden. Aikavertailua ei suoriteta.

## Syötteet

Ohjelma saa yksinkertaisen graafisen käyttöliittymän (tkinter) avulla syötteenä digitaalisessa muodossa nuotinnettua musiikkia (abc-notaatio tai midi), jota saa julkisista tietokannoista, kuten https://abcnotation.com/ ja https://www.mididb.com/. Tämän jälkeen ohjelma generoi syötteiden pohjalta musiikkia halutulla Markovin ketjun asteella trie-rakennetta hyödyntäen.

## Aika- ja tilavaativuudet

Trie-puun rakentaminen tapahtuu ajassa O(mn), jossa n on tallennettavien merkkijonojen määrä ja m näiden merkkijonojen pituuden keskiarvo. Trie-puussa operaatioiden (lisääminen, poistaminen ja etsintä) aika- ja tilavaativuudet on O(n) sekä keskimääräisesti että pahimmassa tapauksessa.

## Viitteet

Tarkat inspiraation lähteet eivät ole vielä tiedossa, mutta googlaamalla löytyy hyvin materiaalia esimerkiksi hakusanoilla "markov chain music generator python". Alla lisäksi muutama yleisempi lähde aiheeseen liittyen.

- Trie: https://en.wikipedia.org/wiki/Trie.
- Markovin ketju: https://en.wikipedia.org/wiki/Markov_chain.
- Markovin ketju musiikin generoinnissa: https://www.cs.cmu.edu/~music/cmsip/slides/05-algo-comp.pdf.

## Laajojen kielimallien käyttö

Työssä ei käytetä laajoja kielimalleja.
