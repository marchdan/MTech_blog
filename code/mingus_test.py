
from mingus.core import *
from mingus.containers import *
#from mingus.midi import *
from mingus.extra import *
from mingus.midi import *
from time import *
'''
notes.is_valid_note(note)
notes.reduce_accidentals(note)
notes.note_to_int(note)
notes.int_to_note(note)
notes.augment(note)
notes.diminish(note)
notes.to_minor(note)
notes.to_major(note)
'''

def transform(note):
	note = note.lower().capitalize()
	if notes.is_valid_note(note):
		return note
	else:
		raise Exception("Please enter a valid musical note!!!!!!")

def transpose(note, trans):
	if trans > 0:
		for i in range(trans):
			note = notes.augment(note)
	elif trans < 0:
		trans = trans * -1
		for i in range(trans):
			note = notes.diminish(note)
	return notes.reduce_accidentals(note)

def get_bar(time, key):
	b = Bar(key, (time, 4))
	return b

def writemusic(nts, time, key, file):
	t = Track()
	bt = 0
	b = get_bar(time, key)
	for i in range(len(nts)):
		b + Note(nts[i])
		if (bt+1)%time == 0:
			t + b 
			b = get_bar(time, key)
		bt += 1
	##test = lilypond.from_Track(t)
	##lilypond.to_pdf(test, file)
	return t

if __name__ == "__main__":
	choice = int(input("Transpose(0) or Write(1)? (-1 to exit) "))
	while(choice >= 0):
		if choice == 0:
			n = raw_input("Note name: ")
			n = transform(n)
			t = int(raw_input("Number of half-steps to transpose: "))
			print transpose(n, t)
		elif choice == 1:
			fq = raw_input("File?(y/n): ")
			if fq == 'y':
				fname = raw_input("File name: ")
				fname = "inputs/"+fname
				file = open(fname, "r")
				NoteL = []
				key = file.readline().strip()
				transform(key)
				num = int(file.readline().strip())
				for i in range(num):
					get= file.readline().strip().split()
					if (len(get) == 1):
						get.append("4")
					get[0] = transform(get[0])
					n = get[0] + '-' + get[1]
					NoteL.append(n)
				time = int(file.readline().strip())
				t = writemusic(NoteL, time, key, file.readline().strip())
				file.close()
			else:
				NoteL = []
				key = raw_input("Key (Case sensitive): ")
				transform(key)
				time = int(input("Beats per measure(#/4): "))
				num = int(input("Number of notes: "))
				for i in range(num):
					get= raw_input("Note(NAME OCTAVE): ").split()
					if (len(get) == 1):
						get.append("4")
					get[0] = transform(get[0])
					n = get[0] + '-' + get[1]
					NoteL.append(n)
				t = writemusic(NoteL, time, key,raw_input("File Title: "))

		c = Composition()
		c.add_track(t)
		c.set_author("Daniel Ackermans", "ackerd2@rpi.edu")
		c.set_title("Composition")

		t = localtime(None)
		tS = struct_time(t)
		time_string = "%s_%s_%s" % (tS[0], tS[1], t[2])


		outFile = raw_input("Outfile name: ")
		pdfF = "pdfs/"+outFile+".pdf"
		midF = "midiFiles/"+outFile+".mid"
		file_string = "logs/history_" + time_string + ".txt"

		tet = lilypond.from_Composition(c)
		lilypond.to_pdf(tet, pdfF)
		
		hist = open(file_string, "a")
		hist.write(str(asctime(t)) + "\n")
		hist.write(tet + "\n")
		hist.write("\n")
		hist.close()
		
		midi_file_out.write_Composition(midF, c)

		choice = int(input("Transpose(0) or Write(1)? (-1 to exit) "))
