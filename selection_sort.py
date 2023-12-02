def selection_sort(lst) :
    for i in range(0, len(lst)) :
        i_position = i
        for j in range(i + 1, len(lst)) :
            if lst[j] < lst[i_position] :
                i_position = j

        lst[i], lst[i_position] = lst[i_position], lst[i]

lst = [3, 7, 6, 2, 4, 5]
selection_sort(lst)
print(lst)