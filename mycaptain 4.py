
class Student:
    
    def __init__(self, name, rollno, sec, m):
        self.name = name
        self.rollno = rollno
        self.sec = sec
        self.m = m
   
    def accept(self, Name, Rollno, section, marks ):
        # use  ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, section, marks)
        ls.append(ob)
  
    
    def display(self, ob):
            print("Name   : ", ob.name)
            print("RollNo : ", ob.rollno)
            print("section: ", ob.sec)
            print("Marks : ", ob.m)
            print("\n")    
         
    def search(self, rn):
        for i in range(ls.__len__()):
                 if(ls[i].rollno == rn):
                     return i       
                                
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
     
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = 1;
         

ls =[]

obj = Student('', 0, " ", 0)
  



obj.accept("A", 1, "a", 100)
obj.accept("B", 2, "b", 90)
obj.accept("C", 4, "a", 80)
         
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):    
    obj.display(ls[i])

print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
         

obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             

obj.update(4, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# else:
print("Thank You !")
