def insertion_sort(n):
    lenght = len(n) 

    if lenght <= 1:
        return  
    for i in range(1, lenght): 
        key = n[i]  
        j = i-1
        while j >= 0 and key < n[j]:  
            n[j + 1] = n[j]
            j -= 1
        n[j + 1] = key  
n = [12, 11, 13, 5, 6]
insertion_sort(n)
print(n)