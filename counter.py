import re
from collections import Counter

#defining word list
word_list=['is','of','the','and','or','in','on','at','you','it']

#pointing to the file to read data from
text_file=open('pg11.txt','r')

#defining the dictionary to store the frequency of the words 
word_count={}
def dict_init():
	for word in word_list:
		word_count[word]=0	#putting initial value of keys to 0

#Defining frequency counter
def freq_count(option=1):
	'''option = 1 : calculates only the frequency of words presents in the word_list
	   option = 2 : appends the word_list with new words found while reading the file calculates the frequency too
	   The default option is 1 
	   '''
	for lines in text_file:
		lines=lines.strip("\n")
		for word in lines.split(" "):
			word=re.sub("\W+","",word)
			word=word.lower()
			if word in word_list:
				word_count[word]+=1
			elif word=="":#Why??? Because the program was also counting blank space as a word so this line prevents the issue. 
				pass
			else:
				if option==2:
					word_list.append(word.lower())
					word_count[word]=1
				else:
					pass
					
	return word_count

#This function prints word present in the word list
def list_printer():
	word_list.sort()
	print("\nThe Word list are:\n")
	for word in word_list:
		print(word)

#defining function to add words to the wordlist

def word_add():
	extra_word=input('Enter word: ')
	try:	#Checking whether the given word is already in the list
		word_list.index(extra_word) #If the word is already in the word list this method return error 
		print("The word '{}' already exists in the current word list so enter new word!!!!!\n".format(extra_word))
		return word_add()
	except:
		word_list.append(extra_word)
		print('The new Word list : \n',word_list)	
	while(True):
		print("Do you want to add more? \n")
		ask=input("ANS==>>>")
		if ask.lower()=="y" or ask.lower()=="yes":
			print(word_list)
			return word_add()
		else:
			break

#counting maximum frequency of words and printing them and descending order of their frequency
def maxm_freq(n):
	maxm=list(Counter(word_count).most_common(n))
	print("\nThe {} words having highest frequencies are given below:-\n".format(n))
	print("{0:5} : {1:12} :    {2:12}".format("S.N","Word","Frequency"))#
	print("..... : ............ : .............")
	i=1
	for word,freq in maxm:
		print("{0:5d} : {1:12} : {2:12d}".format(i,word,freq),flush=True)
		i+=1

#Defining menu for this app
def menu():
	print("\nWhat do you want to do? \n")
	print("1-Calculate the word frequency from the default word list\n")
	print("2-Add words to word list and calcuate\n")
	print("3-Print the words with higest frequency throughout the given document\n")
	ask=input("Enter your choice: ")
	if ask.isdigit():
		ask=int(ask)
		if ask >0 and ask <4:
			return ask
		else:
			print("\nPlease enter valid option\n")
			return menu()
	else: 
		print("\nPlease enter valid option\n")
		return menu()
	
		



def main():
	list_printer()
	x=menu()
	if x == 1:
		dict_init()
		freq_count(1)
		maxm_freq(len(word_list))
	elif x==2:
		word_add()
		dict_init()
		freq_count(1)
		maxm_freq(len(word_list))
	elif x==3:
		dict_init()
		freq_count(2)
		n=int(input("Please enter the no of maximum frequency words to show '0' to show all: "))
		if n ==0:
			maxm_freq(len(word_list))
		else:
			maxm_freq(n)
	else:
		pass

if __name__=="__main__":
	main()