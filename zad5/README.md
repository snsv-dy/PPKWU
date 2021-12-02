# Dokumentacja
## Endpoint: /query/<szukana firma>
### <b>Metoda: GET</b>
### <b>Wartość zwracana: Dokument html z listą wyników</b>
### <b>Parametry ścieżki:</b>
| Nazwa | Typ | Opis |
|:---|:---|:---|
| szukana firma | String | Wartość którą będzie odbywało się wyszukiwanie na stronie panorama firm. |

Wyszukuje firmy za pomocą wyszukiwarki panorama firm i zwraca dokument html z listą wyników oraz możliwością wygenerowania wizytówki w formacie vcard.

&nbsp;

### Przykłady

Zapytanie `/query/szkoła`

Odpowiedź: 
```
Generuj vcard Nazwa firmy: CK EDUKATOR Anna Sowińska , telefon: 793 804 545, email: edukatorkielce@op.pl, address: ul. Jagiellońska 90, 25-734 Kielce
Generuj vcard Nazwa firmy: CK EDUKATOR Anna Sowińska , telefon: 793 804 545, email: edukatorkielce@op.pl, address: ul. Jagiellońska 90, 25-734 Kielce
Generuj vcard Nazwa firmy: Euronauka , telefon: 607 172 688, email: sekretariat@euronauka.eu, address: ul. Harcerska 18, 63-000 Środa Wielkopolska
Generuj vcard Nazwa firmy: Euronauka , telefon: 607 172 688, email: sekretariat@euronauka.eu, address: ul. Harcerska 18, 63-000 Środa Wielkopolska 
```