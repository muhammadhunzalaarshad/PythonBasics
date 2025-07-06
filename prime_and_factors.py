def is_prime_number(number: int) -> bool:
    """
    Check if a given number is prime.

    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if number is prime, False otherwise.
    """
    if number <= 1:
        return False
    
    if number == 2:
        return True
    
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    
    return True

def find_factors(number: int) -> list[int]:
    """
    Find all factors of a given number

    Args:
        number (int): The number to find factor for.
    
    Returns:
        list[int]: A list of all factors of the number:
    """

    factors = []
    for divisor in range(1, number + 1):
        if number % divisor == 0:
            factors.append(divisor)
    
    return factors

def main():
    """Main fuction to handle user input and display results"""

    try:
        user_input = input("Enter a positive integer: ")
        number = int(user_input)

        if number < 0:
            print("Please enter a positive integer!")
            return 
        
        if is_prime_number(number):
            print(f"{number} is a prime number!")
        else:
            factors = find_factors(number)

            if factors:
                print(f"{number} is not a prime number. Its factor are: {factors}")
            else:
                print(f"{number} is not a prime!")

    except ValueError:
        print("Invalid input! Please enter a valid integer!")

if __name__ == "__main__":
    main()
