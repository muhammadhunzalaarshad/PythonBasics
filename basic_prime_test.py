def is_prime(number: int) -> bool:
    """
    Check if a given number is prime.

    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for divisor in range(3, int(number ** 0.5) + 1, 2):
        if number % divisor == 0:
            return False
    return True
    

def main() -> None:
    """Main function to handle user input and display result."""
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            raise ValueError("Please enter a positive number!")
        
        prime_status = is_prime(number)

        if prime_status:
            print(f"{number} is a prime!")
        else:
            print(f"{number} is not a prime!")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()