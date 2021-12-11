from sort import sort


if __name__ == '__main__':
    array = [10, 9, 8, 7, 6 ,5, 4, 3, 2 ,1 ,-1,-2,-3]
    # sort.bubble_sort(array)
    # sort.insertion_sort(array)
    sort.selection_sort(array)
    print(array)

