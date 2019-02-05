#Sequence A077947
#The digital roots of the terms of this sequence repeat in the pattern (1,1,2,5,9,9). 

a=1
b=1
c=2
d=5
e=9
f=18
for x in range(0,100):
  print(a)
  a = a+(36*64**x)
  print(b)
  b = b+(72*64**x)
  print(c)
  c = c+(144*64**x)
  print(d)
  d = d+(288*64**x)
  print(e)
  e = e+(576*64**x)
  print(f)
  f = f+(1152*64**x)

