import string

def wyczysc_tekst(tekst):
    translator = str.maketrans('', '', string.punctuation)
    return tekst.translate(translator).lower().split()

liczba_dokumentow = int(input("Ile dokumentów chcesz wprowadzić? "))

dokumenty = []

for i in range(liczba_dokumentow):
    dokument = input(f"Wpisz treść dokumentu {i+1}: ").strip()
    dokumenty.append(dokument)

liczba_slow = int(input("Ile słów chcesz szukać? "))

slowa = []

for i in range(liczba_slow):
    slowo = input(f"Wpisz słowo {i+1} do wyszukania: ").strip().lower()
    slowa.append(slowo)

wyniki = {}

for i, dokument in enumerate(dokumenty):
    dokument_id = f"Dokument {i+1}"
    wyniki[dokument_id] = {}
    
    oczyszczony_dokument = wyczysc_tekst(dokument)
    
    for slowo in slowa:
        liczba_wystapien = oczyszczony_dokument.count(slowo)
        wyniki[dokument_id][slowo] = liczba_wystapien

wyniki_listy = [[] for _ in range(liczba_slow)]

for i, slowo in enumerate(slowa):
    dokumenty_wyniki = sorted(range(liczba_dokumentow), key=lambda x: wyniki[f"Dokument {x+1}"][slowo], reverse=True)
    dokumenty_wyniki = [doc for doc in dokumenty_wyniki if wyniki[f"Dokument {doc+1}"][slowo] > 0]
    wyniki_listy[i] = dokumenty_wyniki

for lista in wyniki_listy:
    print(lista)
