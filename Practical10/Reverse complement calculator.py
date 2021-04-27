
DNA=input("The DNA sequence is:") #input the DNA sequence
#function: complement+reverse
def RC(DNA):
	duplication={'A':'T','T':'A','C':'G','G':'C'} #dictionary for complement
	n=len(DNA) #length of DNA
	Reverse_complement='' #empty DNA

	for i in range (n,0,-1):
		Reverse_complement+=duplication[DNA[i-1:i]] #reverse
	print('Reverse complement=',Reverse_complement) #print the DNA
	return DNA
RC(DNA)

