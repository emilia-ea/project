from core import get_trigram, get_changed_lines, get_hexagram_result

def get_three_digit(prompt):
    while True:
        try:
            val = int(input(prompt))
            if 100 <= val <= 999:
                return val
            else:
                print("Number must be between 100 and 999.")
        except ValueError:
            print("Invalid input. Please enter a valid three-digit number.")

def main():
    num1 = get_three_digit("Enter the first three-digit number: ")
    num2 = get_three_digit("Enter the second three-digit number: ")
    num3 = get_three_digit("Enter the third three-digit number: ")

    upper = get_trigram(num1 % 8)
    lower = get_trigram(num2 % 8)
    original = f"{upper}\n{lower}"
    changed = get_changed_lines(original, num3 % 6)

    print("\nOriginal 6 lines:")
    print(original)
    print("Result:")
    print(get_hexagram_result(original))

    print("\nChanged 6 lines:")
    print(changed)
    print("Result:")
    print(get_hexagram_result(changed))

if __name__ == "__main__":
    main()
