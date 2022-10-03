def convert(number, unit):
    if unit == "inch":
        print(number * 2.54, "cm")
    elif unit == "cm":
        print(number / 2.54, "inches")
    else:
        print("Not correct unit!")

if __name__ == "__main__":
    print("Adjon meg egy számot és egy mértékegységet (cm/inch):")
    szam = float(input())
    mertek = str(input())
    convert(szam,mertek)

