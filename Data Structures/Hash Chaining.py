class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]  # [] key value pair

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)  # converting the words into ASCII values
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for element in self.arr[arr_index]:  # after getting array index, we search all the elements in it
            if element[0] == key:  # if some elements 0 is equal to key we have found the item
                return element[1]  # value is present at 1

    def __setitem__(self, key, value):
        h = self.get_hash(key)  # the key will generate hash value(index) where value will be stored
        found = False
        for index, element in enumerate(self.arr[h]):  # using enumerate we will iterate through the array
            if len(element) == 2 and element[0] == key:  # len(element) means key-value present in that element
                # element[0] key means the key we are searching for is at 0, indicates element already present in list
                self.arr[h][index] = (key, value)  # index = index points at every element to check the if condition
                found = True
        if not found:
            self.arr[h].append((key, value))  # if the key doesn't exist in the table

    def __delitem__(self, key):
        arr_index = self.get_hash(key)  # we first locate the index in the array then find the element in that index
        for index, element in enumerate(self.arr[arr_index]):  # element = key, value i.e. ele[0] = key & ele[1]=value
            if element[0] == key:
                print('del', index)
                del self.arr[arr_index][index]


if __name__ == '__main__':
    T = HashTable()
    T["march 6"] = 310
    T["march 7"] = 420
    T["march 8"] = 67
    T["march 17"] = 63457
    print(T["march 6"])
    print(T.arr)
    T["march 6"] = 11
    print(T.arr)
    del T['march 6']

