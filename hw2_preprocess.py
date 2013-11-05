import viterbi

# raw_file = open('test.txt')
raw_file = open('corpus.txt')

tags_type = []
all_words = []
all_tags = []
word_tag_tuples = []
tag_tuples = []
all_tag_tuples = []
words = []
read_file = raw_file.readlines()
for line in read_file:
    line = line.rstrip('\n')
    line = line.split('\t')
    if line == ['']:
        line = ['', 'S']
    word = line[0]
    tag = line[1]
    if word not in words:
        words.append(word)
    if tag not in tags_type:
        tags_type.append(tag)
    all_words.append(word)
    all_tags.append(tag)
    word_tag_tuples.append((word,tag))
    
# print all_words
# print all_tags

for i in range(0,len(all_tags)-1):
    tag_tuples.append((all_tags[i],all_tags[i+1]))

for x in range(len(tags_type)):
    for y in range(len(tags_type)):
        all_tag_tuples.append((tags_type[x],tags_type[y]))
print all_tag_tuples
# print tag_tuples
# print len(tag_tuples)

# tag_tuples_giventag = all_tags[:len(all_tags)-1]
# print tag_tuples_giventag

tag_count = {}
for tag in all_tags:
    if tag not in tag_count:
        tag_count[tag] = 1
    else:
        tag_count[tag] += 1
# print tag_count

dict_of_bitags_count = {}
for bitag in all_tag_tuples:
    if bitag not in dict_of_bitags_count:
        if bitag not in tag_tuples:
            dict_of_bitags_count[bitag] = 1    #+1 smoothing
        else:
            dict_of_bitags_count[bitag] = 2
    else:
        dict_of_bitags_count[bitag] += 1

dict_of_bitags_percentage = {}
for bitag in dict_of_bitags_count:
    dict_of_bitags_percentage[bitag] = dict_of_bitags_count[bitag]/float(tag_count[bitag[0]]+len(tags_type))

print '*'*70    
print 'dict_of_bitags_count', dict_of_bitags_count
print 'dict_of_bitags_percentage', dict_of_bitags_percentage
print len(dict_of_bitags_percentage)


dict_of_wordGivenTag_count = {}
for word_tag in word_tag_tuples:
    if word_tag not in dict_of_wordGivenTag_count:
        dict_of_wordGivenTag_count[word_tag] = 1
    else:
        dict_of_wordGivenTag_count[word_tag] += 1

dict_of_wordGivenTag_percentage = {}
for word_tag in dict_of_wordGivenTag_count:
    dict_of_wordGivenTag_percentage[word_tag] = dict_of_wordGivenTag_count[word_tag]/float(tag_count[word_tag[1]])

print '*'*70
print 'dict_of_wordGivenTag_count', dict_of_wordGivenTag_count
print 'dict_of_wordGivenTag_percentage', dict_of_wordGivenTag_percentage



tags_without_period = []
for tag in tags_type:
    if tag != '.':
        tags_without_period.append(tag)
print 'tags_without_period', tags_without_period
# print len(tags_without_period)

a = [{} for n in range(len(tags_without_period))]
for bitags in dict_of_bitags_percentage:
    for i in range(0, len(tags_without_period)):
#         print bitags[0], tags_without_period[i]
        if bitags[0] == tags_without_period[i] and bitags[1] != 'S':
#             print '====', bitags[0], tags_without_period[i]
            a[i][bitags[1]] = dict_of_bitags_percentage[bitags]
# print 'a', a
# print len(a), len(a[0])
a_matrix = {}
for index,tag in enumerate(tags_without_period):
    a_matrix[tag] = a[index]
print 'a_matrix', a_matrix

tags_without_start_period = []
for tag in tags_type:
    if tag != '.' and tag != 'S':
        tags_without_start_period.append(tag)
        
b = [{} for n in range(len(tags_without_start_period))]
for index,tag in enumerate(tags_without_start_period):
    for wordtag in dict_of_wordGivenTag_percentage:
        if wordtag[1] == tag:
#             print wordtag[1], tag
            b[index][wordtag[0]] = dict_of_wordGivenTag_percentage[wordtag]
# print tags_without_start_period
# print 'b', b
# print len(b), len(b[0])
b_matrix = {}
for index,tag in enumerate(tags_without_start_period):
    b_matrix[tag] = b[index]
print 'b_matrix', b_matrix
 
observation = ['i',"'d",'like','to','go','to','a','fancy','restaurant']
print observation
 
print '$'*70
print viterbi.Viterbi(len(tags_without_start_period),len(observation),a_matrix,b_matrix,observation,tags_without_start_period)

# list = [0,0,1,4,5,4,3,6,7]
# for i in list:
#     print tags_without_start_period[list[i]]
# print tags_without_start_period, "00"