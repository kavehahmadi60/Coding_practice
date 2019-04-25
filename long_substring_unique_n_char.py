"""
Given a string you need to print the size of the longest possible substring that has exactly k unique characters. If there is no possible substring print -1.
Example 1:
For the string "aabacbebebe" and k = 3 the substring will be "cbebebe" with length 7.
Example 2:
For the string "aabcbcabdsbajdbaaabbmmjjababaabababbbbcccbbabcbcajjjj" and k = 3 the substring will be "ababaabababbbbcccbbabcbca" with length 25.

"""

class Solution:
    def longest_substring(self, input_str, k=2):
        """
        input_str: string, the input string
        k: int, the number of the unique characters which are alloweded in the substring
        """
        i = 0
        dict = {}
        for j in range(len(input_str)):
            dict[input_str[j]] = dict.get(input_str[j], 0) + 1
            if len(dict)>k:
                dict[input_str[i]] -=1
                if dict[input_str[i]]==0:
                    del dict[input_str[i]]
                i+=1
        return j-i+1

if __name__ == "__main__":
    s = Solution()
    #input_str = "aabacbebebe"
    input_str = "aabcbcabdsbajdbaaabbmmjjababaabababbbbcccbbabcbcajjjj"
    k = 3
    print(s.longest_substring(input_str, k))


    




 
