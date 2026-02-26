 #                                                                      LEETCODE PRACTICE 

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

