import nltk
import ast
import re
import array as arr;

f = open('C:\\lab_assessment\\marks.py', 'r')
program = f.read()
count = 0
    
#print(ast.dump(tree))
#print(ast.iter_fields(tree))
slice = input("Enter the slice criteria")
x = slice.split(",")
var_value = x[0]
endline = x[1]

global Identifiers_Output

Final_Slice =[]
Identifiers_Output = []
Keywords_Output = []
Symbols_Output = []
Conditionals_Output= []
Operators_Output = []
Numerals_Output = []
Headers_Output = []
Variable_Output = []
val = []
global Main_Program
Main_Program=[]



def remove_Comments(program):
    program_Multi_Comments_Removed = re.sub("/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", program)
    program_Single_Comments_Removed = re.sub("#.*", "", program_Multi_Comments_Removed)
    program_Comments_removed = program_Single_Comments_Removed
    return program_Comments_removed



RE_Keywords = "auto|break|case|char|const|continue|def|default|double|enum|write|end|extern|float|goto|int|long|register|return|short|signed|sizeof|static|struct|typedef|union|unsigned|void|volatile|string|class|main|struc|include|print|import"
RE_Conditionals = "if|else|elif|while|do|for"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
#use [a-z][0-9][a-z][0-9] for varname with a mandatory combination of num and char
RE_Variable = "^[a-zA-Z_$][0-9]*$"
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"
RE_Headers = "(?m)^(?:from[ ]+(\S+)[ ]+)?import[ ]+(\S+)[ ]*$"


program_Comments_removed = remove_Comments(program)
prog = program_Comments_removed.split('\n')


#scanned_Prog = remove_Spaces(prog)

#scanned_Program = '\n'.join([str(elem) for elem in scanned_Prog])



#scanned_Program_lines = scanned_Program.split('\n')
match_counter = 0


Source_Code=[]
for line in prog:
        Source_Code.append(line)    
        Main_Program.append([line,len(re.findall("^ *", line)[0])])

#print(Main_Program)
     
display_counter = 0
c=1
for line in Source_Code:
    count = count + 1
    #print("The line no",count," is ",line)
    if(line.startswith("import")):
        print(line)
        tokens = nltk.word_tokenize(line)
    else:
        tokens = nltk.wordpunct_tokenize(line)
        #print("The line",c," is ",line)
        #print("Token ",c," values are :",tokens)
    for token in tokens:
        codeline = str(Main_Program[c-1])
        if(re.findall(RE_Keywords, token)):
            Keywords_Output.append([c,token])
        elif (re.findall(RE_Conditionals, token)):
            Conditionals_Output.append([c,token])
        elif(re.findall(RE_Headers,token)):
            Headers_Output.append([c,token])
        elif(re.findall(RE_Operators, token)):
            Operators_Output.append([c,token])
        elif(re.findall(RE_Numerals,token)):
            Numerals_Output.append([c,token])
        elif (re.findall(RE_Special_Characters, token)):
            Symbols_Output.append([c,token])
        elif (re.findall(RE_Identifiers, token)):
            print("The codeline is ",str(Main_Program[c-1][0]))
            if(codeline.find('=')>=0):
                if("for" in codeline or "if" in codeline or "while" in codeline or "do" in codeline):
                    Identifiers_Output.append([c,token,"loop"])  
                elif(codeline.index(token)< codeline.index('=')): 
                    Identifiers_Output.append([c,token,"defined"])
                else:
                    Identifiers_Output.append([c,token,"used"])       
            elif("read" in str(Main_Program[c-1][0])):
                Identifiers_Output.append([c,token,"defined"])
            else:
                Identifiers_Output.append([c,token,""])            
        elif (re.findall(RE_Variable, token)):
            Variable_Output.append([c,token])    
    c=c+1   

temp = []
Final_Slice.append(int(endline.strip()))
print(Identifiers_Output)
#print(Identifiers_Output)

