def number_analyser(numbers):
    # Initialise counters 
    total = 0
    even_counter = 0
    #Starts both min and max at the first number when looping through the user inputted list
    min_number = numbers[0]
    max_number = numbers[0]
    
    #num is each individual number added together to the total 
    for num in numbers:
        total += num

        if num > max_number:
            max_number = num
        if num < min_number:
            min_number = num
        if num % 2 == 0:
            even_counter += 1

    average = total / len(numbers) 

    return total, average, max_number, min_number, even_counter

user_input = input("Enter numbers separated by spaces: ")
# User input is .split() into a string within a list which is then converts each pieces of data to an integer through map(int()) with list making it a true list
numbers = list(map(int, user_input.split()))

result = number_analyser(numbers)
#F string collects the results from the user inputted list and gains the data through the for loop and if statement (cleaner data )
print(f'Sum: {result[0]}')
print(f'Average: {result[1]}')
print(f'Max_number: {result[2]}')
print(f'Min_number: {result[3]}')
print(f'Even Counter: {result[4]}')

