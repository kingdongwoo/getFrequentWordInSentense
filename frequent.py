from collections import Counter

#data_set
data_set = "baRrIErS baRrieRs   CLASSROom  cRedIT  MiNIMizE SPelL  tIe   Poker  raDIUS MINimIZE QualIFICaTIoNsCRedit  QUaLiFicaTiOns  orGAN  cLaSSRoOM   UNDo   creDiT "

rank = 3
length = 2

#string -> list
split_it = data_set.split()

#count word dictionary
Counter = Counter(split_it)
most_occur = Counter.most_common()
print("most occur count")
print(most_occur)

#get word if word size over length
most_occur_length=[]
for i in most_occur:
    if(len(i[0]) >= length):
        most_occur_length.append(i)
print("check if word size is over length")
print(most_occur_length)

#if rank is same order by character
if_same_rank = []
count = 0
for i in most_occur_length:
    count += 1
    if(i[1]==most_occur_length[rank-1][1]):
        count2 = count
        if_same_rank .append(i)

if_same_rank .sort()
print("same length word sorting")
print(if_same_rank )
print("the 3rd most frequently used word in dataset is: ",end="")
print(if_same_rank[rank-count2-1][0].lower())

