import re
i=0
lines=0
lengths=0
#initial:0
cDNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output=open('unknown_function.fa', 'w') #open the input and output file
result='(base) yyaxuan19macrobook 2018 Week 8 % head unknown_function.fa' #the first line of the output file
for line in cDNA: #read the lines in the input file
	#lines+=1 #count the lines
	if re.search(r'^>',line):
		Flag=False #stop counting
		if lengths>0:
			name_lengths=z=' '.join(name+[str(lengths)])
			result+='\n'+ name_lengths
			lengths=0 #add the lengths to the new file

		if 'unknown function' in line:
			name=re.findall(r'gene:([0-9A-Z]+)',line)
			#find the known function
			i+=1 #count protein of unknown function
			Flag=True
	if not re.search(r'^>',line) and Flag==True:
		length=len(line)
		lengths+=length #count the length

#print(result)
#print(i)
#print(lines)
#print
output.write(result)
cDNA.close()
output.close()
#close
