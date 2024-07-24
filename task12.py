# 1.Write a Python function  that takes a list of unique integers nums containing numbers from 0 to n
#  but with one missing number, and returns the missing number.
# Sample Input:nums = [3, 0, 1]  Expected Output:2
nums = [3, 0, 1]
min1 = min(nums)
max1 = max(nums)
def unique():
    for i in range(min1,max1):
        if i not in nums:
            return i
    else:
        return "There was no missing numbers"
print(unique())


# 2.Write a Python function  that implements binary search to find the index of target in a sorted list nums.
#  Return -1 if target is not found.
# Sample Input:nums = [1, 2, 3, 4, 5, 6, 7]   target = 5  Expected Output:4
nums = [1, 2, 3, 4, 5, 6, 7] 
target = 5
try:
    print(nums.index(target))
except:
    print(-1)

# 3.Write a Python function  and returns the length of their longest common subsequence
# .Sample Input:s1 = "abcdef"  s2 = "ace"   Expected Output:3
s1 = "abcdef"  
s2 = "ace"
s3 = ''
for i in s2:
    if i in s1:
        s3+=i
print(len(s3))

# 4.Write a Python function that rotates a given n x n 2D matrix matrix by 90 degrees clockwise.
# Sample Input:
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
Expected =[
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
n = len(matrix)
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

for i in range(n):
    matrix[i].reverse()
    print(matrix)



# 6.Write a Python function find_peak_element(nums) that finds a peak element in a given list nums. 
# A peak element is an element that is greater than its neighbors(before and after index elements)
# A peak element in an array nums is an element that is greater than its neighbors (if they exist). 
# .Sample Input:nums = [1, 2, 1, 3, 5, 6, 4]
# Expected Output:5

nums = [1, 10, 1, 3, 5, 6, 4]
first, last = nums[0], nums[-1]
list1 = []
for i in range(1,len(nums)-1):
    if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        list1.append(nums[i])
print(list1)

# 8.Implement a Python function that rearranges numbers into the lexicographically next greaterpermutation of numbers.
#  If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
# Sample Input:nums = [1, 2,3]
# Expected Output:[1, 3, 2]

nums = [1, 2,3]
import random
random.shuffle(nums)
print(nums)

# 9.Given an array of integers nums and an integer k, write a Python function 
#  that returns the total number of continuous subarrays whose sum equals to k.
# Sample Input:nums = [1, 1, 1],k = 2
# Expected Output:2
nums = [1, 1, 2]
k = 2
def count_subarrays(nums, k):
    count = 0
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1
    
    return count

result = count_subarrays(nums, k)
print(f"Total number of continuous subarrays with sum {k}: {result}")



# 10.Given n non-negative integers representing vertical lines on a 2D plane where the width of each bar is 1, compute the maximum area of water that can be contained between the vertical lines.
# Sample Input:height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Expected Output:49
def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate current area
        current_area = min(height[left], height[right]) * (right - left)
        # Update max_area if current_area is larger
        if current_area > max_area:
            max_area = current_area
        
        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area

# Test case
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Maximum area of water that can be contained:", max_area(height))
