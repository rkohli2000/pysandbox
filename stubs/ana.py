

def readwords(fname):
    word = open('words','r')
    wordclean = [word.strip().lower() for word in open('words', 'r')]
    print(wordclean[:10])
    wordunique = list(set(wordclean))
    wordunique.sort()
    print(wordunique[:10])








def isAnagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()
    return (str1_list == str2_list)


if __name__ == "__main__":
    readwords("words")

    ret = isAnagram("Elvis", "lives")
    print("elvis/lives are anagrams" if (ret == True) else "elvis/lives are not anagrams")

