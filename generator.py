import itertools as it
import string
import math


file_size = 0
passcode_length = 0
is_Range = True
possible_passcodes = []
passcode_calculated_flag =False

def generate(possible_passcodes,is_Range,length):
	
	#Uncomment the below two lines to test the algorithm...Try your own password as well
	#pass1 = axf2e1
	#possible_passcodes = 'a1mx25feq'

	#Flag variable to break out of loop if finds the passcode
	file = open('PassList.txt','w')
	found = False
	while True:
		try:
			for index in range(length):

				#This conditional will decide it the user has entered fixed lengthed passcode or ranged apsscode
				if is_Range == True:
					temp = it.permutations(possible_passcodes,index)
				else:
					temp = it.permutations(possible_passcodes,length)
				for i in temp:
					pass1 = ''.join(i)
					file.write('\n'+pass1)
	
					#Checks to see if password matches...Uncomment this if clause to test this algorithm
			# 		if pass1 == password:
			# 			found = True
			# 			break
			# 	if found == True:
			# 		break
			# if found == True:
			# 	break
	


		#Breaks out of loop if index error arises ie all possible combinations have been tried
		except IndexError:
			break
	file.close()

	#print('\n\nPassword Found\nPassword: {}\n\n'.format(pass1))

def calculate_size(is_Range, length, pass_length):
	size = 0
	if is_Range:
		#Calculate permutation
		for i in range(1,length+1):
			for j in range(1,i+1):
				size += math.factorial(i)/math.factorial(i-j)
		return size
	else:
		total_permutation = math.factorial(pass_length)/math.factorial(pass_length - length)
		return length * total_permutation


def menu():
	global file_size, passcode_length, is_Range, possible_passcodes, passcode_calculated_flag
	while True:
		#Menu Frame
		print("\n\n\t|----------------------------WordList Generator-----------------------|\n\t\t\t\t\t\t\t\t\t----By Singularity\n\n")
		print("\n\t\tChoose Options....\n")
		print(
		'''
		\t\t\t1)Include all lowercase alphabets\n
		\t\t\t2)Include all Uppercase Alphabets\n
		\t\t\t3)Include all numbers from 0-9\n
		\t\t\t4)Include all special symbols\n
		\t\t\t5)Include custom Characters\n
		\t\t\t6)Set Length of Passcode unless you want to try all possible permutations\n
		\t\t\t7)All set! Lets Generate\n
		\t\t\t\t\t\t\t\t\t\t   Current Length:  {}\n
		\t\t\t\t\t\t\t\t\t\t\tFile size:  {} Bytes
		\t\t\t\t\t\t\t\t\t\t\t\t :  {:.2f} MegaBytes
		\t\t\t\t\t\t\t\t\t\t\t\t :  {:.2f} GigaBytes
		'''.format(passcode_length, file_size, file_size/1024, file_size/(1024**2))
		)
		option_choosen = int(input("\nEnter your choice\n==>"))


		given_data = []
		if option_choosen < 5:
			given_data.append({
				1: [i for i in string.ascii_lowercase],
				2: [i for i in string.ascii_uppercase],
				3: [i for i in range(0,10)],
				4: [i for i in string.punctuation],
				}.get(option_choosen))
		elif option_choosen == 5:
			given_data.append(input("\nEnter the characters you want to include. You can also include whitespaces if there is any...\n"))

		elif option_choosen == 6:
			Minimum = int(input("\nEnter Minimum digits your passcode may be of\n==>"))
			Maximum = int(input("\nEnter Maximum digits your passcode may be of\n==>"))
			#Sets the passcode length and is_Range flag
			if Maximum == Minimum:
				passcode_length = Maximum
				is_Range = False
			else:
				passcode_length = Maximum-Minimum
				is_Range = True
			#Turn the passcode calculated flag
			passcode_calculated_flag = True

		elif option_choosen == 7:
			generate(possible_passcodes,is_Range,passcode_length)
			break

		#Convert the list to plain string
		for i in given_data:
			for j in i:
				#if current element is an integer convert it to string
				if type(j) == int:
					j = str(j)
				possible_passcodes += j

		print(possible_passcodes)

		#Calculate the file size and length with default length of given passcode until user specifies the passcode
		if passcode_calculated_flag == False:
			passcode_length = len(possible_passcodes)
		file_size = calculate_size(is_Range, passcode_length, len(possible_passcodes))

if __name__ == '__main__':
	menu()