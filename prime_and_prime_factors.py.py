def is_prime(number: int) -> bool:
    """
    Determine whether a given number is prime.

    Args:
        number (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime False otherwise. 
    """
    if number <= 1:
        return False
        
    if number == 2:
         return True
        
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
        
    return True

def get_prime_factors(number: int) -> list[int]:
    """
    Computes the prime factors of a given positive integer.  

    Args:
        number (int): A positive integer to factorize.
    
    Returns:
        list[int]: A list of prime factors in ascending order.

    Raises:
        valueError: If the input number is less than or equal to 1
    """
    if number <= 1:
        raise ValueError("Input must be a positive integer greather than 1")
    
    prime_factors = []
    potential_factor = 2

    while number > 1:
        if number % potential_factor == 0:
            number //= potential_factor
            prime_factors.append(potential_factor)
        else:
            potential_factor += 1 if potential_factor == 2 else 2

    return prime_factors

def main():
    """
    Handles user input, validates it, and displays whether the number is prime
    or its prime factors if it is not prime.
    """
    try:
        user_input = int(input("Enter a positive integer: "))
        number = int(user_input)

        if number <= 0:
            print("Please enter a positive integer!")
            return
        
        if is_prime(number):
            print(f"{number} is a prime number!")
        else:
            factors = get_prime_factors(number)
            print(f"{number} is not a prime number. prime factor are: {factors}")
    
    except ValueError:
        print("Invalid input! Please enter a valid positive integer!")

if __name__ == "__main__":
    main()
        

    