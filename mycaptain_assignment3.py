s="mississippi"
fre=[None]*len(s)
char=[]
for i in s:
    char.append(i)
for i in range(0,len(s)):
    fre[i]=1
    for j in range ((i+1),len(s)):
        if char[i]==char[j]:
            fre[i]=fre[i]+1
            char[j]="0"
for i in range(0,len(fre)):
    for j in range((i+1),len(fre)):
        temp=0
        temp1=" "
        if fre[i]<fre[j]:
            temp=fre[i]
            temp1=char[i]
            fre[i]=fre[j]
            char[i]=char[j]
            fre[j]=temp
            char[j]=temp1
            
for i in range(0, len(fre)):
    if char[i]!=""and char[i]!="0":
        print(char[i]+"-"+str(fre[i]))





        
