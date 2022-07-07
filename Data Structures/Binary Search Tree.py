class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:  # if the data already exists, BST cannot have duplicates
            return

        if data < self.data:  # if the data we are adding is less than the node
            if self.left:  # to check if the node already have the left node, if it has then call add_child on that node
                self.left.add_child(data)  # with data value, keep calling until reached leaf node
            else:  # if it doesn't that means we are at the leaf node now add the node to the left
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)  # after call the function will again check data value if conditions
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, value):
        if self.data == value:  # we were searching for the root node
            return True

        if value < self.data:
            if self.left:  # if left node exists search in the left tree then call the search function again
                return self.left.search(value)  # function will again check the whole conditions for root, left & right
            else:
                return False

        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order_traversal(self):  # first we visit subtree from least of left -> most -> root -> least of right -> most
        elements = []  # we will store the elements in the list, InOder traverse is in sorted order
        if self.left:  # we will recursively goto the least(the leftest) node then start adding them in the list only
            elements += self.left.in_order_traversal()  # after reached the last node, at the time of returning

        elements.append(self.data)  # then after adding the left it goes back to parent & add the parent node

        if self.right:  # then it only checks if there exist right node, if exists add it & go back to parent & check if
            elements += self.right.in_order_traversal()  # the parent is the right node of grandparent, if it is, add it

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    def delete(self, value):

        if value < self.data:
            if self.left:  # checking if the
                self.left = self.left.delete(value)  # after deleting assigning a new subtree
            else:
                return None
        elif value > self.data:
            if self.right:  # at the last node the else condition will return None & we will assign it to the last node
                self.right = self.right.delete(value)  # thus, the last node will become empty, python will delete it
            else:
                return None
        else:   # this condition for when value = data, data is not present, and when parent have only one node
            if self.left is None and self.right is None:  # we reached the last node & still not found the value
                return None
            elif self.left is None:  # if the left is empty, then check the right node
                return self.right
            elif self.right is None:  # the search will only continue in the left part of self, thus tree is reduced
                return self.left

            min_val = self.right.find_min()  # using the right tree min value to replace the deleted node
            self.data = min_val  # Now 2 nodes with the same value is present
            self.right = self.right.delete(min_val)  # deleting the min value node returns a new right subtree,
            # which we are copying to the tree without deleted node

            """ # using the left tree max value to replace the deleted node
            max_val = self.left.find_max()  
            self.data = min_val  
            self.right = self.left.delete(max_val)
            """
        return self

    def find_max(self):  # the maximum element will be the rightmost node in BST
        if self.right is None:  # if it is None then we have reached the rightmost node
            return self.data
        return self.right.find_max()

    def find_min(self):  # the minimum element will be the leftmost node in BST
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum


def build_tree(elements):
    print('Building tree with these elements:', elements)
    root = BinarySearchTreeNode(elements[0])  # we take 0th index element as a root node and

    for i in range(1, len(elements)):  # from 1 to len we check the add child conditions & add the rest of the elements
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search('UK'))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print("Pre order traversal gives this sorted list:", numbers_tree.pre_order_traversal())
    print("Post order traversal gives this sorted list:", numbers_tree.post_order_traversal())
    print('Sum of the tree is', numbers_tree.calculate_sum())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ", numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]
