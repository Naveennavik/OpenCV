import glob

folder = '/home/drive/Downloads/zav2/HumanMultiView/sample_data/04/'

filenames = glob.glob(folder + '*.jpg')

filenames.sort()

output = 'python -m demo --img_paths '

for i in range(len(filenames)):

	if i != len(filenames) - 1:
		output = output + '.' + filenames[i][41:] + ','
	else:
		output = output + '.' + filenames[i][41:] 

print(output)