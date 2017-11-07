tree1 = input("Enter your objects: ")
tree = tree1.split(" ")
print(tree)

goal = input("Please enter your goal: ")
def isGoal(node):
    if str(node) == goal:
        return True
    else:
        return False

    #return True if node == goal else return False 

def generateChildren(t):
    for i in t:
        if isinstance(i, list):
            if len(i) <= 0: #empty list
                print("Empty List")
                return False
            else:
               generateChildren(i)
        else:
             anw = isGoal(i)
             if anw:
                 print(i)
                 break

generateChildren(tree)
