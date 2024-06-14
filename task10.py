# # 1
# l = [45, 72, 82, 99, 2, 77, 8]

# # Bubble Sort algorithm
# n = len(l)
# for i in range(n):
#     for j in range(0, n-i-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]

# print(l)

# # 3)l="i am python welcome" output=["I"," Am"," Python"." Welcome"] first letter will be caps
# l="i am python welcome"
# l = l.title()
# l = l.split()
# print(l)

# # 4)l="i love india India" count the number of occurance in the character
# l="i love india India" 
# dict1 = {}
# for check in l:
#     if  check in dict1:
#         dict1[check] +=1
#     else:
#         dict1[check] = 1
# print(dict1)

# # 5)l="i love india India" maximum count of the character
# l="i love india India"
# l = l.lower()
# dict1 = {"char" : 0 , 'count':0 }
# for max1 in l:
#     if l.count(max1) > dict1['count']:
#         dict1['char'] = max1 
#         dict1['count'] = l.count(max1)
# print(dict1)

# # 6)l=[1,2,3,4,5] is false and l=[1,1,1,1] is true list is occurance in same memory true otherwies false
# l = [1,1,1,1,1]
# def hello():
#     for i in l:
#         if i is not l[0]:
#             return False
#     return True
# if hello():
#     print("The list is occurance same memory ")
# else:
#     print("The list doesn't occur in same memory")

# # 7)a=12345 output will be 6 explanation is i have add the total value of the number and print single value of sum data
# a = 12345
# b = str(a)
# while  len(b)>1:
#     c = 0
#     d = list(b)
#     for i in d:
#         c += int(i)
#     b = str(c)
# print(c)

# # 8)input=[4,6,2,4,3,4,2,2] out=[(4,3),(2,3),(6,1),(3,1)]
# input=[4,6,2,4,3,4,2,2]
# dict1 = {'name':[], 'occur':[]}
# for i  in input:
#     if i not in dict1['name']:
#         dict1['name'].append(i)
#         dict1['occur'].append(input.count(i))
# b = zip(dict1['name'],dict1['occur'])
# sorted_tuples = sorted(b, key=lambda x: x[1], reverse=True)
# print(sorted_tuples)

# from collections import Counter
# input = [4, 6, 2, 4, 3, 4, 2, 2]
# counter = Counter(input)
# # print(counter)
# output = sorted(counter.items(), key=lambda x: x[1], reverse=True)
# print(output)

# # 9) check the string is whether it is palindrome or not without using slicing
# a = 'racecar'    
# a = a.replace(" ", "").lower()
# if a == "".join(reversed(a)):
#     print(a , " it is palindrome")
# else: 
#     print(a, " it is not a palindrome")

# 10)Write a function that finds the maximum sum of a contiguous subarray within an array of integers.
# Input:nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output:6
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# def max_subarray_sum(nums):
#     max_sum = float('-inf')  # Initialize max_sum to negative infinity
#     current_sum = 0  # Initialize current_sum to 0
    
#     for num in nums:
#         current_sum += num
#         max_sum = max(max_sum, current_sum)
        
#         if current_sum < 0:
#             current_sum = 0
    
#     return max_sum

# # Example usage:
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# result = max_subarray_sum(nums)
# print("Maximum sum of contiguous subarray:", result)  # Output: 6

def max_subarray_sum(nums):
    max_sum = nums[0]  # Initialize max_sum with the first element of the array
    current_sum = nums[0]  # Initialize current_sum with the first element of the array
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
  
    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print("Maximum sum of contiguous subarray:", result)  # Output: 6
print(nums[:])
print(nums)