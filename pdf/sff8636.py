import pdfplumber
import pandas as pd


pdf = pdfplumber.open("SFF8636.pdf")
pages = pdf.pages[26]
tables = pages.extract_tables()
data = pd.DataFrame(tables[0][1:],columns=tables[0][0])
header = tables[0][0]

for page in range(27,41):
# for page in range(27,28):
    pages = pdf.pages[page]
    tables = pages.extract_tables()
    for i in range(len(tables)):
        if tables[i][0][0] == 'Byte':
            # data.append( pd.DataFrame(tables[i][1:],columns=tables[i][0]))
            tmp = pd.DataFrame(tables[i][1:],columns=tables[i][0])
            data = data.append(tmp,sort=False)
        # if tables[i][0][0] == '145':
        #     # data.append( pd.DataFrame(tables[i][1:],columns=tables[i][0]))
        #     tmp = pd.DataFrame(tables[i][1:],columns=data[0][0])
        #     data = data.append(tmp,sort=False)

pages = pdf.pages[41]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)

pages = pdf.pages[42]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)

for page in range(42,44):
# for page in range(27,28):
    pages = pdf.pages[page]
    tables = pages.extract_tables()
    for i in range(len(tables)):
        if tables[i][0][0] == 'Byte':
            tmp = pd.DataFrame(tables[i][1:],columns=tables[i][0])
            data = data.append(tmp,sort=False)

pages = pdf.pages[42]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header),sort=False)
# data = data.append(pd.DataFrame(tables[1][1:],columns=header),sort=False)

for page in range(43,56):
# for page in range(27,28):
    pages = pdf.pages[page]
    tables = pages.extract_tables()
    for i in range(len(tables)):
        if tables[i][0][0] == 'Byte':
            tmp = pd.DataFrame(tables[i][1:],columns=tables[i][0])
            data = data.append(tmp,sort=False)

pages = pdf.pages[56]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)

pages = pdf.pages[57]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)


pages = pdf.pages[58]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)

pages = pdf.pages[59]
tables = pages.extract_tables()
data = data.append(pd.DataFrame(tables[0][0:],columns=header), sort=False)

data.to_excel('sff8636.xlsx', index=False)