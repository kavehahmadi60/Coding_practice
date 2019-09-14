"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in s.
"""
import os
from collections import defaultdict

def order_string(s):
    char_list = []
    for c in s:
        char_list.append(c)
    char_list = sorted(char_list)
    s = ''
    return(s.join(char_list))

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    d = defaultdict(int)
    result = 0
    for i in range(len(s)):
        for j in range(len(s)-i):
            new_s = s[j:j+i+1]
            #print(new_s)
            d[order_string(new_s)] += 1
    for k,v in d.items():
        #print(k)
        #print(v)
        result += int((v*(v-1))/2)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

