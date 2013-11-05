import hw2_preprocess
words_list = hw2_preprocess.words
tags_list = hw2_preprocess.tags_type
 
class word_class:
    def __init__(self):
        dict_of_tags_per_word = {}
        for tag in tags_list:
            dict_of_tags_per_word[tag] = 0
        self.dict_of_tag = dict_of_tags_per_word
         
raw_file = open('corpus.txt')
# raw_file = open('test.txt')
read_file = raw_file.readlines()
 
dict_of_words = {}
# dict_of_bitags = {}
 
for word in words_list:
    word_obj = word_class()
    dict_of_words[word] = word_obj.dict_of_tag
     
 
 
for line in read_file:
    line = line.rstrip('\n')
    line = line.split('\t')
    if line == ['']:
        line = ['s', 'S']
    word = line[0]
    tag = line[1]
    dict_of_words[word][tag] += 1
 
print dict_of_words
 
dict_of_words_percent = dict_of_words
 
for word in words_list:
    word_count = 0
    for tag in tags_list:
        word_count += dict_of_words[word][tag]
    for tag in tags_list:
        dict_of_words_percent[word][tag] /= float(word_count)
 
print '*'*70
print dict_of_words_percent