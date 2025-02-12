
file = open('positions.txt')
file2 = open('positions2.txt','w')

mylist=list(file)
line = mylist[0]
line_values = line.split(',')
X0=float(line_values[1])
Y0=float(line_values[2])
Z0=float(line_values[3])

for line in mylist:
  line_values = line.split(',')
  X1=float(line_values[1])
  Y1=float(line_values[2])
  Z1=float(line_values[3])
  X_diff=X1-X0
  Y_diff=Y1-Y0
  nX=int(round((X_diff)/650))
  nY=int(round((Y_diff)/650))
  Z_diff=Z1-Z0
  print(nX,nY,Z_diff)
  file2.write(str(nX)+','+str(nY)+','+str(X_diff)+','+str(Y_diff)+','+str(Z_diff)+','+line)
file2.close()
