t=[10.8,10.5,10,10.4,10.7,11,11,10.8,11,12,13,14,14.3,14.7,15,14.6,14.5,14,13,12,11,10.7,10.8,11]
print("Temperatura medie:", sum(t)/24) #a
print("Minimul:", min(t)) #b
print("Maximul:", max(t))
print("Temperatura maxima a fost inregistrata la ora", t.index(max(t))+1) #c
print("Temperatura minima a fost inregistrata la ora", t.index(min(t))+1) #d