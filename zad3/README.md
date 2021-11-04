# Dokumentacja
## Endpoint: /test_string/\<format\>/\<string\>
### <b>Wartość zwracana: dokument w wybranym formacie</b>
### <b>Metoda: GET</b>
### <b>Parametry URL</b>
| Nazwa | Typ | Dozwolone wartości |
|:---|:---|:---|
| Format     | String | txt, json, xml, csv |

<!-- Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: dużych i małych liter, liczb oraz znaków specjalnych.
Jeżeli znak z danej grupy znajduje się stringu to ustawiany jest odpowiedni bit w zwracanej wartości. -->
Zwraca wartość z endpointu <a href="https://github.com/snsv-dy/PPKWU/blob/master/zad2/README.md">/test_string</a> w wybranym formacie. W przypadku podania niepoprawnego formatu, zwracany jest pusty dokument.

### Przykłady

Zapytanie `/test_string/abcA`

Odpowiedź: `3`

---
Zapytanie `/test_string/a0"$`

Odpowiedź: `14`

---
Zapytanie `/test_string/J@CEK`

Odpowiedź: `9`
