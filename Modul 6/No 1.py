print("No 1")
class MhsTIF(object):
    """Class MhsTIF yang dibangun dari class Mahasiswa"""

    def __init__(self,nama,NIM,kota,us):
        """Metode inisialisasi ini menutupimetode inisiasi di class Manusia."""
        self.nama=nama
        self.NIM=NIM
        self.kotaTinggal=kota
        self.uangsaku=us
    

c0 = MhsTIF('Ika', 10, 'sukoharjo', 240000)
c1 = MhsTIF('Budi', 51, 'sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'surakarta', 250000)
c3 = MhsTIF('Chandra', 18, 'surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'wonogiri', 245000)
c8 = MhsTIF('Janto', 23, 'klaten', 245000)
c9 = MhsTIF('Hasan', 64, 'karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'purwadadi', 265000)


Daftar = [c0.NIM,c1.NIM,c2.NIM,c3.NIM,c4.NIM,c5.NIM,c6.NIM,c7.NIM,c8.NIM,c9.NIM,c10.NIM]

def mergeSort(nlist):
    print("Membelah ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Menggabungkan ",nlist)
nlist = Daftar
print("Hasil dari MergeSort")
mergeSort(nlist) 
print(nlist)

def quickSort(data_list):
   quickSortHlp(data_list,0,len(data_list)-1)

def quickSortHlp(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       quickSortHlp(data_list,first,splitpoint-1)
       quickSortHlp(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp


   return rightmark

data_list = Daftar
quickSort(data_list)
print("\n"+"Hasil QuickSort")
print(data_list)
