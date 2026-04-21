#merupakan algoritma binary search yang akan saya gunakan untuk ini

"""
Algorithma Binary search merupakan algoritma yang sangat cocok digunakan untuk
mencari elemen dari sebuah array, input nya adalah list dan target, maka
returnn nya adalah berupa index dari target yang kita inginkan

time complexity: O(log n)
space complexity: depends
"""
"""
-------------------------------------
BINARY SEARCH ALGORITHM
------------------------------------
"""

def binary_search(array: list[int], target:int) -> int:
    """
    Merupakakn algoritma yang berfungsi untuk melakukan search dengan ON time
    assumsi binary search adalah
    1. Array sudah terurut (sorted array)
    """
    left = 0
    right = len(array) - 1 
    #now as long as left is less or equal than right because
    # we need the = apabila telah mencapai nilai left == right
    while left <= right:
        #calcualte the midlle point
        middle = (right + left) // 2
        #now we need to check if the middle point is the target or not
        if array[middle] == target:
            return middle
        #if the middle point is less than the target then we only need to run on right side of the target
        elif array[middle] < target:
            left = middle + 1
        #if the middle point is greater than the target then we need only seacrh the left side
        else:
            right = middle - 1
        #if we exit the loop and we haven't found the target then we can return -1

    return -1



def main():
    #test random sorted array
    array = [1, 2, 3, 5, 6,7, 8, 9, 10, 11, 42, 43, 66, 83, 44, 435, 58, 12, 32, 43, 21210, 453,55]
    array_new = sorted(array)

    target = 55
    index = binary_search(array_new, target)
    print(f"panjang array {len(array_new)}")
    print(f"index nya adalah sebagai berikut {index}")

if __name__ == "__main__":
    main()

