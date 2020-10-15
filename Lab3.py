import sys 
import math
import os
import datetime


def toNumericValue(string):
    convertedNumber = 0
    for i in string:  
        convertedNumber = convertedNumber * 10 + (ord(i) - 48)    
    return convertedNumber  
  

def getFileContent(filePath):
	inputFile  = open(filePath, "r")
	return inputFile 



def main():
	inputFile = getFileContent("InputFile.txt")
	



	#Spliting Input file by NewLine Char
	if inputFile.mode == "r":
		fileRowList = inputFile.read().split("\n")

	#Creating date format, and sorting Row list by the column at index 2 (Birthday)
	format = "%d.%m.%Y"
	fileRowList.sort(key=lambda line: datetime.datetime.strptime(line.split(" ")[2],format)) 

	
	

	#Creating Output file, removing old if exists
	if os.path.isfile("OutputFile.txt"):
		os.remove("OutputFile.txt")
	outputFile = open("OutputFile.txt", "a")
	


	for i in fileRowList:
		fileRow= i.split(" ")

		if len(fileRow)>1:

			#Calculating Average of the 3 scores

			fileRow.append(str( (toNumericValue(fileRow[4]) + toNumericValue(fileRow[5]) + toNumericValue(fileRow[6]) )/3 ))
			
			#Printing Content before writing
			print(fileRow)
		
			outputFile.write(fileRow[0]+" "+ fileRow[1] + "|"+ 
							fileRow[2] + "|"+ fileRow[3] + "|"+ 
							fileRow[4] + " " + fileRow[5] + " " +
							fileRow[6] +" -> " +fileRow[7]+ "\n" )  	


if __name__ == "__main__":
	main()




	
#outputFile.write(items[0]+" "+ items[1] + "|"+ items[2] + "|"+ items[3] + "|"+ items[4] + " " + items[5] + " " + items[6]+" -> \n")