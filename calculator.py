while True:
    print("\nSimple Calculator")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Divide")
    print("0) Quit")

    choice = input("Choose 0-4: ").strip()
    if choice == "0":
        print("Goodbye")
        break
    if choice not in ("1", "2", "3", "4"):
        print("Enter 0, 1, 2, 3 or 4")
        continue

    a_text = input("First number: ").strip()
    b_text = input("Second number: ").strip()

    def parse_number(s):
        if s == "":
            return None
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        if s.isdigit():
            return sign * int(s)
        return None

    a = parse_number(a_text)
    b = parse_number(b_text)
    if a is None or b is None:
        print("Invalid number. Use whole numbers like 3 or -2.")
        continue

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        if b == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", a // b)
