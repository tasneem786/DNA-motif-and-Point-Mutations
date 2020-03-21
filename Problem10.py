s=input("enter: ")
t=input("enter: ")
count=0
for i in range (len(s)-len(t)+1):
 if t==s[i:len(t)+i]:
  print (i)
  count+=1
print ("COUNT",count)
