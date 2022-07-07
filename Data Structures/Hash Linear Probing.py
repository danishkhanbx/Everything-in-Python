class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:  # if the array index is empty
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]  # Let element = current probing index
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:  # if the hash index is empty, so insert the pair
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):  # it will return the order in which we shall search
        return [*range(index, len(self.arr))] + [*range(0, index)]  # *(5, 10) + *(0, 5) = 5,6,7,8,9,0,1,2,3,4

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:  # if the probing index is empty, we have found an empty slot
                return prob_index
            if self.arr[prob_index][0] == key:  # arr[index][key], if the index already contains some values, update it
                return prob_index
        raise Exception("Hashmap full")  # when cannot find a slot empty or with same key

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return  # item not found so return, can also throw an exception
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None  # emptying the array index
        print(self.arr)


if __name__ == '__main__':
    T = HashTable()
    T["march 6"] = 310
    T["march 7"] = 420
    T["march 8"] = 67
    T["march 17"] = 63457
    T["march 17"] = 29
    T["nov 1"] = 1
    T["march 33"] = 234
    del T["nov 1"]
    print(T.arr)
    print(T["march 33"])
