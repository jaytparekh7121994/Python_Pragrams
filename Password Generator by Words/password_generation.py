# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
def generate_password():
    random_list = []
    str_list = []
    for i in range(0,3):
        random_list.append(random.randint(0,len(word_list)))
        str_list.append(word_list[random_list[i]])
    password = "".join(str_list)
    return password
# It should return a string consisting of three random words 
# concatenated together without spaces
# Alternate methods
    # def generate_password():
        # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
    # def generate_password():
       # return ''.join(random.sample(word_list, 3))

# test your function
print(generate_password())
