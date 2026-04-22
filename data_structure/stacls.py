"""
Stack pada python sngat mudah, dia sangat mirip seperti dyamic array, bahkan 
bisa dibiang hampir tidak banyak perubahan antara dynamci array dan imlementasi 
stacck di python (karakteristik LIFO)
"""
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