# Dokumentacja
## Endpoint: /convert_string/\<format źródłowy\>/\<format docelowy\>/\<string\>
### <b>Metoda: GET</b>
### <b>Wartość zwracana: dokument w wybranym formacie docelowym</b>
### <b>Parametry ścieżki:</b>
| Nazwa | Typ | Opis |
|:---|:---|:---|
| format źródłowy | String | Określa format dokumentu który zostanie pobrany z endpointu <a href="https://github.com/snsv-dy/PPKWU/blob/master/zad3/README.md">/test_string</a> . Musi być jedną z wartości: txt, json, xml, csv. |
| format docelowy | String | Określa format dokumentu który zostanie zwrócony w odpowiedzi. Przyjmuje takie same wartości jak format źródłowy. |
| string | String | String przekazywany do endpointu /test_string |

<!-- Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: dużych i małych liter, liczb oraz znaków specjalnych.
Jeżeli znak z danej grupy znajduje się stringu to ustawiany jest odpowiedni bit w zwracanej wartości. -->
&nbsp;

Zwraca wartość z endpointu <a href="https://github.com/snsv-dy/PPKWU/blob/master/zad2/README.md">/test_string</a> zewnętrznej aplikacji w wybranym formacie. W przypadku podania niepoprawnego formatu, zwracany jest pusty dokument.

&nbsp;

### Przykłady

Zapytanie `/test_string/json/txt/abc`

Odpowiedź: 
```
Rodzaj znaków: 2.
```

---
Zapytanie `/test_string/xml/json/a0"$`

Odpowiedź: 
```
{
	"rodzaj_znakow": "14"
}
```

---
Zapytanie `/test_string/txt/xml/J@CEK`

Odpowiedź: 
```
<?xml version="1.0" encoding="UTF-8"?>
<rodzaj_znakow>9</rodzaj_znakow>
```
---
Zapytanie `/test_string/csv/csv/ONLYUPPER`

Odpowiedź: 
```
"Rodzaj znaków"
1
```

## Endpoint: /convert_string/\<format źródłowy\>/\<format docelowy\>
### <b>Metoda: POST</b>
### <b>Wartość zwracana: dokument w wybranym formacie docelowym</b>
### <b>Parametry ścieżki:</b>
| Nazwa | Typ | Opis |
|:---|:---|:---|
| format źródłowy | String | Określa format dokumentu który został przekazany w zawartości żądania. Musi być jedną z wartości: txt, json, xml, csv. |
| format docelowy | String | Określa format dokumentu który zostanie zwrócony w odpowiedzi. Przyjmuje takie same wartości jak format źródłowy. |

<!-- Sprawdza zawartośc przekazanego stringa pod kątem występowania w nim: dużych i małych liter, liczb oraz znaków specjalnych.
Jeżeli znak z danej grupy znajduje się stringu to ustawiany jest odpowiedni bit w zwracanej wartości. -->
&nbsp;

Kontwertuje przekazany w żądaniu string na wybrany przez użytkownika format. W przypadku podania niepoprawnego formatu lub danych niezgodnych z wybranym formatem, zwracany jest pusty dokument.

&nbsp;

### Przykłady

Zapytanie `/test_string/json/txt`

Zawartość żądania: 
```
{
	"rodzaj_znakow": "2"
}
```

Odpowiedź: 
```
Rodzaj znaków: 2.
```

---
Zapytanie `/test_string/xml/json/a0"$`

Zawartość żądania: 
```
<?xml version="1.0" encoding="UTF-8"?>
<rodzaj_znakow>14</rodzaj_znakow>
```
Odpowiedź: 
```
{
	"rodzaj_znakow": "14"
}
```

---
Zapytanie `/test_string/txt/xml/J@CEK`

Zawartość żądania: 
```
Rodzaj znaków: 9.
```
Odpowiedź: 
```
<?xml version="1.0" encoding="UTF-8"?>
<rodzaj_znakow>9</rodzaj_znakow>
```
---
Zapytanie `/test_string/txt/csv/ONLYUPPER`

Zawartość żądania: 
```
Rodzaj znaków: 1.
```
Odpowiedź: 
```
"Rodzaj znaków"
1
```
