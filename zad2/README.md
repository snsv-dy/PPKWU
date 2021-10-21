# Dokumentacja
## Endpoint: /test_string/\<string\>
### <b>Wartość zwracana: int</b>
### <b>Metoda: GET</b>

Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: dużych i małych liter, liczb oraz znaków specjalnych.
Jeżeli znak z danej grupy znajduje się stringu to ustawiany jest odpowiedni bit w zwracanej wartości.
| Typ | Ustawiony bit|
|:---|:---|
| Duże litery     | 0x1 |
| Małe litery     | 0x2 |
| Liczby          | 0x4 |
| Znaki specjalne | 0x8 |

### Przykłady

Zapytanie `/test_string/abcA`

Odpowiedź: `3`

---
Zapytanie `/test_string/a0"$`

Odpowiedź: `14`

---
Zapytanie `/test_string/J@CEK`

Odpowiedź: `9`
