# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("Error: get index  out of  range!")
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("error:  'erase' index out  of  range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list.append(4)
my_list.append(5)


my_list.erase(1)
my_list.display()

print(my_list.length())
print("element at 2nd index:%d" % my_list.get(2))

print('whoopty')
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# hello = 'tim'
#
# world = hello
# print(hello, world)
#
# boogie = input('Name: ')
#
# print("Hello " +  boogie)
#
#
# age = input('Age: ')
# print('Hello',  boogie,  'you are',  age,  'years  old')
#
# x =  9
# y =  3.5
# result   = x % y
# print(result)
#
# num = input('Number: ')
# print(int(num) - 5)




def EvenNum(num):
    print(num)
    if num == 2:
        print(num)
    else:
        EvenNum(num-2)
EvenNum(8)