
# MCA Semester I - Practical 3
# Control Flow & Utility Functions


def show_menu():
    print("\n=== Utility Calculator ===")
    print("1. Add numbers")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show summary")
    print("0. Exit")


def get_number(prompt="Enter a number: "):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def add(*args):
    return sum(args)


def calculate(a, b, operation="+"):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    else:
        raise ValueError("Unsupported operation.")


def show_summary(**kwargs):
    print("\n--- Summary ---")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            break

        elif choice not in {"1", "2", "3", "4", "5"}:
            print("Invalid menu choice. Try again.")
            continue

        elif choice == "5":
            show_summary(
                total_calculations=len(history),
                last_result=history[-1] if history else "No calculations yet"
            )
            continue

        a = get_number("First number: ")
        b = get_number("Second number: ")

        if choice == "1":
            result = add(a, b)
            label = "addition"

        elif choice == "2":
            result = calculate(a, b, "-")
            label = "subtraction"

        elif choice == "3":
            result = calculate(a, b, "*")
            label = "multiplication"

        else:
            try:
                result = calculate(a, b, "/")
            except ZeroDivisionError as error:
                print("Error:", error)
                continue

            label = "division"

        format_result = lambda value: f"{value:.2f}"
        print(f"Result ({label}): {format_result(result)}")
        history.append(result)


# extension Task A 
def average(a, b, c):
    return (a + b + c) / 3


#extension Task B 
def grade_from_marks(marks, maximum=100):
    if maximum <= 0:
        return "Maximum marks must be positive"

    if marks < 0 or marks > maximum:
        return "Invalid marks"

    percentage = (marks / maximum) * 100

    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"


# Extension Task C 
def scope_demo():
    message = "Hello Python"
    print(message)


# Extension Task D 
def test_add():
    print("add(2, 4, 6, 8) =", add(2, 4, 6, 8))


# Extension Task E 
def test_summary():
    show_summary(
        student="Student A",
        practical=3,
        status="Complete"
    )


#task demonstrations
def run_extensions():
    print("\n===== EXTENSION TASK A: AVERAGE =====")
    print("Average:", average(10, 20, 30))

    print("\n===== EXTENSION TASK B: GRADE =====")
    print("Grade:", grade_from_marks(85))
    print("Invalid marks:", grade_from_marks(120))

    print("\n===== EXTENSION TASK C: SCOPE =====")
    scope_demo()

    # Uncomment the next line to access the variable outside the function 
    # print(message)

    print("\n===== EXTENSION TASK D: *args =====")
    test_add()

    print("\n===== EXTENSION TASK E: **kwargs =====")
    test_summary()


if __name__ == "__main__":
    main()
    run_extensions()
