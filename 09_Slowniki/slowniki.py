s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2

s|={'e':5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}



napisy = []
czestosci = {}

while True:
    napis = input("Wprowadź dowolny napis: ")

    if not napis:
        break

    napisy.append(napis)

    if napis in czestosci:
        czestosci[napis] += 1
    else:
        czestosci[napis] = 1

print("Słownik ilości wystąpień napisów:")
for napis, ilosc in czestosci.items():
    print(f"{napis}: {ilosc}")













napisy = {}
while True:
    napis = input("Wprowadź dowolny napis: ")

    if not napis:
        break


    napisy[napis] = napisy.get(napis, 0) + 1


for napis, ilosc in napisy.items():
    print(f"{napis}: {ilosc}")








