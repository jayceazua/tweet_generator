#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by "traversing" its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        # start the count as 1
        count = 1
        # assign the head of the linkedlist to node variable
        node = self.head
        # if node is empty
        if self.is_empty():
            # return the count to 0
            return 0
        else:
            # other wise
            # if the next node in the linkedlist is not None
            while node.next is not None:
                # increase the count by 1
                count += 1
                # move to the next node
                node = node.next
            # once complete return the total count
            return count

    def append(self, item):
        """
            Insert the given item at the tail of this linked list.
            TODO: Running time: O(???) Why and under what conditions?
            Case: what if the list is empty when this is called?
            Case: What if the list is not empty when this is called?
        """
        # TODO: Create new node to hold given item
        # create a new Node instance
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        # CASE: List is empty
        # check if it is in the node is empty
        if self.is_empty():
            # assign the new node as the head
            self.head = new_node
            # assign the new node as the tail
            self.tail = new_node
        else:
            # if this node is not empty
            # assign the current tail of the linkedlist to the None of the new node
            self.tail.next = new_node
            # assign the tail of this linkedlist as the new node
            self.tail = new_node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # create a new Node instance
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        # check if it is in the node is empty
        if self.is_empty():
            # assign the new node as the head
            self.head = new_node
            # assign the new node as the tail
            self.tail = new_node
        else:
            # if this node is not empty
            # assign the current head of the linkedlist to the None of the new node
            new_node.next = self.head
            # assign the head of this linkedlist as the new node
            self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        # Assign the head of the linkedlist to the variable node
        node = self.head
        # run the method .is_empty to see if it is empty
        if self.is_empty():
            # if it is empty return None
            return None
        else:
            # while node is not None
            while node is not None:
                # run the lambda function check if it is True or False
                if quality(node.data):
                    # if True return the node
                    return node.data
                # go to the next node
                node = node.next



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        node_found = self.find(lambda item_: item_ == item) == item
        if node_found is False:
            # TODO: Otherwise raise error to tell user that delete has failed
            # Hint: raise ValueError('Item not found: {}'.format(item))
            raise ValueError('Item not found: {}'.format(item))
        else:
            node = self.head
            previous_node = None
        # TODO: Update previous node to skip around node with matching data
            while node.data is not item:
                previous_node = node
                node = node.next
            if node is self.head:
                self.head = node.next
                # Could probably turn this into a method
                if self.length() is 0:
                    self.head = None
                    self.tail = None
                return
            if node is self.tail:
                self.tail = previous_node
                self.tail.next = None
                # Could probably turn this into a method
                if self.length() is 0:
                    self.head = None
                    self.tail = None
                return
            # This "deletes" anything between the head and tail of the linkedlist"
            previous_node.next = node.next



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['A', 'C', 'B']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))
            print('length: {}'.format(ll.length()))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
