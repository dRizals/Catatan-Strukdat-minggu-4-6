#linkedlist
#adalah suatu struktur data linier,
#namun dibentuk secara dinamik.
#elemen dalam linkedlist disebut Node
#dalam sebuah Node berisi sebuah data dan pointer/arah
#menambah Node = menambah data dan pointer/arah
#Node pertama disebut head
class Node:
    def __init__(self, init_data):  #constructor
        self.data=init_data
        self.next=None
        
    def getData(self):  #mengetahui isi/data dari Node
        return self.data
    
    def getNext(self):  #mengetahui pointer/arah dari Node
        return self.next
    
    def setData(self, newdata): #mengatur/mengubah data 
        self.data=newdata
                                                             
    def setNext(self, new_next):  #mengatur/mengubah pointer/arah  
        self.next=new_next

a=Node(93)  #menambah data Node
b=Node(20)
print(b.getData())
print(a.getNext())

a.setNext(b)
print(a.getNext())

print(a.getData())
print(a.getNext().getData())

class LinkedList:
    def __init__(self):
        self.head=None  #constructor head
        
    def isEmpety(self):
        return self.head==None  #mengecek Node kosong/tidak
    
    def add(self, item):
        temp=Node(item)
        temp.setNext(self.head) #menambah Node(head)
        self.head=temp
        
    def size(self):
        current=self.head   #mengetahui jumlah Node
        count=0
        while current!= None:
            count=count+1
            current=current.getNext()
        return count
    
    def cari(self, item):   #mengetahui Node ada/tidak dalam barisan
        current=self.head
        while current!= None:
            if current.getData()==item:
                found=True
            current=current.getNext()
        return found
    
    def search(self, item): #mengetahui letak/posisi Node
        current = self.head
        found = False
        hit = 0
        while current != None and not found:
            hit+=1
            if current.getData() == item:
                found = True
                print ("Node Position : ", hit)
            else:
                current = current.getNext()
        
        return found
    
mylist=LinkedList()

mylist.add(32)
print(mylist.head)

mylist.add(45)
print(mylist.head)  #setiap Node baru yg masuk akan menjadi head
print(mylist.head.data)

mylist.add(70)
print(mylist.size())
print()
print (mylist.cari(45)) 
print()
print(mylist.search(45))



