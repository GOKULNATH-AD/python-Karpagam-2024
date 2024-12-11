class C1:
    
class C2(C1):
    a = 2342
class C3(C1):
    a = 123
    
class C4(C2,C3):
    a = 203

obj = C4()
# print(obj.val)