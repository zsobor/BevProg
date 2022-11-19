import string

def destroy():
    with open("hazi.txt", "r", encoding="utf-8") as f:
        with open("rozsiKi.txt", "w", encoding="utf-8") as f2:
            line = f.readline()
            bad = string.punctuation + "aáeéiíoóöőuúüű"
            n = 1

            while line:
                s = ""
                line.strip("\n")
                for i in line:
                    if i not in bad:
                        s += i
                if n % 3 == 0:
                    f2.write(s)
                n += 1
                line = f.readline()

if __name__ == "__main__":
    destroy()