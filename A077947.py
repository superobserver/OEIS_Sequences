#Sequence A077947
#The digital roots of the terms of this sequence repeat in the pattern (1,1,2,5,9,9). 

a=1
b=1
c=2
d=5
e=9
f=18
for x in range(0,100):
  print(a,b,c,d,e,f)
  a = a+(36*64**x)
  b = b+(72*64**x)
  c = c+(144*64**x)
  d = d+(288*64**x)
  e = e+(576*64**x)
  f = f+(1152*64**x)

