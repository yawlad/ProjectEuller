def find_primes_in_range(n):
    primes = []
    for i in range(n + 1):
        if i == 1:
            primes.append(0)
            continue
        primes.append(i)
            
    i = 2
    while i <= n:
        if primes[i] != 0:
            j = i*2
            while j <= n:
                primes[j] = 0
                j += i
        i += 1
    primes = set(primes)
    primes.remove(0)
    primes = list(primes)
    primes.sort()
    return primes

def find_nth_prime(n):
    numbers = 4*n
    while True:
        try:
            return find_primes_in_range(numbers)[n-1]
        except IndexError:
            numbers*=4
        
print(find_nth_prime(10001))