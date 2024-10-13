liczba_dokumentow = int(input("Ile dokumentów chcesz wprowadzić? "))


dokumenty = []

for i in range(liczba_dokumentow):
    dokument = input(f"Wpisz treść dokumentu {i+1}: ").strip()
    dokumenty.append(dokument)

liczba_slow = int(input("Ile słów chcesz szukać? "))


slowa = []

for i in range(liczba_slow):
    slowo = input(f"Wpisz słowo {i+1} do wyszukania: ").strip()
    slowa.append(slowo)


wyniki = {}


for i, dokument in enumerate(dokumenty):
    dokument_id = f"Dokument {i+1}"
    wyniki[dokument_id] = {}
    
    for slowo in slowa:
        liczba_wystapien = dokument.lower().split().count(slowo.lower())
        wyniki[dokument_id][slowo] = liczba_wystapien

wyniki_listy = [[] for _ in range(liczba_slow)]


for i, slowo in enumerate(slowa):
    dokumenty_wyniki = sorted(range(liczba_dokumentow), key=lambda x: wyniki[f"Dokument {x+1}"][slowo], reverse=True)
    wyniki_listy[i] = dokumenty_wyniki

for lista in wyniki_listy:
    print(lista)
