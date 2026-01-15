def word_frequency_analyser(sentence): 

    for char in ".,!?;:":
        sentence = sentence.replace(char, "")

    words = sentence.lower().split()        # Convert to lowercase and split the sentence into words
    count = {}                              
    for char in words:  
        count[char] = count.get(char, 0) + 1       # Count occurrences of each word

    return count

def word_frequency_pretty(count):
    print(f"\n--- Word Frequency Counter ---")

    for i, (word, count) in enumerate(count.items(), 1):            # Iterates through the word counts and prints each word with its frequency, starting from index 1
        print(f'{i}. {word}: {count}')

def most_common(count):
    if not count:
        return
    most_used = max(count, key=count.get)          # Find the most frequent word
    print(f"\n--- Most commonly used word ---")
    print(f"Most commonly used word is '{most_used}' with count {count[most_used]}")        

def weird_info(sentence, count):
    total_length = len(sentence.split())                    
    unique_words = len(count)                                

    print(f"\n--- STATISTICS ---")
    print(f"Total words: {total_length}")                   
    print(f"Unique words: {unique_words}")                


sentence = input("Enter text to analyze: ")                
word_frequency_analyser(sentence)     
count = word_frequency_analyser(sentence)                 
word_frequency_pretty(count)            
most_common(count)                          
weird_info(sentence, count)              





