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
	sections=[
		{'title': '', 'instructions': []}
	]
	for line in f.readlines():
		line = line.rstrip();
		if line == "": # Blank
			None # Ignore
		elif line.startswith("##"): # Heading
			line = line.lstrip("# ")
			if ( sections[-1] is sections[0] # Default section
					and sections[-1]['instructions'] == [] ): # No instructions yet
				# Reuse the first section, as it's empty
				sections[-1]['title'] = line
			else:
				# Start a new section
				sections.append({'title': line, 'instructions': []})
		elif line.startswith("\t"): # Ingredient
			line = line.lstrip('\t')
			if line.startswith('  '): # Continuation of previous ingredient
				line = line.lstrip(' ')
				if line.startswith('OR '):
					line = line[3:] # Strip 'OR '
					# Append to previous ingredient
					sections[-1]['instructions'][-1]['ingredients'][-1].append(line.lstrip())
				else:
					raise ValueError("Unknown continuation: {}".format(line))
			else:
				# Regular ingredient, just list it
				sections[-1]['instructions'][-1]['ingredients'].append([line.lstrip()])
		else: # Instruction
			# Begin a new one with this line as the text
			sections[-1]['instructions'].append({'text': line, 'ingredients': []})
	
	return {'metadata': metadata, 'sections': sections}

if __name__ == '__main__':
	import sys
	from pprint import pprint
	pprint(parserecipe(open(sys.argv[1], 'r')))

