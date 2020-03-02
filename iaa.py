import matplotlib.pyplot as plt

import PyPDF3

name = input('nome do arquivo: ')

file = open(name,'rb')

fileReader = PyPDF3.PdfFileReader(file)

info = fileReader.getPage(0)
text = info.extractText()
textSplit = text.split('\n')

iaa = []
x   = []
for i in range(len(textSplit)):
    if(textSplit[i] == 'IAA -'):
        iaa.append(float(textSplit[i-1]))
        x.append(1+len(iaa))
plt.title('IAA')
plt.xlabel('Semestres')
plt.ylabel('Media')
plt.plot(iaa,'*',c='red')
plt.plot(iaa,'-',c='blue')
plt.show()
