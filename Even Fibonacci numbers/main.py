def get_result_sum(max_number):
    result = 0
    current_d = 1
    next_d = 2
    counter = 2
    while(current_d < max_number):
        if(counter == 3):
            result+=current_d
            counter = 0
        current_d, next_d = next_d, current_d + next_d
        counter+=1
    return result

print(get_result_sum(4000000))