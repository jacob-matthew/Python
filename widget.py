from secrets import choice, randbelow
import pasteboard
# Get a list of words that are 4-6 characters long.
with open('words.py') as f:
	words = f.readlines()
# Select 4 words from the list.
pwords = [ choice(words).strip() for i in range(4) ]

# Add a numeral and a "special" character.
# Capitalize one of the words.
numeral = str(randbelow(10))
special = choice('!@#$%^&*')
pNum = randbelow(4)
pSpec = randbelow(4)
pCap = randbelow(4)
pwords[pNum] = pwords[pNum] + numeral
pwords[pSpec] = pwords[pSpec] + special
pwords[pCap] = pwords[pCap].capitalize()
# Assemble the password and put it on the clipboard.
pw = '-'.join(pwords)
pasteboard.set_string(pw)

