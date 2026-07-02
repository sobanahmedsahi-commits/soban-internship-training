def right_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

def inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print("*" * i)

def pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))

def numbers_triangle(rows):
    for i in range(1, rows + 1):
        for x in range(1, i + 1):
            print(x, end=" ")
        print()

def main():
    print("enter which pattern")
    print("1 for right angle triangle")
    print("2 for inverted triangle")
    print("3 for pyramid")
    print("4 for numbers triangle")

    choice = int(input("choice: "))
    rows = int(input("rows: "))

    if choice == 1:
        right_triangle(rows)
    elif choice == 2:
        inverted_triangle(rows)
    elif choice == 3:
        pyramid(rows)
    elif choice == 4:
        numbers_triangle(rows)
    else:
        print("invalid choice!")

main()