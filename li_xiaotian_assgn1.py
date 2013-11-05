#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
class file():
    '''A file class that includes functions of counting paras, sentences, and words'''
    def __init__(self, path):
        self.path = path
    def readFile(self):
        '''Function that reads the file and returns a list of paragraphs'''
        file = open(self.path,'r')
        para = ''
        paras = []
        while 1:
            line = file.readline()
#             print line
            if line != '\n':
                line = line.replace('\n',' ')   # Delete the line break at the end of the line
                para += line
            else:
                paras.append(para)
                para = ''
            if not line:
                paras.append(para)
                break
        return paras
    def paragraphsNum(self):
        '''Function that returns the total number of paragraphs of a file'''
        return len(self.readFile())
    def sentencesNum(self):
        '''Function that returns the total number of sentences of a file'''
        total_sentences_Num = 0
        processedParas = self.fileProcessing()
        for para in processedParas:
            sentences_para = re.findall('\s(?:[\w"-]+|[\d,]+)[\'"\)!?\.]+\s+(?:[\(\'"A-Z]\w*|\d+)', para)
            senNum_para = len(sentences_para) + 1
#             print sentences_para
#             print senNum_para
            total_sentences_Num += senNum_para
        return total_sentences_Num
    def wordsNum(self,type,num = None):
        '''Function that returns the total number of words of a file'''
        total_words_Num = 0
#         nonrepeated_words_Num = 0
        words = []
        paras = self.readFile()
        for para in paras:
#             para = re.sub('[^\w\d\s]+','', para)
            para = para.split()
            for word in para:
                    words.append(word)
            total_words_Num += len(para)
        if type == 'all':
            return total_words_Num
        elif type == 'non-repeated':
            return len(set(words))
        elif type == 'top-words':
            import collections              #Optional, in order to return the frequency of the word
            counter=collections.Counter(words)
            return counter.most_common(num)
    def fileProcessing(self):
        newParas = []
        paras = self.readFile()
        for para in paras:
            if 'â€™' or 'â€' in para:
                para = para.replace('â€™','')
                para = para.replace('â€','')
            if 'Dr.' or 'Mr.' or 'Mrs.' or 'Gov.' or 'Prof.' or 'Rep' in para:
                para = para.replace('Dr.','Prefix')
                para = para.replace('Mr.','Prefix')
                para = para.replace('Mrs.','Prefix') 
                para = para.replace('Gov.','Prefix') 
                para = para.replace('Prof.','Prefix') 
                para = para.replace('Rep.','Prefix') 
            if 'A.' or 'B.' or 'C.' or 'D.' or 'E.' in para:
                para = para.replace('A.','middleInit')
#                 para = para.replace('B.','middleInit')
                para = para.replace('C.','middleInit')
                para = para.replace('D.','middleInit')
                para = para.replace('E.','middleInit')
            if 'Jr.' or 'Sr.' in para:
                para = para.replace('Jr.','Suffix')
                para = para.replace('Sr.','Suffix')
            if 'Univ.' or 'Rep.' or 'Apt.' or 'B.P.M.':
                para = para.replace('Univ.','Abbr')
                para = para.replace('Rep.','Abbr')
                para = para.replace('Apt.','Abbr')
                para = para.replace('B.P.M.','Abbr.')
            newParas.append(para)
        return newParas
        

def main():
    hw1 = file('test.txt')
    print 'NLP HW1 (Xiaotian Li)\n','*'*80
    print 'Paragraphs:', hw1.paragraphsNum()
    print 'Sentences:', hw1.sentencesNum()
    print 'Words:', hw1.wordsNum('all')
    print '\n(Additional work)'
    print 'Non-repeated words:', hw1.wordsNum('non-repeated')
    print 'Top words are:', hw1.wordsNum('top-words',5)
if __name__ == '__main__':
    main()

