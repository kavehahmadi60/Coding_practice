"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

Author: Kaveh Ahmadi
"""

class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        change = False
        for i in range(-2,-1*len(nums), -1):
            if nums[i]<nums[-1]:
                nums[i], nums[-1] = nums[-1], nums[i]
                change = True
                break
        if change == False:
            nums.sort()

if __name__ == "__main__":
    L = [2,1,3]
    S = Solution()
    S.nextPermutation(L)
    print(L)
    