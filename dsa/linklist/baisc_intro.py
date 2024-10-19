l = [5, 7, 9, 9, 6, 1, 7]
# stored in onr part

link_list = ["data/value", "refrence to another node"]

# how to create singly link list


class node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


n1 = node(5)  # giving value to node
n2 = node(10)
n3 = node(15)

# assigning the next/addres
n1.next = n2
n2.next = n3

print(n1.next)
print(n2)
print(n1.next.next)
print(n3)
print(n1.next.next.next)
