import re
i=0
lengths=0
lines=''
#initial:0
translation={'TTT':'F', 'TCT':'S', 'TAT':'Y', 'TGT':'C',
'TTC':'F', 'TCC':'S', 'TAC':'Y', 'TGC':'C',
'TTA':'L', 'TCA':'S', 'TAA':'O', 'TGA':'X',
'TTG':'L', 'TCG':'S', 'TAG':'U', 'TGG':'W',

'CTT':'L', 'CCT':'P', 'CAT':'H', 'CGT':'R',
'CTC':'L', 'CCC':'P', 'CAC':'H', 'CGC':'R',
'CTA':'L', 'CCA':'P', 'CAA':'Q', 'CGA':'R',
'CTG':'L', 'CCG':'P', 'CAG':'Z', 'CGG':'R',

'ATT':'I', 'ACT':'T', 'AAT':'N', 'AGT':'S',
'ATC':'I', 'ACC':'T', 'AAC':'B', 'AGC':'S',
'ATA':'J', 'ACA':'T', 'AAA':'K', 'AGA':'R',
'ATG':'M', 'ACG':'T', 'AAG':'K', 'AGG':'R',

'GTT':'V', 'GCT':'A', 'GAT':'D', 'GGT':'G',
'GTC':'V', 'GCC':'A', 'GAC':'D', 'GGC':'G',
'GTA':'V', 'GCA':'A', 'GAA':'E', 'GGA':'G',
'GTG':'V', 'GCG':'A', 'GAG':'E', 'GGG':'G',}
#dictionary:DNA to protein

cDNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
output=open('unknown_function_protein.fa', 'w') #open the input and output file
result='(base) yyaxuan19macrobook 2018 Week 8 % head unknown_function.fa' #the first line of the output file
for line in cDNA: #read the lines in the input file
#	lines+=1 #count the lines
	if re.search(r'^>',line):
		Flag=False #stop assembling
		if len(lines)>0:
			protein='' #empty protein
			for i in range(0,len(lines),3):
                        	protein+=translation[lines[i:i+3]] #translation
			print(protein)
			lengths=len(protein)
			name_lengths=z=' '.join(name+[str(lengths)])
			result+='\n'+ name_lengths+'\n'+ protein
			lines='' #output:name,length, seqeunce
		if 'unknown function' in line:
			name=re.findall(r'gene:([0-9A-Z]+)',line) #find the known function
		#	i+=1 #count protein of unknown function
			Flag=True
	if not re.search(r'^>',line) and Flag==True:
		lines+=line.strip('\n') #assemble the DNAs

#print(result)
#print(i)
#print(lines)
#print
output.write(result)
cDNA.close()
output.close()
#close
