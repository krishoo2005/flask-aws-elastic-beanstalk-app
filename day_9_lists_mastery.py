print("day 9 list mastery") #title

shopping_list = [" flask", "aws",  "autocad", "cloud developer",   "backend develper"]
print(f"shopping list: {shopping_list}")
print(f"\n Number of list :{len(shopping_list)}")  #lenght = number of lst
   

#forloop
print("\n shopping list")
for item in shopping_list:
    print(f"* {item}")
print(f"\n" + "=" * 50)

#add and remove the list
print("add and remove skills\n")
shopping_list.append("github")
print(f"after append github : {shopping_list}\n\n")
shopping_list.remove("autocad")
print(f"after remove autocad : {shopping_list}")

#reverse  list 

print("\nreverse order")
for item in reversed(shopping_list):
    print(f"\n*{item}")



