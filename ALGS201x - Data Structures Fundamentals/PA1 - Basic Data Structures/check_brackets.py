# python3
# Input: A string (text)
# Output: If the string uses brackets correctly, print "Success"
#         If not, output the 1-index location of the first unmatched closing bracket
#         If no unmatched closing brackets, output the 1-index location of the first unmatched opening bracket

from collections import namedtuple

# Create a subclass of tuple with named fields
Bracket = namedtuple('Bracket', ['char', 'position'])

def are_matching(left, right):
    # Concatenates two characters to check if they are a matching pair
    return (left + right) in ['()', '[]', '{}']

def find_mismatch(text):
    
    # Initialize the opening brackets stack
    opening_brackets_stack = []
    
    # Cycle through the string with a 1-index and character pair
    for index, character in enumerate(text, start = 1):
        
        # Add opening brackets to the stack
        if character in ['[', '(', '{']:
            opening_brackets_stack.append(Bracket(character, index))

        elif character in [']', ')', '}']:
            # If the stack is empty, return the index of the closing bracket
            if opening_brackets_stack == None:
                return index
            
            # If the stack is not empty and the closing bracket doesn't match the top of the stack, return the index of the closing bracket
            top = opening_brackets_stack.pop()
            if are_matching(top.char, character) == False:
                return index
    
    # If the stack isn't empty, return the index of the top of the stack
    if opening_brackets_stack != None:
        top = opening_brackets_stack.pop()
        return top.position
    
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
