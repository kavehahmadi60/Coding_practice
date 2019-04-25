""" 
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.
Example 1:
Input: [1,3,null,null,2]
   1
  /
 3
  \
   2
Output: [3,1,null,null,2]
   3
  /
 1
  \
   2

Example 2:
Input: [3,1,4,null,null,2]
  3
 / \
1   4
   /
  2
Output: [2,1,4,null,null,3]
  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution? 
"""

import numpy as np

class Solution:
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        lower = np.empty(len(root))
        lower.fill(-np.inf)
        lower_ind = np.empty(len(root), dtype = np.int)
        upper = np.empty(len(root))
        upper.fill(np.inf)
        upper_ind = np.empty(len(root), dtype = np.int)
        
        for i in range(len(root)):
            if root[i] != None:
                if root[i]>upper[i]:
                    root[i], root[upper_ind[i]] = root[upper_ind[i]], root[i]
                elif root[i]<lower[i]:
                    root[i], root[lower_ind[i]] = root[lower_ind[i]], root[i]
                else:
                    if 2*i+1 < len(root):
                        upper[2*i+1] = root[i]
                        upper_ind [2*i+1] = i
                        lower[2*i+1] = lower[i]
                        lower_ind [2*i+1] = lower_ind [i]
                    if 2*i+2 < len(root):
                        upper[2*i+2] = upper[i]
                        upper_ind[2*i+2] = upper_ind[i]
                        lower[2*i+2] = root[i]
                        lower_ind[2*i+2] = i

if __name__ == "__main__":

    s = Solution()
    root = [3,1,4,None,None,2]
    #root = [12,2,15, None, 5, 8, 16, None, None, 3]
    s.recoverTree(root)
    print(root)


                
            
        