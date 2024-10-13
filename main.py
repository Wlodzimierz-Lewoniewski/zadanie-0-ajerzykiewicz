import string

# Funkcja do czyszczenia tekstu z interpunkcji i zamieniania na małe litery
def wyczysc_tekst(tekst):
    translator = str.maketrans('', '', string.punctuation)  # Usunięcie znaków interpunkcyjnych
    return tekst.translate(translator).lower().split()  # Zamiana na małe litery i podział na wyrazy

# Pobranie liczby dokumentów
liczba_dokumentow = int(input("Ile dokumentów chcesz wprowadzić? "))

# Inicjalizacja listy dokumentów
dokumenty = []

# Wprowadzanie dokumentów
for i in range(liczba_dokumentow):
    dokument = input(f"Wpisz treść dokumentu {i+1}: ").strip()
    dokumenty.append(dokument)

# Pobranie liczby słów do wyszukania
liczba_slow = int(input("Ile słów chcesz szukać? "))

# Inicjalizacja listy słów
slowa = []

# Wprowadzanie słów
for i in range(liczba_slow):
    slowo = input(f"Wpisz słowo {i+1} do wyszukania: ").strip().lower()  # Zamiana na małe litery
    slowa.append(slowo)

# Słownik do przechowywania wyników wyszukiwania
wyniki = {}

# Przetwarzanie dokumentów i zliczanie wystąpień słów
for i, dokument in enumerate(dokumenty):
    dokument_id = f"Dokument {i+1}"
    wyniki[dokument_id] = {}
    
    # Oczyszczenie dokumentu i rozbicie na wyrazy
    oczyszczony_dokument = wyczysc_tekst(dokument)
    
    for slowo in slowa:
        liczba_wystapien = oczyszczony_dokument.count(slowo)  # Zliczanie słowa w oczyszczonym dokumencie
        wyniki[dokument_id][slowo] = liczba_wystapien

# Tworzenie list wyników
wyniki_listy = [[] for _ in range(liczba_slow)]

# Wypisywanie dokumentów z największą liczbą wystąpień słów
for i, slowo in enumerate(slowa):
    dokumenty_wyniki = sorted(range(liczba_dokumentow), key=lambda x: wyniki[f"Dokument {x+1}"][slowo], reverse=True)
    wyniki_listy[i] = dokumenty_wyniki

# Wypisywanie wyników
for lista in wyniki_listy:
    print(lista)
