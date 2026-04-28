

def is_anagram(s:str, t:str)-> bool:
    #check if this combination is an anagram or not
    #first we need to check both of them must have the same length
    if len(s) != len(t):
        return False
    
    #then we initilizaide it
    map_s = {}
    map_t = {}

    #and then we just need to index for every character and count on it
    for i in range(len(s)):
        #count it
        map_s[s[i]] = 1 + map_s.get(s[i], 0)
        map_t[t[i]] = 1 + map_t.get(t[i], 0)
    
    if map_s == map_t:
        return True

    else:
        return False

def main():
    #this where we will be providing the sring for in 
    #words = ["abba", "baba", "bbaa","cd","cd"]
    #words = ["yjonq","yqnoj","oyqjn","nqoyj","onjqy","joqyn","qynjo","jynoq"]
    words= ["a","b","a"]
    length = len(words)
    for i in range(length-1, 0, -1):
        #and then we need to check if the list are anagram
        if len(words) == 1:
            continue
        anagram = is_anagram(words[i], words[i-1])
        print(words[i])
        print(words[i-1])
        print(anagram,"\n")
        #if this is is an anagram 
        if anagram == True:
            words.pop(i)

        else:
            pass

    print(words)



if __name__ == "__main__":
    main()