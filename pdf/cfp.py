import pdfplumber
import pandas as pd


pdf = pdfplumber.open("CFP_MSA_MIS_V2p6r06a.pdf")
pages = pdf.pages[64]
tables = pages.extract_tables()
data = pd.DataFrame(tables[1][1:],columns=tables[1][0])
header = tables[1][0]

print(data)
