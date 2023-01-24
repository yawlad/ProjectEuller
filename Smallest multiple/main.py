# def lcm(a, b):
#     if a >= b:
#         gr = a
#     else:
#         gr = b
#     while True:
#         if gr % a == 0 and gr % b == 0:
#             return gr
#         gr+=1

def lcm(a, b):
    mul = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return mul // (a + b)

def find_smallest_multiple(start, end):
    result = 1
    for i in range(start, end+1):
        result = lcm(result, i) 
    return result

print(find_smallest_multiple(1,20))