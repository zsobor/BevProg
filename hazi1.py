def betuk_gyakorisaga(mondat):
    megszamolt_betuk = {}

    for i in range(len(mondat)):
        if (mondat[i]) not in megszamolt_betuk:
            megszamolt_betuk[mondat[i]] = 1
        else:
            megszamolt_betuk[mondat[i]] += 1

    print("Betűk gyakorisága: ", megszamolt_betuk)

if __name__ == "__main__":
    print("Adjon meg egy mondatot:")
    text = str(input())
    betuk_gyakorisaga(text)
    print("Fordítva:", text[::-1])
    print("Listába rendezve szavanként:", text.split(' '))