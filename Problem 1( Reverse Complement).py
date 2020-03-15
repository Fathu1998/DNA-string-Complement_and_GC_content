DNA=input("Enter the DNA sequence")
DNA=DNA.upper()
print(DNA)
D={'A':'T','T':'A','G':'C','C':'G'}
Com=""
S=DNA[::-1]
for i in S:
   Com+=D[i]
print("The reverse complement of the sequence is" ,Com )
