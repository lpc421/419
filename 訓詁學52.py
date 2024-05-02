sum = 0 
for x in range(1, 101): 
    if x % 2 != 0:
        sum = sum + x 

print(sum) 


sum = 0 
for x in range(1, 101): 
    if x % 2 == 0:
        continue
    sum = sum + x 
            
print(sum) 



sum = 0 
for x in range(1, 101, 2): 
        sum = sum + x 

print(sum) 