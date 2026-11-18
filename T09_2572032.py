## Waktu Mulai : 06:35
## Waktu Selesai: 06:45
## Definisi Kelas ##
## Definisi Kelas SongNode
## Nama: Khresna Mulia Putra (Khresmupu)
## NRP: 2572032

## Definisi Atribut:
# info  : atribut yang menyimpan judul lagu (string)
# next  : atribut reference elemen berikutnya (SongNode)
class SongNode:
    ## Definisi Konstruktor
    # Kamus Lokal
    # info : var yang menyimpan judul lagu (string)
    def __init__(self, info):
        self.info = info
        self.next = None

## Definisi Kelas PList
## Definisi Atribut:
# head  : atribut yang menyimpan elemen pertama dari list (SongNode)
class PList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    ## Definisi Method traversal()
    # Kamus Lokal
    # p : iterator node (SongNode)
    def traversal(self):
        if self.isEmpty():
            print("List Kosong")
        else:
            p = self.head
            while p.next != self.head:
                print(p.info, end=" ")
                p = p.next
            print(p.info)

    ## Definisi Method insertFirst(p)
    # Kamus Lokal
    # p    : node yang akan ditambahkan (SongNode)
    # last : penanda node terakhir (SongNode)
    def insertFirst(self, p):
        if self.isEmpty():
            p.next = p
            self.head = p
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = p
            p.next = self.head
            self.head = p

    ## Definisi Method insertLast(p)
    # Kamus Lokal
    # p    : node yang akan ditambahkan (SongNode)
    # last : penanda node terakhir (SongNode)
    def insertLast(self, p):
        if self.isEmpty():
            p.next = p
            self.head = p
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            last.next = p
            p.next = self.head

    ## Definisi Method insertAfter(search_value, p)
    # Kamus Lokal
    # curr         : iterator pencarian node (SongNode)
    # search_value : judul lagu yang dicari (string)
    # p            : node baru yang akan disisipkan (SongNode)
    def insertAfter(self, search_value, p):
        if self.isEmpty():
            return False
        curr = self.head
        while True:
            if curr.info == search_value:
                p.next = curr.next
                curr.next = p
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    ## Definisi Method removeFirst()
    # Kamus Lokal
    # q    : node terbuang (SongNode)
    # last : node terakhir (SongNode)
    def removeFirst(self):
        if self.isEmpty():
            return None
        q = self.head
        if self.head.next == self.head:
            q.next = None
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next
            self.head = self.head.next
            last.next = self.head
            q.next = None
        return q

    ## Definisi Method removeLast()
    # Kamus Lokal
    # q    : node terbuang (SongNode)
    # prev : node sebelum terakhir (SongNode)
    # curr : node terakhir (SongNode)
    def removeLast(self):
        if self.isEmpty():
            return None
        q = self.head
        if self.head.next == self.head:
            q.next = None
            self.head = None
        else:
            prev = None
            curr = self.head
            while curr.next != self.head:
                prev = curr
                curr = curr.next
            q = curr
            prev.next = self.head
            q.next = None
        return q

    ## Definisi Method showInfos(search_value)
    # Kamus Lokal
    # prev         : node sebelum curr (SongNode)
    # curr         : node yang sedang diperiksa (SongNode)
    # search_value : judul lagu yang dicari (string)
    def showInfos(self, search_value):
        if self.isEmpty():
            return None
        prev = self.head
        while prev.next != self.head:
            prev = prev.next  
        curr = self.head
        while True:
            if curr.info == search_value:
                res = ""
                if curr != self.head:
                    res += f"{prev.info} -> "
                res += f"{curr.info}"
                if curr.next != prev and curr.next != curr:
                    res += f" -> {curr.next.info}"
                return res
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        return None

def printMenu():
    print("menu:")
    print("1. insert first")
    print("2. insert last")
    print("3. delete first")
    print("4. delete last")
    print("5. mencari lagu dan menampilkan previous dan nextnya")
    print("6. insert after")
    print("0. keluar")

# Kamus Data (Main Program):
# p          : objek playlist sirkuler (PList)
# pilih      : pilihan menu dari pengguna (integer)
# lagu       : judul lagu input (string)
# cari       : judul lagu yang dicari (string)
# nodeBaru   : objek node baru (SongNode)
# hasilHapus : node yang dihapus (SongNode)
# infoLagu   : string informasi posisi lagu (string)
def main():
    p = PList()
    print("============")
    print("kondisi list:")
    p.traversal()
    while True:
        print("============")
        printMenu()
        pilih = int(input("pilihan anda: "))
        if pilih < 0 or pilih > 6:
            print("pilihan tidak valid")
        else:
            if pilih == 0:
                print("program selesai")
                break
            elif pilih == 1:
                lagu = str(input("masukkan lagu: "))
                nodeBaru = SongNode(lagu)
                p.insertFirst(nodeBaru)
            elif pilih == 2:
                lagu = str(input("masukkan lagu: "))
                nodeBaru = SongNode(lagu)
                p.insertLast(nodeBaru)
            elif pilih == 3:
                hasilHapus = p.removeFirst()
                if hasilHapus != None:
                    print(f"{hasilHapus.info} terhapus")
            elif pilih == 4:
                hasilHapus = p.removeLast()
                if hasilHapus != None:
                    print(f"{hasilHapus.info} terhapus")
            elif pilih == 5:
                cari = str(input("masukkan lagu: "))
                infoLagu = p.showInfos(cari)
                if infoLagu != None:
                    print(infoLagu)
                else:
                    print(f"{cari} tidak ditemukan")
            elif pilih == 6:
                cari = str(input("cari lagu: "))
                lagu = str(input("masukkan lagu baru: "))
                nodeBaru = SongNode(lagu)
                if not p.insertAfter(cari, nodeBaru):
                    print(f"{cari} tidak ditemukan")
            
            print("Isi list:")
            p.traversal()

if __name__ == '__main__':
    main()