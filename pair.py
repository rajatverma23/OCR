#Read the ith Page from inds folder in var ocr
#Read the ith Page from corrected folder in var corrected
#For jth line in ith page in ocr and kth line in corrected, print ocr j and corrected k and distance between them
#If ocr j is empty, increment j by 1; if corrected k is empty, increment k by 1
#If ocr j and corrected k have distance beyond threshold t then manually modify ocr file to align
#only if required modify corrected file

#importing libraries
import os
import sys
import fileinput

#reading a file and converting the lines into list
def readFile(filename):
	if(os.path.isfile(filename) == False):
		return []
	my_file = open(filename, "r") 
  
	# reading the file 
	data = my_file.read() 
	  
	# replacing end splitting the text  
	# when newline ('\n') is seen. 
	data_into_list = data.split("\n") 
	my_file.close()
	return data_into_list
	

#https://www.geeksforgeeks.org/edit-distance-dp-5/
def editDistance(str1, str2, m, n):
     
    # Initialize a list to store the current row
    curr = [0] * (n + 1)
     
    # Initialize the first row with values from 0 to n
    for j in range(n + 1):
        curr[j] = j
     
    # Initialize a variable to store the previous value
    previous = 0
     
    # Loop through the rows of the dynamic programming matrix
    for i in range(1, m + 1):
        # Store the current value at the beginning of the row
        previous = curr[0]
        curr[0] = i
         
        # Loop through the columns of the dynamic programming matrix
        for j in range(1, n + 1):
            # Store the current value in a temporary variable
            temp = curr[j]
             
            # Check if the characters at the current positions in str1 and str2 are the same
            if str1[i - 1] == str2[j - 1]:
                curr[j] = previous
            else:
                # Update the current cell with the minimum of the three adjacent cells
                curr[j] = 1 + min(previous, curr[j - 1], curr[j])
             
            # Update the previous variable with the temporary value
            previous = temp
     
    # The value in the last cell represents the minimum number of operations
    return curr[n]
    

def removeBlankLineInTextFile(filename):
	

#global variable to start with first page
pageno = 1

#word pairs of two text files	
while(pageno <= int(sys.argv[1])) :
	corrected = readFile('Corrected/page-' + str(pageno) + '.txt')
	ocr = readFile('Inds/page-' + str(pageno) + '.txt')
	
	if(len(corrected) == 0): 
		pageno += 1
		continue
	
	print("Pairing page no - ", pageno)
	
	if(len(ocr) == 0): 
		print('OCR file doesnot exits but corrected file exists for pageno-', pageno)
		break
		
	ol = 0
	cl = 0
	
	while(ol < len(ocr) and cl < len(corrected)):
		cline = corrected[cl].strip()
		oline = ocr[ol].strip()
		
		if(oline == ""):
			ol += 1
			continue
			
		if(cline == ""):
			cl += 1
			continue
					
		print("corrected line ", cl+1, " : " , cline)
		print("ocr line ", ol+1, " : " , oline)
		
		ed = editDistance(cline, oline, len(cline), len(oline))
		print("Edit Distance ", ed)
		ol += 1
		cl += 1
		
	pageno += 1		
			
	
