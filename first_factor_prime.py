def is_prime(number: int) -> tuple[bool, int | None]:
    """
    Check if a given number is prime

    Args:
        number (int): The number to check for primality.

    Returns:
        tuple: (bool, int or None) - (is_prime, first_factor if nor prime, else None)
    """
    if number <= 1:
        return False, None
    if number == 2:
        return True, None
    
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False, divisor
    
    return True, None

def main():
    """Main Function to handle user input and display result"""
    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)

        if number <= 0:
            print("Please enter a non-positive integer!")
            return
        
        prime_status, first_factor = is_prime(number)

        if prime_status:
            print(f"{number} is a prime number.")
        else:
            if first_factor:
                print(f"{number} is not a prime number! First factor found {first_factor}")
            else:
                print(f"{number} is not a prime number!")

    except ValueError:
        print("Invalid input! Please enter a valid integer")

if __name__ == "__main__":
    main()


