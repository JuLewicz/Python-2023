l = [3, 5, 6, 7]
l

l[1]   #drugi element listy - w pythonie liczymy od 0!
l[0]
len(l)
l[0:2]    #przedział otwarty z prawej
l[1:2]
l[1:]    #lista od konkretnego elementu do końca
l[:2]
l[-1]     #ostatni element
l[1:-1]    #OD DRUGIEGO DO przedostatniego elementu
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop()
l

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'
s2.join(["Ala", "ma", "kota"])

'.' in s2


napisy = []

while True:
    napis = input("Wprowadź dowolne słowo: ")

    if not napis:
        break

    napisy.append(napis)
    napisy.sort()

print(napisy)





napisy = []

while True:
    napis = input("Wprowadź dowolną liczbę: ")

    if not napis:
        break

    try:
        liczba = int(napis)
    except ValueError:
        print("To nie jest liczba. Spróbuj ponownie.")
        continue

    if liczba % 2 == 0:
        ostatnia_parzysta = liczba

try:
    print("Ostatnia parzysta liczba:", ostatnia_parzysta)
except NameError:
    print("Nie wprowadzono żadnej parzystej liczby.")


