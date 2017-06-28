#! /usr/bin/python
import yaml

# TODO: (optional) ingredients/instructions

def _getMetadata(f):
	metadataText=""
	metadataEnd = False
	while not metadataEnd:
		line = f.readline()
		if line == "----\n":
			metadataEnd = True
		else:
			metadataText += line
	return yaml.load(metadataText)

def parserecipe(f):
	metadata = _getMetadata(f)
	instructions = []
	for line in f.readlines():
		line = line.rstrip();
		if line == "": # Blank
			None # Ignore
		elif line.startswith("\t"): # Ingredient
			line = line.lstrip('\t')
			if line.startswith('  '): # Continuation of previous ingredient
				line = line.lstrip(' ')
				if line.startswith('OR '):
					line = line[3:] # Strip 'OR '
					# Append to previous ingredient
					instructions[-1]['ingredients'][-1].append(line.lstrip())
				else:
					raise ValueError("Unknown continuation: {}".format(line))
			else:
				# Regular ingredient, just list it
				instructions[-1]['ingredients'].append([line.lstrip()])
		else: # Instruction
			# Begin a new one with this line as the text
			instructions.append({'text': line, 'ingredients': []})
	
	return {'metadata': metadata, 'instructions': instructions}

if __name__ == '__main__':
	import sys
	from pprint import pprint
	pprint(parserecipe(open(sys.argv[1], 'r')))
