from IPython import get_ipython
get_ipython().system('pip install openpyxl')
from openpyxl import Workbook
import pandas as pd


a = pd.read_excel("Yoklama.xlsx")
asd = a.iloc[:,0]

b = pd.read_excel("Sınıf Listesi.xlsx")
bsd = b.iloc[:,0]


q = list(set(bsd)-set(asd))


yoklama = Workbook()
sheet = yoklama.active
sheet.append(q)
yoklama.save("Katılmayan Öğrenciler.xlsx")
yoklama.close()

