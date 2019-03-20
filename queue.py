#Queue
#adalah sebuah list yang menggunakan konsep queue(FIFO) yaitu data masuk pertama keluar pertama
#kita bisa menambah data dari ujung belakang(rear) dan menghapus data dari ujung depan(front)

def createqueue():
    q=[]            #membuat queue baru
    return(q)

def enqueue(q, data):
    q.insert(0, data)       #menambah data pada rear
    return(q)

def dequeue(q):
    data=q.pop()        #henghapus data pada front(mengembalikan nilai data yg dihapus)
    return(data)

def isEmpety(q):
    return(q==[])   #mengecek apakah queue kosong(return True/False)

def size(q):
    return (len(q)) #mengetahui ukuran queue

qu = []
enqueue(qu, 'aku')          #menambah data from front
enqueue(qu, 'kamu')
enqueue(qu, 'dia')
print(qu)
print(size(qu))             #mengetahui size
dequeue(qu)                  #menghapus data dari front
print(qu)
