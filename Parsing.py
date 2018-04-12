#Author - Jayasimha Reddy
stories=open("stories.txt",'w')
for k in range(0,22):
    filename="reut2-"+str(k).zfill(3)+".sgm"
    with open(filename,'r') as f:
        a=f.readlines()
    a=[x.strip() for x in a]
    indices=[]
    count=0
    for line in a:
        count+=1
        if(line.find("<BODY>")!=-1):
            start_line=count-1
        if(line.find("</REUTERS>")==0):
            end_line=count-4
            if(start_line!=-1):
                indices.append([start_line,end_line])
            start_line=-1
    texts=[]
    for i in range(len(indices)):
        text=""
        for j in range(indices[i][0],indices[i][1]+1):
            if(j==indices[i][0]):
                index=a[j].find("<BODY>")+6
                text=text+" "+a[j][index:]
            else:
                text=text+" "+a[j]
        stories.write(text+'\n')
    print len(indices)
        #texts.append(text)
