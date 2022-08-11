# 二分查找
# from distutils.log import debug


from calendar import c


def efsearch(li, low, height, key):
    if low > height:
        return -1
    mid = int((low+height)/2)
    if li[mid] == key:
        return mid
    elif li[mid] > key:
        height = mid-1
        return efsearch(li, low, height, key)
    else:
        low = mid + 1
        return efsearch(li, low, height, key)
# li = [7,9,14,15,16,19,33]
# tar = efsearch(li,0,len(li),1)
# print(tar)

# 线性查找


def linesearch(li, key):
    for i in range(0, len(li)):
        if li[i] == key:
            return i
    return -1
# li = [7,9,14,15,16,19,33]
# tar = linesearch(li,19)
# print(tar)


# 排序算法 都是从小到大排
li = [17, 33, 17, 59, 19, 14, 33, 15, 16, 19, 4]
# 快速排序 一个基准 两个数组 递归


def kssort(arr):
    if len(arr) <= 1:
        return arr
    minli = []
    maxli = []
    mid = arr[0]
    for i in range(1, len(arr)):
        if mid >= arr[i]:
            minli.append(arr[i])
        else:
            maxli.append(arr[i])
    return kssort(minli)+[mid]+kssort(maxli)
# print(kssort(li))

# 插入排序  双层循环


def crsortA(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
# print(crsortA(li))

# 插入排序 略过第一个，从第二个开始，往前进行对比，
# 从小到大排列  要保证前面的都比自己小
# 碰到比自己小的  就继续往前比
# 碰到比自己大的  就换位子   让大的那个换到自己的位置上， 相当于自己往前挪，然后自己继续往前比
# print(li)


def insterSort(arr):
    for i in range(1, len(arr)):
        curr = i
        # print('----------------------------------------------------------')
        for j in range(i-1, -1, -1):
            # print('curr=',curr,',j=',j)
            if arr[curr] < arr[j]:
                arr[curr], arr[j] = arr[j], arr[curr]
                curr = j
            # print('arr=',arr)
    return arr
# print(insterSort(li))

# 选择排序
# 先假设第一个是最小的，往后比
# 找到比自己小的就交换  用这个最小的再往后比  直到数组结束， 就找到了最小的   放在第一个
# 然后再把第二个当成最小的和后面所有的比


def pickSort(arr):
    for i in range(0, len(arr)):
        min_index = i
        # print('----------------------------------------------------------')
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # print(arr)
        arr[min_index], arr[i] = arr[i], arr[min_index]
        # print(arr)
    return arr
# print(pickSort(li))

# 冒泡排序
# 第一个和第二个比 第一个大于第二个 交换 在用第二个和第三个个比 一直比到最后一个
# 那么一轮下来 最大的 就会到最后一个 所以第二轮 就不用再和最后一个比了


def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# print(bubbleSort(li))


# 归并排序
# 1 从下往上的归并排序：将待排序的数列分成若干个长度为1的子数列
# 然后 将这些数列两两合并，得到若干个长度为2的数列 再将这些数列两两合并，
# 直到合成一个数列为止    
def merge(left,right):# 将两个已经有序的小数组 合并成一个有序的数组 
    i,j=0,0
    res= []  #要返回的数组
    while i<len(left) and j<len(right):  # 循环比较两个数组  用左边的第一个和右边的第一个对比 把较小的放到添加到res中
        if left[i]<right[j]:         #  如果左边第一个较小 把左边第一个塞进res  下一轮 拿左边第二个 和右边第一个比 
            res.append(left[i])
            i+=1                   # 左边第一个 塞进res中了 所以左边的下标要+1
        else:
            res.append(right[j])
            j+=1
    print('------------------',res,left[i:],right[j:])
    res.extend(left[i:])  # 循环结束后  左边或者右边有剩余的项 没有比较   直接加到res中
    res.extend(right[j:])
    return res

def msort(arr):  
    if len(arr)<=1:  # 如果长度为0 或者1  就直接返回 不用比较了
        return arr
    # 将数组分成两个数组  需要找到中间的
    mid=int(len(arr)/2)
    arrl=msort(arr[:mid]) # 递归排序子数组
    arrr=msort(arr[mid:])
    return merge(arrl,arrr)  # 合并
# print(li)
# print(msort(li))

# 堆排序

def heapify(arr, n, i): 
    largest = i  
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
        heapify(arr, n, largest) 
  
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        heapify(arr, i, 0) 

# heapSort(li)
# print(li)


# 单独比较 一颗小树 根节点 node 左子节点 left  右子节点right
# 待排序的列表 arr
# 待排序的数组长度 n
# 当前节点的下标i  
print(li) 
def heapSign(arr,n,i):
    left = 2*i+1
    right = 2*i+2
    lag = i
    if left < n and arr[i]<arr[left]:
        lag = left
    if right < n and arr[lag]<arr[right]:
        lag = right
    if lag != i:
        print('lagggggggggggg',i ,lag)
        arr[lag],arr[i]= arr[i],arr[lag]
        heapSign(arr,n,lag)
    print('signnnnnnnnnnnnnn',arr,n,lag)
def heaps(arr):
    if len(arr)==0:return
    c = len(arr)
    n = int(c/2) - 1 # 最后一个非叶子节点的索引
    # 这个循环是为了把整个树变成大顶堆
    for i in range(n,-1,-1):
        heapSign(arr,c,i)
    print('maxxxxxxxxxxxxx',li)   
    #  大顶堆 在下面循环直接换 根节点和最后一个叶子节点  
    #  这个时候 数组最后一位 是最大的 他的位置就固定了  所以要对比的数组长度就减一变成c-1
    #  然后再接着循环
     
     
    for i in range(c-1,0,-1):
        print('maxxxxxxxxxxxxx-',li) 
        arr[i],arr[0]=arr[0],arr[i]
        print('maxxxxxxxxxxxxx-',li) 
        print('----------------------------------------------------------') 
        heapSign(arr,i,0)
# heaps(li)
# print(li)
# def print2tree(arr):
#     c = len(arr)
#     n = int(c/2) - 1
#     print(2*n*' ',arr[0])
#     left = []
#     right =[]
#     for i in range(1,c,2):


# 计数排序

# 先找到最大的值
def getMax(arr):
    maxitem = arr[0]
    for i in range(1,len(arr)):
        if maxitem<arr[i]:
            maxitem = arr[i]
    return maxitem        
# 然后定义一个 数组 长度为最大值
def countSort(arr):
    c = getMax(arr)
    sortarr=[]
    temparr = [0 for i in range(c+1)]
    for i in arr:
        temparr[i]+=1
    for i in range(c+1):
        if temparr[i]>0:
            for j in range(temparr[i],0,-1):
                sortarr.append(i)
        continue
    return sortarr
print(countSort(li))
    
    
    
        


    
    
