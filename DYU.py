print("""

||\        \     //      ||      ||
|| \        \   //       ||      ||     ---------------
||  \        \ //        ||      ||     by str1g1f0rmes
||  //        ||         ||      ||     ---------------
|| //         ||         ||      ||
||//          ||         ||======||  

""")


from openpyxl import Workbook
import pandas as pd


sınıfl_i = input("Sınıf Listesinin Adını Giriniz: ")

SınıfL = pd.read_excel(sınıfl_i)
SınıfL_1 = SınıfL.iloc[:,0]


yoklama_i = input("Yoklama Listesinin Adını Giriniz: ")

Yoklama= pd.read_excel(yoklama_i)
Yoklama_1 = Yoklama.iloc[:,0]


Katılmayanlar = list(set(SınıfL_1)-set(Yoklama_1))


katılmayanlar_i = input("Katılmayanlar Listesinin Adı Ne Olsun?: ")

yoklama = Workbook()
sheet = yoklama.active
sheet.append(Katılmayanlar)
yoklama.save(katılmayanlar_i)
yoklama.close()

print("\nİşlem Gerçekleştirildi, Kolay Gelsin.")
