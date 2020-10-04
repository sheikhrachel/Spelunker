import os

def destination_matcher(current_dir):
	# Test folder
	try:
	    os.mkdir('test')
	except:
	    pass
	finally:
	    return current_dir + '/test'

def file_maker(file, files):
	filename = 'test_' + file + '.py'
	with open(filename, 'a') as fp: 
		for method in files[file]:
			fp.write('test_' + method)
			fp.write('\n')

def test_generator(test_dir, files):
	os.chdir(test_dir)
	print(os.getcwd())

	for file in files:
		try:
			file_maker(file, files)
		except:
			continue

	# path_parent = os.path.dirname(os.getcwd())
	# os.chdir(path_parent)
