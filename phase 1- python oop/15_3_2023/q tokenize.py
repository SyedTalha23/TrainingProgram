sentences=["a new world record was set","in the holy city of ayodhya","on the eve of divali on tuesday","with over three lakh diya or earthen lamps","lit up simultaneously on the banks of the sarayu river"]
stopwords=["for","a","of","the","and","to","in","on","with","was"]
l=[]
for i in sentences:
    temp=list(i.split())
    for j in temp:
        l.append(j)
print(l)
for i in stopwords:
    for j in l:
        if i==j:
            l.remove(i)
print(l)