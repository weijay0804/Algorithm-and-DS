"""

    Search Algorithm


"""

def linear_search(array : list, n : int) -> int:

    for i in range(0, len(array)):
        if array[i] == n:
            return i
    
    return -1


def binary_search(array : list, num : int) -> int:

    import math
    min = 0              # array 的頭
    max = len(array) - 1 # array 的尾

    while min <= max:
        middle = math.floor((max + min) / 2)    # array 的中間

        # 如果 num 在 array 的右邊
        if array[middle] < num:
            min = middle + 1    # min 變成 array 中間的下一個
        
        # 如果 num 在 array 的左邊
        elif array[middle] > num:
            max = middle - 1    # max 變成 array 中間的前一個

        #如果 middle的位置就是 num，回傳 middle
        elif array[middle] == num:
            return middle

    # 如果都沒有找到
    return -1 