#getting the variables used on the prog line numbers in Final slice
def get_Variables(Slice):
    global Final_Slice
    temp.clear()
    c=0
    for i in range(len(Slice)-1, -1, -1):
        for k in range(len(Identifiers_Output)-1, -1, -1):  
            if(Identifiers_Output[k][0]==Slice[i] and Identifiers_Output[k][2]in['used','','loop']):
                temp.append(Identifiers_Output[k][1])
                c=c+1
   
        #print("temp values :",temp)
        #print("Final vals:", Final_Slice)
    if(c>0):        
        get_FinalSlice(temp)
        

#getting the program line numbers to be included in final slice
def get_FinalSlice(temp):
    global Final_Slice
    c=0
    for i in range(len(temp)-1, -1, -1): 
        maxi=0
        for k in range(len(Identifiers_Output)-1, -1, -1):  
            if(Identifiers_Output[k][1]==temp[i] and Identifiers_Output[k][0]<=int(endline)):
                if(Identifiers_Output[k][2] =='defined'):
                    Final_Slice.append(Identifiers_Output[k][0])
                    if(maxi<Identifiers_Output[k][0]):
                        maxi = Identifiers_Output[k][0]
                    Final_Slice.append(maxi)
                    val.append(maxi)
                    c=c+1
                    Final_Slice = list(dict.fromkeys(Final_Slice))    
    #print(temp)
    #print(Final_Slice) 
    #print("new values:",val)
    if(c>0):
        #print(Final_Slice) 
        Final_Slice = list(dict.fromkeys(Final_Slice))  
        get_Variables(val)
                       
                
def check_Indentation():
    global Final_Slice
    global Main_Program
    c=0
    for sliceno in Final_Slice:
        indent = Main_Program[int(sliceno)-1][1]
        if(indent>0): 
            for k in range(len(Conditionals_Output)-1, -1, -1):
                linenum = Conditionals_Output[k][0]
                if(linenum<sliceno and int(Main_Program[linenum-1][1])<indent):     
                    if(Conditionals_Output[k][0] not in Final_Slice):
                        Final_Slice.append(Conditionals_Output[k][0]) 
                        c=c+1
    Final_Slice = list(dict.fromkeys(Final_Slice))
    if(c>0):
        check_Indentation()          
        
#print the program lines for the line numbers saved in final slice
def print_Slice():
    global Final_Slice
    Final_Slice = list(dict.fromkeys(Final_Slice))
    Final_Slice.sort()
    print("Final Slice values are :", Final_Slice)
    print("\n\n ******Final Slice******")
    for i in Final_Slice:
        print(str(Main_Program[i-1][0]),"\n")
        

#get the variables used in the program line numbers returned by get_Finalslice saved to temp
get_Variables(Final_Slice)

check_Indentation()
  
print_Slice()



"""
#adding indirects vars to temp list
for i in range(len(Identifiers_Output)-1, -1, -1): 
    for k in range(len(Final_Slice)-1, -1, -1):  
        if(Identifiers_Output[i][0]==Final_Slice[k]):
            temp.append(Identifiers_Output[i][1])    
temp = list(dict.fromkeys(temp))

#getting the final slice by adding the line numbers of all indirect vars
get_Finalslice(temp, Final_Slice)

#writing the final program slice into a file
f = open("finalfile.txt", "w")
line_no=1;
for line in scanned_Program_lines:
    if line_no in Final_Slice:
        print("line no=",line_no,"line=",line)
        Source_Code.append("\n"+line)
    else:   
        continue
    line_no = line_no + 1
f.close()    


print("There Are ",len(Keywords_Output),"Keywords: ",Keywords_Output)
print("\n")
print("There Are ",len(Identifiers_Output),"Identifiers: ",Identifiers_Output)
print("\n")
print("There Are ",len(Headers_Output),"Header Files: ",Headers_Output)
print("\n")
print("There Are",len(Symbols_Output),"Symbols:",Symbols_Output)
print("\n")
print("There Are ",len(Numerals_Output),"Numerals:",Numerals_Output)
print("\n")
print("There Are ",len(Variable_Output),"Variables:",Variable_Output)
print("\n")
print("There Are",len(Operators_Output),"Operators:",Operators_Output)
"""