import os

Reference = open('Reference','r')

ReferenceToSort=[]
for line in Reference:
    ReferenceToSort.append(line.split())
#print(ReferenceToSort)


SortedReference = sorted(ReferenceToSort,key=lambda x: x[0])
print(SortedReference)

Reference.close()

#print(len(SortedReference))


if(1):
    os.mknod("SortedReferenceDissertation.txt")  # mknod create a new file
    f = open('SortedReferenceDissertation.txt', 'w')
    for line in SortedReference:
        strReference = " ".join(line)
        f.write(strReference+'\n')
