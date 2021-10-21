# Dokumentacja
## Endpoint /test_string/\<string\>

Wartość zwracana: uint8?

Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: występowanie dużych i małych liter, liczb, znaków specjalnych.
Jeżeli znaleziono znak z danej grupy, ustawiany jest odpowiedni bit w zwróconej wartości.
* Duże litery     (0x1)
* Małe litery     (0x2)
* Liczby          (0x4)
* Znaki specjalne (0x8)