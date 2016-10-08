import nltk, os, glob, re, sys
from nltk.collocations import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from collections import Counter
from nltk import bigrams
from nltk import trigrams
from nltk.util import ngrams
from nltk.corpus import stopwords
from pymystem3 import Mystem
'''
alltext = []
m = Mystem()

names = glob.glob('./OpenCorpora/*.txt')    #все файлы корпуса
for name in names:
    if os.path.isfile(name):
        texty = open(name)
        text = texty.read()
        for s in text:
            alltext.append(s)

result = ''.join(alltext)
#print(result)
textsegma = sent_tokenize(result)          #бьем на предложения
#print(textsegma)
f = open('senttok.txt', 'w')
f.write(str(textsegma))
f.close()

lemmaswrite = open('lemmasmystem.txt')
with open('senttok.txt') as tokenz:
    text = tokenz.read()

lemmas = m.lemmatize(text)
#print(lemmas)
with open('senttok.txt', 'w') as tokenz:
    tokenz.write(''.join(lemmas))

lemmas2 = os.system(r'/home/haniani/Загрузки/mystem -l '+ 'senttok.txt' + ' ' + 'lemmasmystem.txt')              #лемматизируем
'''
forgrams = open('lemmasmystem.txt', 'r')
forgrams2 = forgrams.read()
forgrams2 = re.sub(r'}{', ' ', forgrams2)
forgrams3 = forgrams2.split(" ")
forgrams3 = re.sub(r'\.|\,|\*|\?|\'|n|}|{|\|\w*\b', '', str(forgrams3))
forgrams4 = forgrams3.split(' ')
forgrams5 = [word for word in forgrams4 if word not in stopwords.words('russian')]

#print(forgrams4)

lll = 0
bbb = 0
ttt = 0

file4gramsPosition = open('FGramsPositions.txt', 'w')
fileBigramPosition = open('FBigramPositions.txt', 'w')
fileTrigramPosition = open('FTrigrramPositions.txt', 'w')
filefreqB = open('BigraFreq.txt', 'w')
filefreqT = open('TrigramFreq.txt', 'w')
filePmiB = open('PmiB.txt', 'w')
filePmiT = open('PmiT.txt', 'w')
fileFreqWords = open('WordsFreq.txt', 'w')
        
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(forgrams5)
finder2 = TrigramCollocationFinder.from_words(forgrams5)
finder.apply_freq_filter(4)
finder2.apply_freq_filter(4)



bigr = ngrams(forgrams5, 2)
trigr = ngrams(forgrams5, 3) 
fourgr = ngrams(forgrams5, 4)                   #4-граммы

for i in fourgr:                          #слово; позиция в би-три-4грамме; номер 2-3-4гр
    lll = lll + 1
    for k, st in enumerate(i):
        print(str(st)+ ";" + str(k) + ";" + str(lll))
        file4gramsPosition.write(str(st)+ ";" + str(k) + ";" + str(lll) + "\n")

for i in bigr:
    bbb = bbb + 1
    for k, st in enumerate(i):
        print(str(st)+ ";" + str(k) + ";" + str(bbb))
        fileBigramPosition.write(str(st)+ ";" + str(k) + ";" + str(bbb) + "\n")

for i in trigr:
    ttt = ttt + 1
    for k, st in enumerate(i):
        print(str(st)+ ";" + str(k) + ";" + str(ttt))
        fileTrigramPosition.write(str(st)+ ";" + str(k) + ";" + str(ttt) + "\n")

#частота слов
diction = Counter(forgrams5)
fileFreqWords.writelines('{0}={1}\n'.format(k,v) for k,v in diction.items())    

for k,v in finder.ngram_fd.items():            #частота биграммов и триграммов
  print("частота биграммов", k,v)
  filefreqB.write(str(k) + ';' + str(v) + "\n")

for q,x in finder2.ngram_fd.items():
  print("частота триграммов", q,x)
  filefreqT.write(str(q) + ';' + str(x) + "\n")

for i in finder.score_ngrams(bigram_measures.pmi):  #pmi биграммов и триграммов
    print('Биграммы пми', i)
    filePmiB.write(str(i) + "\n")

for p in finder2.score_ngrams(trigram_measures.pmi):
    print('Триграммы пми', p)
    filePmiT.write(str(p) + "\n")

file4gramsPosition.close()
filefreqB.close()
filefreqT.close
filePmiB.close()
filePmiT.close()
fileFreqWords.close()
fileBigramPosition.close()
fileTrigramPosition.close()

sys.exit()