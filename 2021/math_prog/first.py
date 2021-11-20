def isSorted(array):
    for iterator in range(len(array)-1):
        if array[iterator] > array[iterator+1]:
            return False

    return True

def swap(indexes, target, exception):
    for index in range(len(indexes)//2):
        last = len(indexes) - 1 - index
        if indexes[index] == exception or indexes[last] == exception:
            continue
        first = target[indexes[index]]
        target[indexes[index]] = target[indexes[last]]
        target[indexes[last]] = first

dancers_count, mayor, o_o = input("").split(" ")[0:3]

dancers_count = int(dancers_count)
mayor = int(mayor) - 1

dancers = input("").split(" ")[0:dancers_count]
last = dancers.copy()
dv = []
steps = []

while not isSorted(dancers):
    for index in range(len(dancers)):
        if index != len(dancers) - 1:
            if dancers[index] > dancers[index+1]:
                dv.append(index)
                continue

        if (len(dv) > 0):
            dv.append(index)
            swap(dv, dancers, 2)
            steps.append([dv[0], dv[-1]])
            dv.clear()

    if last == dancers:
        print("NE")
        exit()
    last = dancers

print("ANO")

if int(o_o) > 0:
    print(len(steps))
    for step in steps:
        print(f"{step[0]+1} {step[1]+1}")
