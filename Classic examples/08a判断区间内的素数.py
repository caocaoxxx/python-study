def is_primes(number):
    for i in range(2,number):
        if number % i == 0:
            return False

        

def print_primes(begin,end):
    for number in range(begin,end+1):
        if is_primes(number):
            print(f'{number}是素数')
begin = 11
end = 25
print_primes(begin,end)