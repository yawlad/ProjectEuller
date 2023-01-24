def factorization(number):
    dividers_list = []
    divider = 2
    while divider**2 <= number:
        if number % divider == 0:
            dividers_list.append(divider)
            number //= divider
        else:
            divider += 1
    if number > 1:
        dividers_list.append(number)
    return dividers_list

def find_largest_prime_factor(num):
    div_list = factorization(num)
    return div_list[len(div_list)-1]

print(find_largest_prime_factor(600851475143))