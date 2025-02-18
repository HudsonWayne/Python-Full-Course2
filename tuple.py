#Tuple = collection which is ordered and unchangeable
            #used to group together related data
            
student = ("wayne",25,"male")     

print(student.count("wayne"))     
print(student.index("male"))

for x in student:
    print(x)
    
if "Bro" in student:
    print("Bro is in the tuple")