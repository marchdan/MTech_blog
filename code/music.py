import sys
from time import *

if __name__ == "__main__":
	tr = localtime(None)
	tS = struct_time(tr)
	time_string = "{}-".format(tS[0])
	if(tS[1] < 10):
		time_string += "0"
	time_string += "{}-".format(tS[1])
	if(tS[2] < 10):
		time_string += "0"
	time_string += "{}".format(tS[2])

	inputs = sys.argv

	top = "\\score {"

	bottom = "}"


	head = "\t\\header\n\t{\n"
	head += '\t\ttitle = "{}"\n'.format(inputs[1].strip().rstrip('.txt'))
	head += '\t\tsubtitle = "{}"\n'.format(time_string)
	head += '\t\tcomposer = "Daniel Ackermans"\n'
	head += '\t}\n'

	filename = "inputs/" + inputs[1].strip()

	key = inputs[2].lower()
	modal = inputs[3].lower()
	clef = inputs[4].lower()
	time = inputs[5]
	tempo = int(inputs[6])

	if(len(key) == 1):
		keyNew = key[0]
	else:
		if(key[1] == 'b'):
			keyNew = key[0] + 'es'
		else:
			keyNew = key[0] + 'is'

	data = "\t\\new Staff {\n"
		
	data += "\t\t\\key {} \\{}\n".format(keyNew, modal)
	data += '\t\t\\clef "{}"\n'.format(clef)
	data += '\t\t\\time {}\n'.format(time)
	data += '\t\t\\tempo {} = {}\n\t'.format(time[-1], tempo)

	file = open(filename, 'r')
	notes = []
	octaves = []
	lengths = []

	for line in file:
		lineS = line.split()
		notes.append(lineS[0].lower())
		octaves.append(int(lineS[1]))
		lengths.append(int(lineS[2]))

	baseOct = 3
	curLen = 3
	for i in range(len(notes)):
		if i > 0 :
			data += ' '
		else:
			data += '\t'
		n = notes[i][0]
		if len(notes[i]) == 2:
			if notes[i][1] == '#':
				n += 'is'
			else:
				n += 'es'
		if octaves[i] == baseOct:
			o = ''
		else:
			if octaves[i] > baseOct:
				o = "'"*(octaves[i] - baseOct)
			else:
				o = "," *(baseOct - octaves[i])

		if lengths[i] == curLen:
			l = ''
		else:
			l = str(lengths[i])
			curLen = lengths[i]

		data += (n+o+l)

	data += '\n\t}'

	layout = "\t\\layout { }"

	midi = "\t\\midi { }"


	#print(sys.argv)
	print(top)
	print(head)
	print(data)	
	print(layout)
	print(midi)
	print(bottom)


