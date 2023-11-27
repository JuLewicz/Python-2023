n = 5

while n > 0:
    print(n)
    n -= 1   #sprawdzaj co o 1 mniejszą liczbe

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    if n < 3:
        break
    print(f'{n} tak')
else:
    print('Koniec')

n = 8
while n > 0:
    n -= 1
    if n % 2 == 0:
        print(f'{n} tik')
        continue

    print(f'{n} tak')
else:
    print('Koniec')


i=0
while i<100:
    i+=1
    if i % 2 == 0 and (i % 10 + i // 10) % 7 == 0:
        print(i)
        continue
else:
    print('Koniec')








# rozwiązanie JL

liczba = input("Podaj liczbę: ")

suma_cyfr = 0

for cyfra in liczba:

    suma_cyfr += int(cyfra)

print(f"Suma cyfr liczby {liczba} wynosi: {suma_cyfr}")


#rozwiązanie MK

n = int(input('podaj liczbe'))
print(f'Podałeś liczbę: {n}')

suma = 0
while n>0:
    suma += n%10
    n//=10
print(suma)
