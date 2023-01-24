def find_sum_sqr_difference__v1(n):
    num_1 = 0
    num_2 = 0
    for i in range(n+1):
        num_1 += i**2
        num_2 += i
    return num_2**2 - num_1

def find_sum_sqr_difference__v2(n):
    num_1 = n*(n+1)*(2*n+1)/6
    num_2 = n*(n+1)/2
    return num_2**2 - num_1
    

print(find_sum_sqr_difference__v1(100))
print(find_sum_sqr_difference__v2(100))