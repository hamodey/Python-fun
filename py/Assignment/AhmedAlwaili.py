objStr = str(input("Input all your objects: "))
spltStr = objStr.split(" ")
print("Here you can see your objects: ", spltStr)
s0 = str(input("Please describe your initial state: "))
goal = str(input("Input your goal: "))
g0Start = goal.find("on(") + 3
g0End = goal.find(")", g0Start)
g0state = goal[g0Start:g0End]
g0split = g0state.split(",")
g1split = []
copyS0 = []


def toyWorld():
    s0Start = s0.find("on(") + 3
    s0End = s0.find(")", s0Start)
    s0state = s0[s0Start:s0End]
    s0split = s0state.split(",")
    print(s0state)
    s0split[0] #heavier - 0 is heavier than 1
    print(s0split[0], "is on top of", s0split[1])
    copyS0.append(spltStr[0])
    g1split.append(spltStr[1:1])
    
    print(copyS0)
    print(g0split)
#    for i in spltStr:
#       spltStr.remove(i)
#        copyS0.append(i)
#        print("Current state ", spltStr)
#        print("----- Holder list ",copyS0)

def isGoal(node):
    print(g0state)
    if str(node) == goal:
        return True
    else:
        return False
    
def generateChild(t):
    for i in t:
        if isinstance(i, list):
            if len(i) <= 0: #empty list
                print("Empty List")
                return False
            else:
               generateChild(i)
        else:
             anw = isGoal(i)
             if anw:
                 print(i)
                 break

def main():
    toyWorld()
    generateChild(objStr)
    
main()
