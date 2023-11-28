print(1, 2 , 6, 5)


def test_var_args(farg, *args):
    print ("formal arg:", farg)
    print(args)
    for arg in args:
        print ("another arg:", arg)

test_var_args(1, "two", 3)


def test_var_kwargs(farg, **kwargs):
    print ("formal arg:", farg)
    for key in kwargs:
        print ("another keyword arg: %s: %s" % (key, kwargs[key]))
    print (kwargs)


test_var_kwargs(farg=1, myarg2="two", myarg3=3)




def funkcja1():
    print("*")

def funkcja2():
    print("#")

slownik = {'first': funkcja1, 'second': funkcja2}
klucz = input("first lub second: ")

if klucz in slownik:
    slownik[klucz]()

def funkcja1(x):
    suma = 1 +1
    return suma

def funkcja2(x):
    roznica = 4 - 3
    return roznica

slownik = { 'first': funkcja1, 'second': funkcja2 }

klucz = input("Podaj klucz")

funkcja = slownik[klucz]
print(funkcja(2))






def alphabet_range(end="Z", step=1, start="A"):
    return [chr(x) for x in range(ord(start), ord(end), step)]

alphabet_range('F')





#to jest generator
def alphabet_range(end="Z", step=1, start="A"):
    return (chr(x) for x in range(ord(start), ord(end), step))

alphabet_range('F')
list(alphabet_range('F'))





def _slownie_do999(n):
    lista = []
    if n >= 100:
        lista = [((n // 100) * 100, nazwy_setki[(n // 100) * 100])]
        n %= 100

    if n > 19:
        lista.append((n - n % 10, nazwy_dziesiatki[n - n % 10]))
        if n % 10 > 0:
            lista.append((n % 10, nazwy_jednosci[n % 10]))
    elif n > 10:
        lista.append((n, nazwy_nastki[n]))
    else:
        if n > 0:
            lista.append((n, nazwy_jednosci[n]))
    return lista



def _sklej(lista):
    return " ".join([x[1] for x in lista])



def dodaj_jednostke(lista, jednostki):
    print(f'Lista przy dodawaniu jednostek {lista}')
    if len(lista) == 1 and lista[0][0] == 1:
        lista = [(1, jednostki[0])]

    elif lista[-1][0] >= 2 and lista[-1][0] <= 4:
        lista.append((0, jednostki[1]))
    else:
        lista.append((0, jednostki[2]))
    return lista


def slownie_do999(n, jednostki=["", "", ""]):
    lista = _slownie_do999(n)
    lista = dodaj_jednostke(lista, jednostki)
    return _sklej(lista)


def slownie(n):
    jednosci = n % 1000
    tysiace = (n // 1000) % 1000
    miliony = n // 1_000_000 % 1000
    miliardy = n // 1_000_000_000 % 1000

    lista = [slownie_do999(miliardy, jednostki=["miliard", "miliardy", "miliardów"]),
        slownie_do999(miliony, jednostki=["milion", "miliony", "milionów"]),
        slownie_do999(tysiace, jednostki=["tysiąc", "tysiące", "tysięcy"]),
             slownie_do999(jednosci)]


    return " ".join(lista)




