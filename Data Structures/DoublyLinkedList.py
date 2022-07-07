class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

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
        if self.head is None:
            node = Node(None, data, self.head)
            self.head = node  # Head pointer points to node now
        else:
            node = Node(None, data, self.head)  # if nodes already there, so we point the new node to Head node
            self.head.prev = node  # making the prev of Head point to the New node. |Prev|New|Next|<--|Prev|Head|Next|
            self.head = node  # making New node = Head node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:  # at i-1 we stop
                node = Node(itr, data, itr.next)  # Prev = i-1| Data | Next = i-1.next = i+1
                if node.next:  # if nodes next exists
                    node.next.prev = node  # | Prev | NEW | Next |<---| Prev = i+1 | Data | Next|
                itr.next = node  # if nodes iterator
                break

            itr = itr.next
            count += 1

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(itr, data, None)  # |Prev|Last|Next|--->| Prev = last | New last| Next = None|

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next  # Head will now point on index 1
            self.head.prev = None  # |Prev=None|Head|Next=i+1| and | Prev=None | New Head | Next=i+2 |
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:  # at index i were new node to be removed
                itr.prev.next = itr.next  # |Prev| i-1 |Next=i+1| & |Prev=i-1| i |Next=i+1| --> |i| i+1 |Next|
                if itr.next:  # if i.Next exists
                    itr.next.prev = itr.prev  # |Prev| i-1 |Next=i+1| --> |Prev=i-1| i+1 |Next|
                break

            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
