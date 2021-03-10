#compare ages
a=060202
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
print("d="+str(d))
print("e="+str(e))
if d>e:
  print("d>e")
else:
  print("d<e")


#I don't know why we should submit two tasks in only one files.I mean it is confusing to full this file with the file"Booleans.py".


#equal or not:Booleans.py
X=True
Y=True
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
print("first round:")
print("X="+str(X))
print("Y="+str(Y))
print("Z="+str(Z))
print("W="+str(W))
if Z==W:
  print("Z=W")
else:
  print("Z!=W")



X=False
Y=True
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
print("Second round:")
print("X="+str(X))
print("Y="+str(Y))
print("Z="+str(Z))
print("W="+str(W))
if Z==W:
  print("Z=W")
else:
  print("Z!=W")



X=False
Y=True
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
print("third round:")
print("X="+str(X))
print("Y="+str(Y))
print("Z="+str(Z))
print("W="+str(W))
if Z==W:
  print("Z=W")
else:
  print("Z!=W")


X=False
Y=False
Z=(X and not Y) or (Y and not X)
W=(X!=Y)
print("forth round:")
print("X="+str(X))
print("forth round:")
print("X="+str(X))
print("Y="+str(Y))
print("Z="+str(Z))
print("W="+str(W))
if Z==W:
  print("Z=W")
else:
  print("Z!=W")







