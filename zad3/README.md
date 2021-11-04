# Dokumentacja
## Endpoint: /test_string/\<format\>/\<string\>
### <b>Metoda: GET</b>
### <b>Wartość zwracana: dokument w wybranym formacie</b>
### <b>Parametry ścieżki:</b>
| Nazwa | Typ | Opis |
|:---|:---|:---|
| format     | String | Określa format zwracanego dokumentu. Musi być jedną z wartości: txt, json, xml, csv. |
| string | String | String przekazywany do endpointu <a href="https://github.com/snsv-dy/PPKWU/blob/master/zad2/README.md">/test_string</a> |

<!-- Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: dużych i małych liter, liczb oraz znaków specjalnych.
Jeżeli znak z danej grupy znajduje się stringu to ustawiany jest odpowiedni bit w zwracanej wartości. -->
&nbsp;

Zwraca wartość z endpointu <a href="https://github.com/snsv-dy/PPKWU/blob/master/zad2/README.md">/test_string</a> w wybranym formacie. W przypadku podania niepoprawnego formatu, zwracany jest pusty dokument.

&nbsp;

### Przykłady

Zapytanie `/test_string/txt/abc`

Odpowiedź: `Rodzaj znaków: 2.`

---
Zapytanie `/test_string/json/abc`

Odpowiedź: <code>
{
	"rodzaj_znaków": "2"
}
</code>

---
Zapytanie `/test_string/xml/abc`

Odpowiedź: ``
