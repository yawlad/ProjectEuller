def make_palindrome(n):
   n = str(n) 
   return int(n + n[::-1])

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

def check_primals(num_list, number_of_digits):
    max_number = int('9'*number_of_digits)
    if num_list[-1] > max_number:
        return False
    
    temp_l = num_list.copy()
    list_len = len(temp_l)
    count = 0
    
    i = 0
    j = 1
    
    while i < (len(num_list)):
        while j < (len(num_list)):
            mul = temp_l[i]*temp_l[j]
            if mul > max_number:
                ############################
                # NEED TO REBUID THIS PART #
                ############################
                temp_l = num_list.copy()
                j-= (count-1)
                count = 0
                ############################
                continue 
            else:
                temp_l[i] = mul
                count+=1
                if list_len - count == 2:
                    return True
            j+=1
        i+=1
        j=i+1
                
def find_palindrome(number_of_digits):
    result = ''
    for i in range(int('9'*number_of_digits),int('1' + '0' * (number_of_digits -1)),-1):
        pal = make_palindrome(i)
        if check_primals(factorization(pal), number_of_digits):
            result = pal
            return result

# print(find_palindrome(2))
check_primals(factorization(9009), 2)