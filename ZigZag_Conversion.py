
""" 
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
______________
P   A   H   N
A P L S I I G
Y   I   R
______________

And then read line by line: "PAHNAPLSIIGYIR"

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"

Another example num of rows = 4
______________
P     I     N
A   L S   I G
Y A   H R   
P     I 
______________
convert("PAYPALISHIRING", 4) should return "PINALSIGYAHRPI"

Write the code that will take a string and make this conversion given a number of rows

Author: Kaveh Ahmadi
"""

def convert(s, numRows):
    if numRows == 1:
        return(s)            
    output = ""
    for c in range(numRows):
        i = c
        step1 = 2 * (numRows-1-i)            
        step2 = 2 * i
        while i<len(s):
            output += s[i]
            if step1>0 and step2>0 and i+step1<len(s):
                i += step1
                output += s[i]
                i += step2
            else:
                i += (step1+step2)
    return(output) 

if __name__ == "__main__":
    
    s = "PAYPALISHIRING"
    numRows = 4
    result = convert(s,numRows)
    print(result)
