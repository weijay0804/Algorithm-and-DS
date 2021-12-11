"""

    各種的排序演算法

"""

def swap(array : list, i : int, j : int) -> None:
    ''' 交換 array 中的元素 '''

    temp = array[i]
    array[i] = array[j]
    array[j] = temp

def bubble_sort(array : list) -> list:
    ''' 氣泡排序 '''

    array_len = len(array)

    for i in range(0, array_len):
        flag = False    # 檢查 array 是否已經排序好

        # array 的最後一項不用排序
        for j in range(0, array_len - i - 1):
            if array[j] > array[j + 1]:
                swap(array, j, j+1)
                
                flag = True # 變更 flag 讓迴圈繼續

        if not flag:
            break
    
    return array


def insertion_sort(array : list) -> list:
    ''' 插入排序 '''

    array_len = len(array)

    # 從第 2 個元素開始比較
    for i in range(1, array_len):
        temp = array[i] # 要比較的元素
        j = i - 1   # 已經排序好右邊的 index

        # 依序對比排序好的數字
        while j >= 0:

            if array[j] > temp:
                array[j+1] = array[j]   # [4,3,2,1] if j = 0 => [4,4,3,2,1]
                j = j - 1   # 再已經排序好的 array 中往左繼續比對

            # 如果沒有代表已經排序好
            else:
                break

        array[j + 1] = temp # 將 temp 放到已經排序好的第一個
    
    return array


def selection_sort(array : list) -> list:
    ''' 選擇排序 '''

    array_len = len(array)

    for i in range(0, array_len):
        minindex = i    # 最小值的 index

        # 依序找到 array 中的最小值，並互換
        for j in range(i, array_len):   
            # 找到 array 中的最小值
            if array[j] < array[i]:
                minindex = j

        swap(array, i, minindex)
    
    return array