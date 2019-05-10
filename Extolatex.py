import os
import codecs
import string

# change working directory
os.chdir('C:\\Users\\Chenxi\\Dropbox\\Projects\\Extolatex')


def transtotex(filename, label = None, cite = None):
	"""
	Transfer the Elan output (as interlinear text: export as tranditional transcript text) 
	to latex (expex package) syntax
	label - the label of the example for cross-reference (str)
	cite - the example index in the corpus (str)
	"""
	
	# oldlist = codecs.open('AL_GN.txt', 'r', encoding='utf-8')

	oldlist = [line.rstrip('\n') for line in codecs.open(filename)]
	newlist = []
	
	if label != None: 
		label_print = '\label{' + str(label) + '}'
	else: 
		label_print = ''
		
	cite_print = r'\trailingcitation' + '{[' + str(cite) + ']}'

	# add in Latex syntax
	for line in oldlist:
	# replace possible ending characters to //

		if line.startswith("tx@"):
			newlist.append((line.strip("\r") + "//").replace('tx@', '\ex' + label_print + '\n' + r'\begingl' + '\n' + '\gla'))		
			# after operator "+", \r is presented in between string and "//", thus remove it beforehand	

			newlist.append('\n'+ '\glb' + '  ' + '//' + '\n')
			
		elif line.startswith("tf@"):
			if cite == 1:
				line += cite_print
			newlist.append((line.strip("\r") + "'" + '//' + '\n' + '\endgl' + '\n' + r'\xe' + '\n' + '\n').replace('tf@' + '   ', '\glft' + ' ' + '`'))
			# remove space in between tf@ and sentence

	# write into test.txt 
	newfile = open('test.txt', 'w')

	for line in newlist:
		newfile.write(line)
		
	newfile.close()
	newfile = file('test.txt', 'r')

transtotex('WM_JJ.txt')