class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''  # created an empty linked list string, and in this string we will append data
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)  # arrow will only be printed when next is
            itr = itr.next  # not None,
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():  # the index should be valid and not the last index (because we
            raise Exception("Invalid Index")  # already created a function for it)

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # we will iter to one index before insertion, and make i-1 index point to i
                node = Node(data, itr.next)  # now Node will point to i+1 index we copied the next value from i-1's next
                itr.next = node  # now i-1 will point to i
                break

            itr = itr.next
            count += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:  # exit when the next element doesn't exist
            itr = itr.next

        itr.next = Node(data, None)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:  # python do the garbage collection for us, we don't have to do it explicitly
            self.head = self.head.next  # the head will point to index 1 now which is the new index 0 now
            return

        count = 0  # we use count to keep check on which index we are, it will just increment with itr.next
        itr = self.head
        while itr:
            if count == index - 1:  # stopping at i-1 index
                itr.next = itr.next.next  # i-1 will now point to i+1 index
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    print('Inserting values: ')
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    print('Inserting blueberry at index 1: ')
    ll.insert_at(1, "blueberry")
    ll.print()
    print('Inserting apple in starting index: ')
    ll.insert_at_begining("apple")
    ll.print()
    print('Removing from index 2: ')
    ll.remove_at(2)
    ll.print()
    print('Inserting jackfruit at the end: ')
    ll.insert_at_end('jackfruit')
    ll.print()
