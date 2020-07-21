from random import randint
import matplotlib.pyplot as plt
import math


import sys
sys.setrecursionlimit(10000)
# create random array of length 'length'
#array intergers are in range from 0 to maxint (here it is 40)
def creating_random_array(length=10, maxint=40):

        new_arr=[randint(0,maxint) for _ in range(length)]
        return new_arr

def bubble_sort_function(arr):
    swapped=True
    while swapped:
        swapped=False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swapped=True
    return arr
def insertion_sort_function(a):
    for sorted_len in range(1,len(a)):
        current_item=a[sorted_len]
        inserted_index=sorted_len

        while inserted_index>0 and current_item<a[inserted_index-1]:
            a[inserted_index]=a[inserted_index-1]
            inserted_index+=-1

            a[inserted_index]=current_item
    return a
def merge_sort_function(a,b):
    c=[]
    a_index,b_index=0,0
    while a_index<len(a) and b_index<len(b):
        if a[a_index]<b[b_index]:
            c.append(a[a_index])
            a_index+=1
        else:
            c.append(b[b_index])
            b_index+=1
    if a_index==len(a):c.extend(b[b_index:])
    else:              c.extend(a[a_index:])
    return c


def merge_sort(a):
    if len(a)<=1: return a
    lgt=int(len(a)/2)
    left,right = merge_sort(a[:lgt]),merge_sort(a[lgt:])
    return merge_sort_function(left,right)

def heap_data(a, index, heap_size):
    largest_num = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < heap_size and a[left_index] > a[largest_num]:
        largest_num = left_index

    if right_index < heap_size and a[right_index] > a[largest_num]:
        largest_num = right_index
    if largest_num != index:
        a[largest_num], a[index] = a[index], a[largest_num]
        heap_data(a, largest_num, heap_size)
def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heap_data(a, i, n)
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        heap_data(a, 0, i)
    return a
'''user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]'''
'''heap_sort(a)
print(a)'''
#quick sort 3 median method
def swap(arr, low, high):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp


def medianofthree(arr, low, high):
    mid = math.floor((low + high) / 2)

    if int(arr[high]) < int(arr[low]):
        swap(arr, low, high)

    if int(arr[mid]) < int(arr[high]):
        swap(arr, mid, high)

    if int(arr[mid]) < int(arr[low]):
        swap(arr, mid, low)

    pivot = arr[high]
    i = low  # index of smaller element

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if int(arr[j]) < int(pivot):
            arr[i], arr[j] = arr[j], arr[i]
            # increment index of smaller element
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i]

    return i


def quicksort(arr, low, high):
    if low >= high:
       # print(arr[low])
        return
    p = medianofthree(arr, low, high)
    quicksort(arr, low, p - 1)
    quicksort(arr, p + 1, high)
    #print(arr)





# def is_sorted(arr):
#     sorted_arr=sorted(arr)
#     return arr==sorted_arr
#performance of bubble sort
def benchmark(n=[10,100,1000,10000]):
    from time import time
    bubble_sort_time=[]  # bubble sort times
    insertion_sort_time=[]
    merge_sort_time=[]
    heap_sort_time = []
    quick_sort_time=[]

    for length in n:
        a= creating_random_array(length,length)
        t0=time()
        insertion_sort_function(a)#sorting with insertion sort
        t1=time()
        insertion_sort_time.append(t1-t0)

        a=creating_random_array(length,length)
        t0 = time()
        bubble_sort_function(a)#sorting with bubble sort
        t1 = time()
        bubble_sort_time.append(t1-t0)#recording time

        a = creating_random_array(length, length)
        t0 = time()
        merge_sort(a)  # sorting with bubble sort
        t1 = time()
        merge_sort_time.append(t1 - t0)  # recording time

        a = creating_random_array(length, length)
        t0 = time()
        heap_sort(a)  # sorting with insertion sort
        t1 = time()
        heap_sort_time.append(t1 - t0)

        a = creating_random_array(length, length)
        t0 = time()
        quicksort(a, 0 ,(len(a) - 1))  # sorting with insertion sort
        t1 = time()
        quick_sort_time.append(t1 - t0)



    plt.xlabel("Time")
    plt.ylabel("Array Size")
    plt.title("Array Size vs Time")
    plt.plot(bubble_sort_time, n, label="Bubble Sort")
    plt.plot(insertion_sort_time, n, label="Insertion Sort")
    plt.plot(merge_sort_time, n, label="Merge Sort")
    plt.plot(heap_sort_time, n, label="Heap Sort")
    plt.plot(quick_sort_time, n, label="Quick Sort")
    plt.legend()
    plt.show()

    '''print ("n \t\tInsertion sort\t\t Bubble Sort\t\t Merge Sort\t\tHeap Sort\t\tQuick Sort")
    print ("_________________________")
    for i,length in enumerate(n):
        print ("%d\t\t%0.5f\t\t%0.5f\t\t%0.5f\t\t%0.5f\t\t%0.5f"% (length,insertion_sort_time[i],bubble_sort_time[i],merge_sort_time[i],heap_sort_time[i],quick_sort_time[i]))'''


'''def benchmark2(n):
    bubble_sort_time = []
    merge_sort_time = []
    insertion_sort_time = []
    heap_sort_time = []
    x_axis = []
    for i in range(1, n+1):
        btime = i * (math.log2(i)) * 0.000000000000001
        mtime = i * (math.log2(i)) * 0.000000000000001
        htime = i * (math.log2(i)) * 0.000000000000001
        itime = (i * i) * 0.000000000000001
        x_axis.append(i)
        bubble_sort_time.append(btime)
        merge_sort_time.append(mtime)
        insertion_sort_time.append(itime)
        heap_sort_time.append(htime)

    plt.xlabel("Time")
    plt.ylabel("Array Size")
    plt.title("Array Size vs Time")
    plt.plot(bubble_sort_time, x_axis, label="Bubble Sort")
    plt.plot(insertion_sort_time, x_axis, label="Insertion Sort")
    plt.plot(merge_sort_time, x_axis, label="Merge Sort")
    plt.plot(heap_sort_time, x_axis, label="Heap Sort")
    plt.legend()
    plt.show()'''

if __name__=='__main__':
    a= creating_random_array()
    print("unsorted array=" ,a)
    del a[:]
    a = creating_random_array()
    a=bubble_sort_function(a)
    print("sorted array using bubble sort:",a)
    del a[:]
    a = creating_random_array()
    s=insertion_sort_function(a)
    print("sorted array using insertion sort:",s)
    del a[:]
    a = creating_random_array()
    t=merge_sort(a)
    print("Sorted array using merge Sort:",t)
    del a[:]
    a = creating_random_array()
    d=heap_sort(a)
    print("sorted array using heap sort:",d)
    del a[:]
    a = creating_random_array()
    quicksort(a,0,len(a)-1)
    print("Sorted array using Quick Sort",a)






'''n = []
for i in range(10, 1001):
     n.append(i)'''

# print(is_sorted(a))
benchmark()
# benchmark2(100000)




