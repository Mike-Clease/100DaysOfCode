def prime_checker(number):
    not_prime = False
    if number == 1:
        not_prime = True
    else:
        for n in range(2, number):
            not_prime = (number % n) == 0

            if not_prime:
                break
        
    if not_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


num = int(input("Check this number: "))
prime_checker(num)