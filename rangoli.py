def my_string(number, row):
    myList = []
    loop = row
    myString = ""

    while (loop > 0):
        myList.append(chr(96 + number - row + loop))
        loop -= 1

    loop = 1
    while (loop <= (row - 1)):
        myList.append(chr(96 + number - row + loop + 1))
        loop += 1

    for x in range(len(myList)):
        myString = myString + myList[x] + "-"

    # truncate the last -
    return myString[:-1]


def print_rangoli(size):
    width = (4 * size) - 3

    for x in range(1, size + 1):
        print '{:-^{w}}'.format(my_string(size, x), w=width)

    for x in range(size - 1, 0, -1):
        print '{:-^{w}}'.format(my_string(size, x), w=width)


if __name__ == '__main__':
    n = int(raw_input("Enter number less than 27:"))
    print_rangoli(n)