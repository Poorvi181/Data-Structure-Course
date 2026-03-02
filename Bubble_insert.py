mylist = [3,1,2,5,4]

mylist.sort(reverse = True) #Descending Order

print(mylist)

mylist.sort(reverse= False) #Ascending Order

print(mylist)

#Bubble Sort
 
bubblelist= [12,34,2,5,7]

for i in range(0, len(bubblelist)):
    for j in range(i, len(bubblelist)):
        if bubblelist[i] < bubblelist[j]:
            bubblelist[i], bubblelist[j] = bubblelist[j], bubblelist[i]

print(bubblelist)