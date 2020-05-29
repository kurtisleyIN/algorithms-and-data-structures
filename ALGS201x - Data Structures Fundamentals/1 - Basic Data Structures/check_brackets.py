# python3
# Input:
# Output:

from collections import namedtuple

Bracket = namedtuple('Bracket', ['char', 'position'])

def are_matching(left, right):
    return (left + right) in ['()', '[]', '{}']


def find_mismatch(text):
    opening_brackets_stack = []
    for index, character in enumerate(text, start = 1):
        
        if character in ['[', '(', '{']:
            opening_brackets_stack.append(Bracket(character, index))

        elif character in [']', ')', '}']:
            if not opening_brackets_stack:
                return index
            
            top = opening_brackets_stack.pop()
            if are_matching(top.char, character) == False:
                return index

    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position
    
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
