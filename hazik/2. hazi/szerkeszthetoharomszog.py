def szerkesztheto(a, b, c):
    if (a + b > c) and (b + c > a):
        print(f"A {a}, {b} és {c} oldalú háromszög szerkeszthető.")
    else:
        print(f"A {a}, {b} és {c} oldalú háromszög NEM szerkeszthető.")

if __name__ == "__main__":
    print("Adja meg a háromszög három oldalát cm-ben:")
    a = input("a oldal (cm): ")
    b = input("b oldal (cm): ")
    c = input("c oldal (cm): ")
    szerkesztheto(a, b, c)