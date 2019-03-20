#dequeue hampir sama dengan queue,
#bedanya, dequeue bisa menambah atau menghapus data dari ujung depan maupun belakang

def createDeque():
    d=[]            #membuat dequeue baru
    return(d)

def addFront(d,data):
    d.insert(0,data)    #menambah data di ujung depan
    return(d)

def addRear(d,data):
    d.append(data)  #menambah data di ujung belakang
    return(d)

def removeRear(d):
    data=d.pop()    #menghapus data di ujung belakang
    return(data)

def removeFront(d):
    data=d.pop(0)   #menghapus data di ujung depan
    return(data)

def isEmpty(d):
    return(d==[])   #mengecek dequeue kosong/tidak

def size(d):
    return(len(d))  #mengetahui jumlah data

dq = []
print(isEmpty(dq))
addRear(dq, 'aku')
addFront(dq, 'kamu')
addFront(dq, 'dia')
print(size(dq))
print(isEmpty(dq))
addRear(dq, 'saya')
print(dq)
addFront(dq, 'dirimu')
print(dq)
print(removeRear(dq))
print(dq)
removeFront(dq)
print(dq)
