# python3
# Input: An integer (BucketCount) for the number of buckets
#        An integer (n) for the number of queries to follow
#        A list of queries (queries)
# Output: Print the result of each find and check command

# Wrap all of the query functions into a class
class QueryProcessor:
    # Set multiplier and prime number
    _multiplier = 263
    _prime = 1000000007

    # Function that creates space for the queries
    def __init__(self, BucketCount):
        self.BucketCount = BucketCount
        self.buckets = [[] for _ in range(BucketCount)]

    # Function that hashes the queries
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    # Function that adds queries
    def add(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        if string not in bucket:
            self.buckets[hashed] = [string] + bucket

    # Function that deletes queries
    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i] == string:
                bucket.pop(i)
                break

    # Function that finds queries
    def find(self, string):
        hashed = self._hash_func(string)
        if string in self.buckets[hashed]:
            return "yes"
        return "no"

    # Function that checks queries
    def check(self, i):
        return self.buckets[i]

# Function that decides which query function to call
def process_queries(queries):
    for query in queries:
        command, arg = query.split()
        if command == "add":
            qp.add(arg)
        elif command == "del":
            qp.delete(arg)
        elif command == "find":
            print(qp.find(arg))
        elif command == "check":
            arg = int(arg)
            print(" ".join(qp.check(arg)))

if __name__ == "__main__":
    BucketCount = int(input())
    n = int(input())

    qp = QueryProcessor(BucketCount)
    queries = [input() for i in range(n)]
    process_queries(queries)