# add two numbers


# l1 = 2->4->3
# l2 = 5->6->4

# 342 + 465 = 807
# output = 7->0->8


from coding_interview.utils import LinkedList, ListNode


l1 = LinkedList()
l1.inserts([2, 4, 3])
l1.print()

l2 = LinkedList()
l2.inserts([5, 6, 4])
l2.print()

l1_list = []
l2_list = []

cur = l1.head
while cur:
    l1_list.append(cur.val)
    print(l1_list)
    cur = cur.next


cur = l2.head
while cur:
    l2_list.append(cur.val)
    # print(l2_list)
    cur = cur.next

print(pow(10, 0))
print(pow(10, 1))
print(pow(10, 2))
l1_value = 0
l2_value = 0

for i, v in enumerate(l1_list):
    print(i, v)
    print(pow(10, i) * v)
    l1_value += pow(10, i) * v

for i, v in enumerate(l2_list):
    print(i, v)
    print(pow(10, i) * v)
    l2_value += pow(10, i) * v

print(l1_value)
print(l2_value)

# print('result: ', l1_value + l2_value)

result = l1_value + l2_value
print('result:', result)

print('hello', [i for i in str(result)])

list_ = [i for i in str(result)]

node = ListNode(int(list_[-1]))
cur = node
for i in range(0, len(list_)-1):
    new_node = ListNode(list_[-1-1-i])

    cur.next = new_node
    cur = new_node

node.print_all()
