def bubbleSort(list):
    for i in range(0, len(list)):
        for j in range(1, len(list) - 1):
            if list[j - 1] > list[j]:
                list[j], list[j - 1] = list[j - 1], list[j]
    print(f"A rendezett lista: {list}")

def binarySearch(list, num):
    low, high = 0, len(list) - 1
    step = 0
    while low <= high:
        k = (low + high) // 2
        step += 1
        if num < list[k]:
            high = k - 1
        elif num > list[k]:
            low = k + 1
        else:
            print(f"{step} lépésből találta meg a számot.\nFelső: {high}\nAlsó: {low}\n'K' értéke: {k}")
            break
    else:
        print(f"Nem találta meg a számot :(\nFelső: {high}\nAlsó: {low}\n'K' értéke: {k}")


if __name__ == "__main__":
    list = [54, 76, 23, 45, 21, 5, 67, 22, 12, 64, 26, 59, 82, 99]
    bubbleSort(list)
    list = [2, 5, 6, 8, 13, 32, 42, 50, 53, 62, 66, 70, 80, 89, 91]
    num = 70
    binarySearch(list, num)