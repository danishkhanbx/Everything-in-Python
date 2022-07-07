class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)  # converting the words into ASCII values
        return hash % self.MAX

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # the key will generate hash value(index) where value will be stored
        self.arr[h] = value

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    T = HashTable()
    T['march 6'] = 310
    T['march 7'] = 420
    print(T.arr)
