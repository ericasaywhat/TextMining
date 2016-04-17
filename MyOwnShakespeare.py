from pattern.web import *
from text_mining_analysis import *

url = URL('http://www.shakespeares-sonnets.com/all.php')
all_sonnets = url.download()

#save sonnets to a txt file so we don't have to download multiple times
with open('web_sonnets.txt', 'w') as e:	
	e.write(all_sonnets)

d = open('web_sonnets.txt').read()
start_index = d.index('I.')			#skips the intro stuff and finds where the sonnets start
end_index = d.index('Copyright')	#finds where the sonnets end

just_sonnets = d[start_index:end_index]


clean_sonnets = plaintext(just_sonnets).encode("UTF-8")

sonnets_to_proccess = proccessed_sonnet(clean_sonnets) #removes roman numerals from plaintext sonnets
hist = process_file(sonnets_to_proccess)    #creates a histogram of word frequency in Shakespeare's sonnets


with open('sonnets.txt','w') as f:
	f.write(sonnets_to_proccess)	#puts just the sonnets into one txt file


IAmMyOwnShakespeare = "\n".join(Shakespeare(hist)[1:])	#makes a new sonnet

with open('IAmMyOwnShakespeare.txt', 'w') as g:
	g.write(IAmMyOwnShakespeare)


#To create a sorted histogram for word frequency analysis:

# import operator
# sorted_hist = sorted(hist.items(), key=operator.itemgetter(1))

# print sorted_hist
