#merupakan algoritma yang digunakan untu untuk menghitugn prefix sum dari sebuah array

"""
Prefix sum adalah metode untuk melakukan komputasai
secarar efisien untuk menghitung jumlah dari elemen - elemen yang ada di array
permasalahan ini biasanya digunakan untuk permasalahan yang membutuhkan
perhitungan subarray atau sublist day sebuah arrray

#prefix[i] = prefix[i-1] + array[i] #this is the prefix of that something array

#contoh menghitung jumlah array dari index a sampai index b dengan asumsi bahwa a < b
#sumup_to_b = prefix[b] - prefix[a-1] #this is the sum of the array from index a to index b

#we can actually use this method to calcualte a lot of things 
#in a subarray
"""

"""
-------------------------------------
PREFIX SUM ALGORITHM
------------------------------------
"""

#calculate the prefix
def calculate_prefix_sum(array: list[int]) -> list[int]:
    #initilize the prefix sum array
    prefix_sum = [0] * len(array)
    prefix_sum[0] = array[0]
    for i in range(1, len(array)):
        prefix_sum[i] = prefix_sum[i-1] + array[i]
    return prefix_sum

#to calculate subarray sum fro index a to index b
#first check if a is 0 or not because if a is 0 then we can just return prefix[b]
#assumption is a < b
def calculate_subarray_sum(prefix_sum:list[int], a:int, b:int)->int:
    #right now we need to calcualt the subarray sum from a to b
    #assume that a < b
    if a < b:
        if a == 0:
            return prefix_sum[b]
        else:
            return prefix_sum[b] - prefix_sum[a - 1]
    else:
        raise ValueError("Masukkan nilai yang valid")

#now we can test this crap

array_a = [10, 32, 3, 54, 65, 12, 54, 9, 10, 11, 12, 23, 43, 490, 3, 23]
print(array_a)
#calculate the prefix sum of that array
prefix_sum = calculate_prefix_sum(array_a)

#and now we can check the sum from a to b
a = 0
b = len(array_a) -3
print(f"panjang array adalah {len(array_a) - 1 }")
print(f"sum of array from index {a} to index {b} is {calculate_subarray_sum(prefix_sum, a, b)}")