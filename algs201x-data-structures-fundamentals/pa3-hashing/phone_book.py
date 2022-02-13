# python3
# Input: An integer(n) for the number of queries
#        A list (queries) that contains all of the queries
# Output: Print the result of each "Find" query (name to the phone number or "not found")

# Wrap all of the query functions into a class
class PhoneBook:

    # Function that initializes the phonebook
    def __init__(self):
        self.book = [None] * 10000000

    # Function that adds to the phonebook
    def add(self, number, name):
        self.book[number] = name

    # Function that deletes from the phonebook
    def delete(self, number):
        if self.book[number] is not None:
            self.book[number] = None

    # Function that finds entries in the phonebook
    def find(self, number):
        if self.book[number] is None:
            return "not found"
        return self.book[number]

# Function that loops through the queries and decides which query function to call
def process_queries(queries):
    for query in queries:
        q = query.split()
        cmd = q[0]
        number = int(q[1])
        if cmd == "add":
            phonebook.add(number, q[2])
        elif cmd == "find":
            print(phonebook.find(number))
        elif cmd == "del":
            phonebook.delete(number)

if __name__ == "__main__":
    phonebook = PhoneBook()

    n = int(input())
    queries = [input() for i in range(n)]
    process_queries(queries)
