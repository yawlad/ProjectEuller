def find_triplet_from_nums_sum(sum_):
    triplet_list = []
    for m in range(1, sum_):
        n = (sum_ - 2*m**2)/(2*m)
        
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        
        if a <= 0 or b <=0 or c <= 0:
            continue
        if int(a) != float(a):
            continue
        
        triplet_list.append((a,b,c))
    return triplet_list
        
    
      
print(find_triplet_from_nums_sum(1000))