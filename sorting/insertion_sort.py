def sort(lst):
    print("Unsorted array:")
    print(lst)

    print("After sorting:")
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        print(min_index)
        lst[i], lst[min_index] = lst[min_index], lst[i]
    print(lst)



if __name__ == '__main__':
    lst = [25, 35, 45, 12, 65, 10]
    sort(lst)
