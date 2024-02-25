#filter out a list of paragraphs from a text file
#look for the paras which have only hindi text of threshold(minimum lines=5 and minimum words per line = 6)
#count the list of paras and decide first, middle and last paras
#storing the paras into a text file
#Reference - https://www.geeksforgeeks.org/reading-writing-text-files-python/

import os
#mention the parent folder
parent_folder = 'txt/'
threshold_for_no_of_lines = 5
threshold_for_no_of_words_per_line = 6

#get list of text files
def get_list_of_text_files_from_parent_folder(parent_folder):
	lstOfFiles = []
	for filename in os.listdir(parent_folder):
    		if filename.endswith('.txt'):
    			lstOfFiles.append(filename)
	return lstOfFiles
    			

#extract list of clean paras from text file
def extract_clean_paras(file_path):
	with open(file_path, 'r') as fp:
		lines = fp.readlines()

		lenOfLines = len(lines)
		lstOfParas = []

		for lineno in range(lenOfLines):      
			para = []
			flag = True  	
			i = 0
				
			while(lines[lineno].strip()):
				i += 1
				lstOfWords = lines[lineno].split()
				if len(lstOfWords) >= threshold_for_no_of_words_per_line:
					para.append(lines[lineno])
				else:
					flag = False
					while(not lines[lineno].strip()):
						lineno += 1
				lineno += 1
			
			if flag and i >= threshold_for_no_of_lines:
				lstOfParas.append(para)
		
	return lstOfParas
		
        	
lstOfFiles = get_list_of_text_files_from_parent_folder(parent_folder)
for _file in lstOfFiles:
	file_path = os.path.join(parent_folder + _file)
	lstOfParas = extract_clean_paras(file_path)
	noOfParas = len(lstOfParas)

	if noOfParas < 3:
		print("Not able to extact first,  middle and last paras from " + file_name + ".txt")
	else:

		first_para = lstOfParas[0]
		middle_para = lstOfParas[int(noOfParas/2)]
		last_para = lstOfParas[noOfParas - 1]


		# writing first, middle and last paras to a text file
		para_file = os.path.basename(file_path)[0:-4] + '_paras'
		with open(f'{para_file}.txt', "w") as fp:
			fp.writelines(first_para)
			fp.write("\n\n")
			fp.writelines(middle_para)
			fp.write("\n\n")
			fp.writelines(last_para)
	
