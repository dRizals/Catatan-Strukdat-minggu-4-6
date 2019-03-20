#class dapat kita gambarkan sebagai sketsa suatu benda dengan label dan karakteristik suatu benda
#Kita dapat membuat tipe data baru selain tipe data defaut seperti int, String, boolean, dll
#tipe data baru tersebut bisa kita namai sesuka kita

class Bilkom: #membuat class dengan nama Bilkom(sekaligus menjadi tipe datanya)
    def __init__(self, a, b):
        self.real = a
        self.im = b
        # return data
    
    def display(self):
        print(self.real, "+", self.im)
        # temp = str(self.real) + '+' +str(self.im)
        # return temp
        
data = Bilkom(4, 6) #membuat objek dengan nama data
data.display()
print(type(data))   #mengecek tipe data bilangan komponen

#Overriding Methods
#Adalah ketika suatu class child yang turunan dari class parent.
#mempunyai beberapa method dengan nama yang sama dengan yang dipunya si parent,
#tetapi dengan implementasi yang berbeda.

class Bilkom:
    def __init__(self, a, b):   #constructor metode inisialisasi yang dipanggil
        self.real = a           #Python ketika membuat instance baru dari kelas ini
        self.im = b
        # return data
    
    def display(self):
        print(self.real, "+", self.im, "i")

    def __str__(self):
        temp = str(self.real) + '+' +str(self.im) + "i"
        return temp

    # Step 1
    def pertambahan(self, obj1, obj2):
        self.real =obj1.real + obj2.real
        self.im = obj1.im + obj2.im

    # Step 2
    def addKompleks(self, obj):
        a = self.real + obj.real
        b = self.im + obj.im
        return Bilkom(a, b)

# # Dengan sekali pemanggilan dengan menggunakan method addKompleks()
data1 = Bilkom(4,6)
data2 = Bilkom(2,5)
jumlah = data1.addKompleks(data2)
print(jumlah)
# data1.display()
# data2.display()

print("_______")

# mengoperasikan bilangan komponen dengan override 
data = Bilkom(4,6)
data1 = Bilkom(3,2)
data1.pertambahan(data, data1)
print(data1)
