DNA=input("Enter the DNA sequence/sequences")
G=C=0
for i in DNA:
    if i=="G":
        G=G+1
    if i=="C":
        C=C+1
GC_percent=(G+C)*100/len(DNA)
print("The GC% of the given DNA sequence is calculated to be" ,GC_percent)

    
   
    
 
