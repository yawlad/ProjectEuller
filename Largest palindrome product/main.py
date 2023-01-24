from math import floor

def check_palindrome(num):
    num = str(num)
    for digit_i in range(floor(len(num)/2)):
        if num[digit_i] != num[-(digit_i+1)]:
            return False
    return True


def find_palindrome(num_of_digits):
    result = 0
    for i in range(int('9'*num_of_digits),int('1' + '0' * (num_of_digits -1)),-1):
        for j in range(int('9'*num_of_digits),int('1' + '0' * (num_of_digits -1)),-1):
            temp = i*j
            if result < temp and check_palindrome(temp):
                result = temp
    return result

print(find_palindrome(3))