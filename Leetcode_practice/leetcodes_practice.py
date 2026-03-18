 #                                                                      LEETCODE PRACTICE 

def max_subarray(nums):
    current_sum = nums[0] #Initialise code at index 0 within the array 
    max_sum = nums[0] #Initialise code at index 0 within the array 

    for num in nums[1:]: # Moves the number 1 each time
        current_sum = max(num, current_sum + num) # the current sum is the max of the current num, current_sum + the current number
        max_sum = max(max_sum, current_sum) # Max sum is the max of the highest value identified within the array while the loop was going on each time it replaced the prior value to find the max 
    return max_sum #Returns the max_sum identified throughout the loop

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))



def three_sum(nums): #Corrected three_sum for avoiding duplicates (True Medium leetcode question)
    nums.sort()
    result = []
  

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        first_number = nums[i]
        left = i + 1
        right = len(nums) -1 
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i] , nums[left] , nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1
                left +=1
                right -=1
            elif current_sum < 0:
                left +=1
            else:
                right -=1 
    return result
def sliding_window(arr, k):
    window_sum = sum(len(arr[:k]))
    max_sum = window_sum

    for i in range(k , len(arr)):
        window_sum += arr[i] - (arr[i - k])
        max_sum = max(max_sum, window_sum)
    return max_sum
    
print(sliding_window([2, 1, 5, 1, 3, 2], 3))

def three_sum(nums):   #Uncorrected three_sum DOES NOT! avoid duplicates.
    nums.sort()
    results = []

    for i in range(len(nums)):
        first_number = nums[i]

        left = i +1
        right = len(nums) -1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                results.append([nums[i], nums[left] , nums[right]])
                left +=1 
                right -=1
            elif current_sum < 0:
                left +=1
            else:
                right -=1

    return results
print(three_sum([-1, 0, 1, 2, -1, -4]))
  
def container_volume(heights):
    left = 0  
    right = len(heights) - 1

    largest_area = 0

    while left < right:

        current_area = min(heights[left] , heights[right]) *  (right - left)
        if current_area > largest_area:
            largest_area = current_area 

        if heights[left] < heights[right]:

            left +=1 
        else:

            right -=1 
    return largest_area 


print(container_volume([1, 8, 6, 2, 5, 4, 8, 3, 7]))

def MoveZeros(nums):
    write = 0

    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write] = nums[read]
            write +=1

    for i in range(write, len(nums)):
        nums[i] = 0
    return nums 


print(MoveZeros([0,1,0,3,12]))

def valid_palindrome(s):
    cleaned = ''
    for char in s: 
        if char.isalnum():
            cleaned += char.lower()
        
    left = 0 
    right = len(cleaned) -1 

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left +=1
        right -=1

    return True
        

print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
           



def two_sum_2(nums, target):

    left = 0
    right = len(nums) -1 


    while left < right:
        current_sum = nums[left] + nums[right]


        if current_sum == target:
            print(f"Indexes {left +1} & {right +1} equal your target of {target} ")
            return [left + 1, right + 1]  

        elif current_sum < target:
            nums[left] += 1
        else:
            right -=1
        
    return current_sum



print(two_sum_2([2,7,11,15], 9))

def RemoveDuplicates(nums, val):
    write = 1

    for read in range(1, len(nums)): #Read, initialises the content within the array and reads through from the first index point (Not Zero) as it is already a single value.
        if nums[read] != nums[read-1]:  #if the num read != the previous number(same value) then add we add it to the write array 
            nums[write] = nums[read]    #Turns the number read into a write number where it is now stored.
            write += 1  #Move up the index to the next number to be stored within the array
    return write


def RemoveStringDups(s):
    result = []

    for char in s:          
        if result and result[-1] == char:      # if the result and the previous result = the same char
            result.pop()                    # we will pop it and remove it from the string
        else:
            result.append(char)            #if it is not! then we will append the character to the list
    fixed_string = ''.join(result)      #join the strings together to create the single string

print(RemoveStringDups("abbaca"))

def AllowDuplicates(nums):
    write = 2

    for read in range(2, len(nums)): #Read, initialises the content within the array and reads through from the second index point as they are already single values.
        if nums[read] != nums[write-2] :   #if the num read != 2 written numbers (same value)
           nums[write] = nums[read]     #Write in the number which is currently on the pointer read.
           write += 1  #Move up the index to the next number to be stored within the array
    return write
