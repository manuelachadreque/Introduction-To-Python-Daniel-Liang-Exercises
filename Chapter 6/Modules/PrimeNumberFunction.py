def isPrime(number):
    divisor = 2
    while divisor <= number/2:
        if number % 2 == 0:
            return False
        divisor += 1
    return  True

def printPrimeNumbers(numberOfPrimes):
    NUMBEROFPRIMES = 50 # Numbers of primes to display
    NUMBER_OF_PRIMES_PER_LINE = 10

    count = 0
    number =2

    while count <= numberOfPrimes:
        count +=1
        print(number, end=' ')
        if count % NUMBER_OF_PRIMES_PER_LINE == 0:
            print()

        number +=1

def main ():
    print("The first 50 numbers are ")
    printPrimeNumbers(50)

main()

