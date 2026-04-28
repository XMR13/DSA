"""
Stack pada python sngat mudah, dia sangat mirip seperti dyamic array, bahkan 
bisa dibiang hampir tidak banyak perubahan antara dynamci array dan imlementasi 
stacck di python (karakteristik LIFO)
"""

#implement the basic stack 
class Stack:
    def __init__(self):
        self.__stack = []

    def put(self,  values):
        self.__stack.append(values)

    def peek(self, values):
        #check if the stack is not empty first
        return self.__stack[-1]
    
    def pop(self):
        if self.__stack:
            self.__stack.pop()

        else:
            raise ValueError("stack sudah kosong dan tidak ada lagi data yang ada")
    
    def print(self):
        #print element in the stack
        print(self.__stack)



stack1 = Stack()
stack1.put(2)
stack1.put(3)
stack1.print()

tes_stack = []
tes_stack.append(10)
tes_stack.append(20)
tes_stack.append(30)


print(tes_stack)

#remove it from the latest one
tes_stack.pop()

#peek into it
tes_stack[-1] 

#and then check if it isi empty
def is_stack_empty(stack)->bool:
    if stack:
        return True
    return False

hasil_exist = is_stack_empty(tes_stack)
print(hasil_exist)