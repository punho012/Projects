def check_primality():
    number = input("Give me a number: ")
    number = int(number)
    for x in range(2, number):
        if number % x == 0:
            return "It is not prime number"
    return "It is prime number"
        
     

print(check_primality())