print(AllowDuplicates([1,1,1,2,2,3]))


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in group:
                group[sorted_word] = []
            group[sorted_word].append(word)
        return list(group.values())


def majority_element(nums):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1      #Counts each number and provides amount to number value

    majority_ceiling = len(nums) / 2       #Finds the max amount of numbers within the array (ceiling)

    for num, freq in count.items():         #For loop  finds the frequency of each number within count through the use of .items()
        if freq > majority_ceiling:
            return num

    
print(majority_element([3, 2, 3]))              # 3
print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2


nums = [2,7,11,15]
target = 9

def two_sum(nums, target):
    seen = {}                                                                     # Official Leetcode question
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]        
        seen[num] = i
    return None

print(two_sum(nums, target))
#-------------------------------------------------------------------------------------
def is_palindrome(s):
        
    cleaned = ''                                                                  # Official Leetcode question

    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    return cleaned == cleaned[::-1]
#-------------------------------------------------------------------------------------
def max_profit(prices):
    max_profit = 0
    min_price = float("inf")                                                     # Official Leetcode question

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit
#-------------------------------------------------------------------------------------
def is_anagram(word1, word2):
    count1 = {}
    count2 = {}

    for char in word1:                                                           # Official Leetcode question
        count1[char] = count1.get(char, 0) + 1

    for char in word2:
        count2[char] = count2.get(char, 0) + 1

    return count1 == count2 # returns True if both dictionaries are equal i.e. both dictionaries have the same characters counts. otherwise False is returned
#-------------------------------------------------------------------------------------
def count_words(sentence):
    words = sentence.split()
    count = {}

    for word in words:                                                           #LeetCode-Style Practice Problems
        if word in count:
            count[word] += 1                                        
        else:
            count[word] = 1

    return count
#-------------------------------------------------------------------------------------
def count_letters(word):
    counts = {}
    for char in word:                                                            #LeetCode-Style Practice Problems
        counts[char] = counts.get(char, 0) + 1
    return counts
#-------------------------------------------------------------------------------------
def contains_duplicate(nums):
    seen = set()
    for num in nums:                                                             # Official Leetcode question
        if num in seen:
            return True
        seen.add(num)
    return False
#-------------------------------------------------------------------------------------
def find_all_duplicates(nums):
    seen = set()                                                                 #LeetCode-Style Practice Problems
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        if num is not seen:
            seen.add(num)
    return list(duplicates)
#-------------------------------------------------------------------------------------
def find_duplicate(nums):
    seen = set()                                                                 #LeetCode-Style Practice Problems
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None

#-------------------------------------------------------------------------------------
def find_pair_with_sum(numbers, target):
    seen = set()                                                                 #LeetCode-Style Practice Problems
    for num in numbers:
        needed = target - num
        if needed in seen:
            return True
        seen.add(num)
    return False
#-------------------------------------------------------------------------------------
def find_sum_pairs(numbers, target):
    seen = set()
    pairs = set()                                                               #LeetCode-Style Practice Problems

    for num in numbers:
        required = target - num
        if required in seen:
            pair = tuple(sorted((num, required)))
            pairs.add(pair)
        seen.add(num)

    return list(pairs)
#-------------------------------------------------------------------------------------
def remove_duplicates(numbers):
    seen = set()
    result = []                                                                  #LeetCode-Style Practice Problems

    for num in numbers:
        if num in seen:
            result.append(num)
        if num is not seen:
            seen.add(num)

    return seen
#-------------------------------------------------------------------------------------
def longest_word(words):
    longest = words[0]                                                           #LeetCode-Style Practice Problems
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
#-------------------------------------------------------------------------------------
def first_unique(text):
    seen = {}

    for char in text:
        if char in seen:                                                
            seen[char] += 1                                                     # Official Leetcode question
        else:
            seen[char] = 1

    for char in text:
        if seen[char] == 1:
            return char

#-------------------------------------------------------------------------------------  
def first_unique_char(s):
    seen= {}

    for i, char in enumerate(s): 
        if char in seen:                                                 
            seen[char] += 1                                     
        else:
            seen[char] = 1             

    for i, char in enumerate(s):              
        if seen[char] == 1:
            return i  

print(first_unique_char("leetcode"))  # 0
print(first_unique_char("loveleetcode"))  # 2
print(first_unique_char("aabb"))  # -1
#-------------------------------------------------------------------------------------  







