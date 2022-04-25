def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1

    return d
                
s="mississippi"
s1=s[-1::-1]
print (most_frequent(s1))
