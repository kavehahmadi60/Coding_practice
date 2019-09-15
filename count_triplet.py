"""
You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression 
for a given common ratio r and i<j<k.
"""
import os
from collections import defaultdict
# Complete the countTriplets function below.
def countTriplets(arr, r):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    result = 0

    for i in range(len(arr)):
        pre_i = arr[i]/r
        pre_pre_i = pre_i/r
        if d2[(pre_pre_i, pre_i)]>0:
            result += d2[(pre_pre_i, pre_i)]
        if d1[pre_i]>0:
            d2[(pre_i,arr[i])] += d1[pre_i]
        d1[arr[i]] += 1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
