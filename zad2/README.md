# Dokumentacja
## Endpoint /test_string/\<string\>

Wartość zwracana: int

Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: występowanie dużych i małych liter, liczb, znaków specjalnych.
Jeżeli znaleziono znak z danej grupy, ustawiany jest odpowiedni bit w zwróconej wartości.
| Typ | Ustawiony bit|
|:---|:---|
| Duże litery     | 0x1 |
| Małe litery     | 0x2 |
| Liczby          | 0x4 |
| Znaki specjalne | 0x8 |

### Przykłady
---
Zapytanie `/test_string/abcA`

Odpowiedź: `3`

---
Zapytanie `/test_string/a0"&`

Odpowiedź: `14`

---
Zapytanie `/test_string/J/\CEK`

Odpowiedź: `9`
