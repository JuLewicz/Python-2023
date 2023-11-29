l = list(range(5, 10))
print(l)
try:
    i = int(input("podaj indeks "))
    print(f'Pod indeksem {i} jest element {l[i]}')
except IndexError as e:
    print(e)
except ValueError as e:
    print("In value error")
    print(e)
except Exception as e:
    print(e)
else:
    print("Koniec")
finally:
    print("Finally")


while True:
    try:
        i = int(input("Podaj liczbę: "))
        suma_cyfr = sum(int(a) for a in str(i))
        print("Suma cyfr:", suma_cyfr)
    except ValueError as e:
        print("Wprowadzono nieprawidłową liczbę. Spróbuj ponownie.")
        print(e)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd.")
        print(e)
    else:
        print("Koniec")
        break
    finally:
        print("Finally")








