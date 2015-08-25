import re

# defining word list
word_list=['is','of','the','and','or','in','on','at','you','it']

# pointing to the file to read data from
text_file=open('pg11.txt','r')

# defining the dictionary to store the frequency of the words 
word_count={}
def dict_init():
	for word in word_list:
		word_count[word]=0	# putting initial value of keys to 0

# Defining frequency counter
def freq_count():
	for lines in text_file:
		lines=lines.strip("\n")
		for word in lines.split(" "):
			word=re.sub("\W+","",word)
			for words in word_list:
				if word.lower() == words.lower():
					word_count[words]+=1

# defining ability to add words to the wordlist				
def word_add():
	word_list.sort()
	print("The Word list are:\n\n")
	for word in word_list:
		print(word)
	while(True):
		print("Do you want to add more? \n")
		ask=input("ANS==>>>")
		if ask.lower()=="y" or ask.lower()=="yes":
			extra_word=input('Enter word: ')
			try:
				word_list.index(extra_word)
				print("The word '{}' already exists in the current word list so enter new word!!!!!".format(extra_word))
				word_add()
			except:
				word_list.append(extra_word)
				print(word_list)
				
		else:
			break



def main():
	word_add()# adding words to word list
	dict_init()# initiating dictionary for storing frequencies
	freq_count()# Counting the frequency of words
	print("The frequency of words are: ",word_count)

if __name__=="__main__":
	main()
