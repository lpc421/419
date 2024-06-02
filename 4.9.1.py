def compare_value(x,y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
    
print(compare_value(3,5))
print(compare_value(5,5))
print(compare_value(5,3))