
def plus(x, y):
    return x + y


def minus(x, y):
    return x - y


def vermenigvuldigen(x, y):
    return x * y


def delen(x, y):
    return x / y


print("Wat wil je doen?")
print(" ")
print("1. - Plus (+)")
print("2. - Minus (-)")
print("3. - Vermenigvuldigen (x)")
print("4. - Delen (/)")
print(" ")

while True:
    keuze = input("Je kan kiezen uit(1, 2, 3, 4): ")
    if keuze in ('1', '2', '3', '4'):
        nummer1 = float(input("Eerste getal: "))
        nummer2 = float(input("Tweede getal: "))

        if keuze == '1':
            print(nummer1, "+", nummer2, "=", plus(nummer1, nummer2))

        elif keuze == '2':
            print(nummer1, "-", nummer2, "=", minus(nummer1, nummer2))

        elif keuze == '3':
            print(nummer1, "*", nummer2, "=",
                  vermenigvuldigen(nummer1, nummer2))

        elif keuze == '4':
            print(nummer1, "/", nummer2, "=", delen(nummer1, nummer2))

        volgende = input(
            "wil je nog eens een berekening doen? (ja/nee): ")
        if volgende == "nee":
            break

    else:
        print("Hmm... er klopt iets niet...")
