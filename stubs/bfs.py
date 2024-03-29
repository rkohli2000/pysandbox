"""
BFS: Given a Node class that has a name and an array of optional childern
nodes, implement a BFS seatch method on the Node class which takes an empty
array, traverses the tree using BFS and stores the node names in the input
array and returns it.

      A
     /|\
    B C D
   /\   /\
  E  F G  H
    /\ \
   I J  K

Sample output = [A, B, C, D, E, F, G, H, I, J, K]

"""

#import program
import unittest

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            array.append(current.name)
            for child in current.children:
                queue.append(child)
        return array





test1 = Node("A")
test1.addChild("B").addChild("C")
test1.children[0].addChild("D")

test2 = Node("A")
test2.addChild("B").addChild("C").addChild("D").addChild("E")
test2.children[1].addChild("F")

test3 = Node("A")
test3.addChild("B")
test3.children[0].addChild("C")
test3.children[0].children[0].addChild("D").addChild("E")
test3.children[0].children[0].children[0].addChild("F")

test4 = Node("A")
test4.addChild("B").addChild("C").addChild("D")
test4.children[0].addChild("E").addChild("F")
test4.children[2].addChild("G").addChild("H")
test4.children[0].children[1].addChild("I").addChild("J")
test4.children[2].children[0].addChild("K")

test5 = Node("A")
test5.addChild("B").addChild("C").addChild("D").addChild("L").addChild("M")
test5.children[0].addChild("E").addChild("F").addChild("O")
test5.children[1].addChild("P")
test5.children[2].addChild("G").addChild("H")
test5.children[0].children[0].addChild("Q").addChild("R")
test5.children[0].children[1].addChild("I").addChild("J")
test5.children[2].children[0].addChild("K")
test5.children[4].addChild("S").addChild("T").addChild("U").addChild("V")
test5.children[4].children[0].addChild("W").addChild("X")
test5.children[4].children[0].children[1].addChild("Y").addChild("Z")


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(test1.breadthFirstSearch([]), ["A", "B", "C", "D"])

	def test_case_2(self):
		self.assertEqual(test2.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F"])

	def test_case_3(self):
		self.assertEqual(test3.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F"])

	def test_case_4(self):
		self.assertEqual(test4.breadthFirstSearch([]), ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])

	def test_case_5(self):
		self.assertEqual(test5.breadthFirstSearch([]), ["A", "B", "C", "D", "L", "M", "E", "F", "O", "P", "G", "H", "S", "T", "U", "V", "Q", "R", "I", "J", "K", "W", "X", "Y", "Z"])


if __name__ == "__main__":
	unittest.main()