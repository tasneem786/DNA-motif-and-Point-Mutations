a = input ("enter :")
b = input ("enter :")
hamming_count = 0
if len(a)==len(b):
 for i in range (len(a)):
  if a[i] != b [i]:
   hamming_count +=1
print (hamming_count)
