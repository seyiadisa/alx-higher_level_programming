#!/usr/bin/python3
"""Linked list module"""


class Node:
    """A node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """

        Args:
            data (int)
            next_node (Node): pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns the private attribute data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the private attribute data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """returns the private attribute next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the private attribute next_node"""
        if type(value) is not Node and value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A singly linked list"""

    def __init__(self):
        """

        Args:
            head (Node or None): first element of the linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """insert a new list element based on its value"""
        node = Node(value)

        if self.__head == None or node.data < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            current = self.__head

            while current.next_node != None and current.next_node.data < node.data:
                current = current.next_node

            node.next_node = current.next_node
            current.next_node = node

    def __str__(self):
        """string representation of a SinglyLinkedList"""
        current = self.__head
        string = str(current.data)
        current = current.next_node

        while (current) != None:
            string += "\n" + str(current.data)
            current = current.next_node

        return string
