
from mingus.core import *
from mingus.containers import *
#from mingus.midi import *
from mingus.extra import *
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

def writemusic(nts, time, key):
	t = Track()
	bt = 0
	b = get_bar(time, key)
	for i in range(len(nts)):
		b + Note(nts[i])
		if (bt+1)%time == 0:
			t + b 
			b = get_bar(time, key)
		bt += 1

	test = lilypond.from_Track(t)
	lilypond.to_pdf(test, "composition")


	


if __name__ == "__main__":
	choice = int(input("Transpose(0) or Write(1)? (-1 to exit) "))
	while(choice >= 0):
		if choice == 0:
			n = raw_input("Note name: ")
			n = transform(n)
			t = int(raw_input("Number of half-steps to transpose: "))
			print transpose(n, t)
		else:
			NoteL = []
			key = raw_input("Key(major): ")
			key = transform(key)
			num = int(input("Number of notes: "))
			for i in range(num):
				get= raw_input("Note(NAME OCTAVE): ").split()
				if (len(get) == 1):
					get.append("4")
				get[0] = transform(get[0])
				n = get[0] + '-' + get[1]
				NoteL.append(n)
			time = int(input("Beats per measure(#/4): "))
			writemusic(NoteL, time, key)
		choice = int(input("Transpose(0) or Write(1)? (-1 to exit) "))
