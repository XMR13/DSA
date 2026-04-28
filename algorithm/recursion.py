"""
Recursion adalah metode memanggil suatu fungsi atau elemen secara berulang - ulang
Dalam konteks pemorgraman, recursion memanggil suatu fungsi n, secara berulang hingga mencapai suatu base case tertentu.
Untuk setiap permasalahan recursion, harus memiliki:
1. Base case untuk mengmebalikan nilai agar recursion tidak berjalan terus

it works like a call stack 
"""
import time

def fibonacci(n:int) -> int:
    #this algorithm will take O(2**n) times 
    #so this algorith is an exponential algorithm

    if n == 0:
        return 0
    elif n == 1 :
        return 1
    elif n < 0:
        raise ValueError("value tidak boleh bernilai negatif")
    else:
        #check if the current_fibonacci sequence is already in the hash
        #we need to check if both of these already in the lookup
        
        return fibonacci(n-1) + fibonacci(n-2)
    
#test the time
start = time.time()

n = 10
hasil = fibonacci(40)

end = time.time()
waktu = end - start
print(f"waktu yang diperlukan untuk menhitung {n} fibonnaci number adalah {waktu:.2f} detik")
print(hasil)