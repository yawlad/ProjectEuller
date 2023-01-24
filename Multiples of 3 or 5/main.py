def find_multipliers_sum(n):
    sum = 0
    for num in range(3,n,3):
        if num % 5 == 0:
            continue
        sum+=num
    for num in range(5,n,5):
        sum+=num
    return sum

print(find_multipliers_sum(15))