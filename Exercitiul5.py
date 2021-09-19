x=[1,2,3,4,5]
y=x.copy()
print(x[0]+x[1]+x[2]) #a
suma=0 #b
for a in range(y[0], (len(y)+1)):
    suma=suma+a
print(suma)
produs=1 #c
for b in range(x[0], (len(x)+1)):
    produs=produs*b
print(produs)
print(abs(x[2])) #d
print(x[0]+y[0]) #e