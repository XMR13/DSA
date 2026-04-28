#this is one of the hardes problem i can do ain't gonna li, the

#if i nput the 

def roman_to_integer(inp:str) -> int:
    """this is the roman to integer one"""

    #first create the mapping of this crap
    roman_mapping = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100, 
        "D" : 500,
        "M" : 1000
    }

    #Now we need to get into the frist index and last index 
    #kinda like 2 pointers huh
    start = 0
    end = len(inp)
    sum = 0

    #first we need to check if the index is still less and also the current value of the the mapping is less thatn 
    while start < end:
        if start < end - 1 and roman_mapping[inp[start]] < roman_mapping[inp[start + 1]]:
            #then we just need to add the sum of it 
            sum += roman_mapping[inp[start + 1 ]] - roman_mapping[inp[start]]
            #and thwn we skip two parts 
            start += 2

        else:
            #ust add it to next sum
            sum += roman_mapping[inp[start]]
            start +=1
    
    return sum

def main():
    #just have list inputs, this the inputs of it 
    list_inputs = [
        "IXVII", "VII", "MCVIIX"
    ]

    #and then loops into the inputs
    for i in list_inputs:
        # we take the current and calculate the roman integeres
        hasil = roman_to_integer(i)
        print(f"hasil dari roman to integer dari {i} adalah {hasil}")


if __name__ == "__main__":
    main()