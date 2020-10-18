
def getFileContent(filePath):
	newFile  = open(filePath, "r")
	return newFile 


def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def parsingJsonFileToYaml():
   # timeFormat = "%H:%M"
    
    jsonFile = getFileContent("Weekday.json")
    
    #getting a list of jsonfile lines
    if jsonFile.mode == "r":
       jsonFiletext = jsonFile.readlines()
    

    #Creating Output file
    outputFile = open("Weekday.yaml", "w")

    lineCount =0
    for line in jsonFiletext:
        lineCount+=1
        if lineCount==1:
            line = line.lstrip(" ")
            line = line.replace("{","---")
            outputFile.write(line)
        elif(lineCount == len(jsonFiletext)):
            line = line.replace("}","")
            outputFile.write(line)
        else:
           
            #validating if is not an object
            if ":{" not in line and ": {" not in line :         

               #Replacing chars, so the syntax matches yaml: 
                line= line.replace("{","-").replace("}\n","").replace("}","").replace("[","").replace("]","").replace("},","").replace(",\n","\n")
                
                tempLine = line.split(": ")  
            #Validating that there's something meaningful after colon(:)
                if len(tempLine)>1:          
                #Removing quotes from left side :    
                    line = tempLine[0].replace("\"","") + " : "+ str(tempLine[1])       
            else:
                tempLine2 = line.strip().split(":")
                line = tempLine2[0].replace("\"","").replace("{","") + ":\n"

            if len(line.lstrip())!=0:
               outputFile.write(line)

def main():
    parsingJsonFileToYaml()
    return 

if __name__ == "__main__":
    main()
    print("End of execution")