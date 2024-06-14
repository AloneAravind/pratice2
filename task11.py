

# 1
def longest_common_prefix(strs):
    prefix = strs[0]
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
# Example usage:
print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longest_common_prefix(["dog", "racecar", "car"]))    # Output: ""

# 2.write a function to check how many prime number in a given range get it from user.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Enter a end number: "))

print("Prime numbers up to", number, "are:")
for i in range(2, number + 1):
    if is_prime(i):
        print(i, end=" ")
 
# 3 anagram
def are_anagrams(str1, str2):
    if sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower()):
        print("it's is  anagram")
    else:
        print("it's is  not a anagram")

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
are_anagrams(string1, string2)
   
# # 4 write a function to rotate a list to the right by k
# input:l=[1,2,3,4,5]  k=3   output:[3,4,5,1,2]
a = [1,2,3,4,5]
k = 3
b = a.index(k)
d = a[b:]
n = 0
for i in d:
    a.remove(i)
    a.insert(n,i)
    n+=1
print(a)

# 5
a = 786
b = list(str(a))
b.sort(reverse=True)
c = ''.join(b)
print(c)


# 6 triplets
def three_sum(nums):
    nums.sort()
    print(nums)
    result = []
    n = len(nums)
    
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 
        
        left, right = i + 1, n - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums)) 

# 7.a=[1,2,3,4,5] b=[11,12,13,14,15]
# o/p:[(1,11),(2,12),(3,13),(4,14),(5,15)
a=[1,2,3,4,5] 
b=[11,12,13,14,15]
print(list(zip(a,b)))

# 8.i=["eat","tea","tan","ate","nat","bat"]
# o/p:[["eat","tea","ate"],["tan","nat"],["bat"]]
item=["eat","tea","tan","ate","nat","bat"]
def group_anagrams(strs):
    anagrams_dict = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    print(anagrams_dict)
    return list(anagrams_dict.values())

input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(input_list))

# 9.Write a Python program to generate a chessboard pattern
for j in range(3):
    for i in range(4):
        print('0',end='')
        print('1',end='')
    print(end = "\n")
    for k in range(4):
        print('1',end='')
        print('0',end='')
    print(end = "\n")
    
# 10.write a function to determine if a number is an armstrong number.
num = 153
list1 = list(str(num))
b = []
for i in list1:
    b.append(int(i)**int(list1[-1]))
if sum(b) == num:
    print(num , " it's is a armstrong number")
else:
    print(num, " it's is not a armstrong")

