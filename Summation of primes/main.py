def find_sum_primes_below_num(num):
    primes = []
    sum = 0
    for i in range(num + 1):
        if i == 1:
            primes.append(0)
            continue
        primes.append(i)
            
    i = 2
    while i <= num:
        if primes[i] != 0:
            sum+=i
            j = i*2
            while j <= num:
                primes[j] = 0
                j += i
        i += 1
    return sum

print(find_sum_primes_below_num(2000000))