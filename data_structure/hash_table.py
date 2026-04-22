"""
Important stuff about hash_tables and hash_maps
dia bekerja dengan cara melakukan hash pada input yang ada, kemudian 
dari hash tersebut akan ada sebuah index --> dari index tersbeut lalu
akan dimasukkan nilainya

#berikut time complexity dari operation yang ada di hash tables
first we neecd to check for sets
get : *O(1)
put : *O(1)
delete: *O(1)


"""

#implement hash table basic implementation of a hash tbales
class Pair:
    """Key-value Pair"""
    def __init__(self, key:int, value:str):
        self.key = key
        self.value = value

class ArrayHashMap:
    """Implementasi Hashmap dengan menggunakan struktur data array"""
    def __init__(self):
        self.buckets: list[Pair | None]  = [None] * 100

    def hash_function(self, key):
        """merupakan hash function yang akan digunakan untuk mendapatkan key"""
        index = key % 100
        return index
    
    def get(self, key):
        """diberikan suatu key, tentukan index dan return valuenya"""
        index_hash = self.hash_function(key)
        #and then we check at that index, if there's exist
        pair: Pair = self.buckets[index_hash]
        #kemudian mengecek apaah pada index tersebut terdapat data
        #atau tidak, jika ada maka ambil valuenya
        if pair is None:
            return None
        
        #return pair 
        return pair
    
    def put(self, key, value):
        """update the data at the specific index"""
        pair = Pair(key, value)
        index = self.hash_function(key)
        self.buckets[index] = pair

    def delete(self, key):
        """delete the data at that specific key"""
        #we need to access or get the index
        index = self.hash_function(key)
        #we get the index and then after that we can access the pair
        self.buckets[index] = None

    def get_all_items(self) -> list[Pair]:
        #we need to get all the key value pairs of this stuff
        result = []
        #first we need to access the index based on that key, and then return it
        for pair in self.buckets:
            if pair is not None:
                result.append(pair)
        return result
    
    def get_all_value(self) -> list[int]:
        #get all the values based on the key
        value_result = []
        for pair in self.buckets:
            if pair is not None:
                value_result.append(pair.value)
        return value_result
    
    def get_all_keys(self) -> list[str]:
        #get all the keys on the dictionary
        key_results = []
        for pair in self.buckets:
            if pair is not None:
                key_results.append(pair.key)
        return key_results


def main():
    #mengtes open addressing
    test_hashmap = ArrayHashMap()
    test_hashmap.put(1,"hallo")
    test_hashmap.put(2,"selamat pagi semuanya")
    test_hashmap.put(3, "hallo ges, selamat sinag all")

    #test hashmap
    welcome = test_hashmap.get(3)
    print(welcome.key, welcome.value)

    print("-------------------------------------------")

    #testing hash tables
    #for clarification, hash tables doesnt raelly explicityly says the number
    #of indexes it have
    hash_maps = {}
    hash_maps[100] = "oi"
    hash_maps[200] = "halo"
    hash_maps[300] = "pagi"
    hash_maps[400] = "malam"
    hash_maps[500] = "apa kabar"

    #loop over the keys
    print(f"\nprint hash maps keys")
    for i in hash_maps.keys():
        print(i)

    #loop over the values
    print(f"\nprint hash maps values")
    for j in hash_maps.values():
        print(j)

    #and then we can loop over the ky value pairs
    print(f"\nprint the key value paris of a hashpas")
    for i, j in hash_maps.items():
        print(i,j)

if __name__ == "__main__":
    main()