def my_binary_search(arr,key):
    start = 0
    end = len(arr)-1
    mid=int((start+end)/2)
    
    print(start,mid,end)

    while not(arr[mid] == key):

        if arr[mid] < key:
            print("right side")
            start=mid+1
            mid = int((start+end)/2)

        elif arr[mid] > key:
            print("left side")
            end = mid-1
            mid = int((start+end)/2)

        print(start,mid,end)

    if arr[mid] == key:
        print("found at index: ",mid)

arr=[-7, -1, 2, 11, 19, 20, 24, 27, 35, 39]
key=20
my_binary_search(arr,key)