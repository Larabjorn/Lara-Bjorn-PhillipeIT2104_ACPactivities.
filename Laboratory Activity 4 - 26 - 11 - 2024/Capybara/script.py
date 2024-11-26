from Capybara import Capybara

def main():
    capybaras = [
        Capybara("Biscoff", "M", 5),
        Capybara("Cappuccino", "F", 3),
        Capybara("Toffee", "M", 7),
    ]

    try:
        test_case_number = int(input("Enter the test case number: "))

        if 1 <= test_case_number <= len(capybaras):
            selected_capybara = capybaras[test_case_number - 1]
            print(f"Test Case {test_case_number}: {selected_capybara}")
        else:
            print("Invalid test case number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
