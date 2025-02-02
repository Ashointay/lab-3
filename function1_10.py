def unique_elements(lst): 
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    return unique_lst

lst = list(map(int, input().split()))
print(unique_elements(lst))