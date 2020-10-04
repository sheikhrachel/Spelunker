from pathlib import Path

def file_reader(file):
	f = open(file, "r")
	filename = Path(file).stem
	temp = []
	request_library_used = False
	spelunker_skip = False

	for line in f.readlines():
		# spelunker_skip to ignore methods
		if 'spelunker_skip' in line:
			spelunker_skip = True
			continue
		if spelunker_skip is True:
			spelunker_skip = False
			continue

		if line is '\n' or line[0] is '#':
			continue
		
		# Only dealing with mocking for the request library at the moment
		if 'request' in line:
			request_library_used = True
		if 'import' not in line and request_library_used is False:
			break

		if 'def' in line:
			temp.append(line[4:-2])

	if len(temp) is 0:
		return

	return filename, temp
