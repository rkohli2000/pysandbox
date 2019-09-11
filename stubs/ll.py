# linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
        print('---')

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while (last_node.next):
            last_node = last_node.next

        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is null")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 0
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def reverse_list(self):
        prev_node = None
        cur_node = self.head
        while (cur_node):
            temp = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = temp

        self.head = prev_node

    def has_cycle(self, head):
        node_set = set()

        curr_node = head
        while curr_node:
            if curr_node in node_set:
                return True
            else:
                node_set.add(curr_node)
            curr_node = curr_node.next

        return False

    def has_duplicates(self, head):
        data_set = set()

        curr_node = head
        while curr_node:
            if curr_node.data in data_set:
                return True
            else:
                data_set.add(curr_node.data)
            curr_node = curr_node.next

        return False


    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def removeKthNodeFromEnd(self, head, k):
        counter = 1
        first = head
        second = head
        while counter <= k:
            second = second.next
            counter += 1
        if second is None:
            head.value = head.next.value
            head.next = head.next.next
            return
        while second.next is not None:
            second = second.next
            first = first.next
        first.next = first.next.next





if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.append("E")
    llist.append("F")
    llist.append("G")

    llist.print_list()

    llist.delete_node("B")

    llist.print_list()

    print('head value is:', llist.head.data)

    llist.reverse_list()

    llist.print_list()

    print('len : ', llist.len_recursive(llist.head))

    llist.swap_nodes("A", "C")

    llist.print_list()

    llist.append("A")
    llist.print_list()

    print('Duplicates present: %s' % (llist.has_duplicates(llist.head)))

    print("\nremove 4th node")
    llist.removeKthNodeFromEnd(llist.head, 4)

    llist.print_list()

    a = 6
    print(type(a))


