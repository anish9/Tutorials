# merging list
a = [[a,c,v,c,d],[r,w,s,a,s],[100,22,1212,212]]
merged = sum(a,[])

#sorting pairs based on tuple indice
tx = [(1,22),(32,5),(5,3),(8,1)]
out = sorted(tx,key=lambda x:x[1])
print(out) #[(8, 1), (5, 3), (32, 5), (1, 22)]
