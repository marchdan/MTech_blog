import sys
import random
import os


FLATS = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
SHARPS = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

def getMajor(key):
	maj = []
	if(len(key) == 1):
		if(key == 'f' or key == 'c'):
			i = 0
			while(FLATS[i] != key):
				i += 1
			while(len(maj) < 8):
				if(i >= 12):
					i -= 12
				maj.append(FLATS[i])
				if(len(maj) == 3 or len(maj) == 7):
					i += 1
				else:
					i += 2
		else:
			i = 0
			while(SHARPS[i] != key):
				i += 1
			while(len(maj) < 8):
				if(i >= 12):
					i -= 12
				maj.append(SHARPS[i])
				if(len(maj) == 3 or len(maj) == 7):
					i += 1
				else:
					i += 2
	else:
		if(key[1] == 'b'):
			i = 0
			while(FLATS[i] != key):
				i += 1
			while(len(maj) < 8):
				if(i >= 12):
					i -= 12
				maj.append(FLATS[i])
				if(len(maj) == 3 or len(maj) == 7):
					i += 1
				else:
					i += 2
		else:
			print("ERROR")

	return maj

def getMinor(key):
	mnr = []
	if(len(key) == 1):
		if(key != 'b' and key != 'e'):
			i = 0
			while(FLATS[i] != key):
				i += 1
			while(len(mnr) < 8):
				if(i >= 12):
					i -= 12
				mnr.append(FLATS[i])
				if(len(mnr) == 2 or len(mnr) == 5):
					i += 1
				else:
					i += 2
		else:
			i = 0
			while(SHARPS[i] != key):
				i += 1
			while(len(mnr) < 8):
				if(i >= 12):
					i -= 12
				mnr.append(SHARPS[i])
				if(len(mnr) == 2 or len(mnr) == 5):
					i += 1
				else:
					i += 2
	else:
		if(key[1] == 'b'):
			i = 0
			while(FLATS[i] != key):
				i += 1
			while(len(mnr) < 8):
				if(i >= 12):
					i -= 12
				mnr.append(FLATS[i])
				if(len(mnr) == 2 or len(mnr) == 5):
					i += 1
				else:
					i += 2
		else:
			i = 0
			while(SHARPS[i] != key):
				i += 1
			while(len(mnr) < 8):
				if(i >= 12):
					i -= 12
				mnr.append(SHARPS[i])
				if(len(mnr) == 2 or len(mnr) == 5):
					i += 1
				else:
					i += 2

	return mnr







if __name__ == "__main__":

	inputs = sys.argv

	key = inputs[1].lower().strip()

	#MAJOR: 2, 2, 1, 2, 2, 2, 1
	#MINOR: 2, 1, 2, 2, 1, 2, 2		
	maj = getMajor(key)
	mnr = getMinor(key)

	notesMaj = []
	notesMin = []
	octaves = []
	lengths = []
	i = 0
	while i < 16:
		num = random.randint(0, 7)
		notesMaj.append(maj[num])
		notesMin.append(mnr[num])
		octaves.append(4)
		lengths.append(4)
		i += 1

	print("The notes for Major are: {}".format(notesMaj))
	print("The notes for Minor are: {}".format(notesMin))

	infile = inputs[2].lower().strip() 
	outfile1 = "inputs/" + inputs[2].lower().strip() + 'Major.txt'
	outfile2 = "inputs/" + inputs[2].lower().strip() + 'Minor.txt'
	fileMaj = open(outfile1, 'w')
	fileMin = open(outfile2, 'w')
	for i in range(len(notesMaj)):
		fileMaj.write("{} {} {}\n".format(notesMaj[i], octaves[i], lengths[i]))
		fileMin.write("{} {} {}\n".format(notesMin[i], octaves[i], lengths[i]))

	fileMaj.close()
	fileMin.close()

	os.system('python3 music.py {}Major.txt {} major treble 4/4 120 > lily/{}Major.ly'.format(infile, key, infile))
	os.system('python3 music.py {}Minor.txt {} minor treble 4/4 120 > lily/{}Minor.ly'.format(infile, key, infile))
	os.system('lilypond lily/{}Major.ly'.format(infile))
	os.system('lilypond lily/{}Minor.ly'.format(infile))

