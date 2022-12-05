def printTops(stacks):
    temp = []
    for s in stacks:
        temp.append(s[-1])
    print("Top of each stack is: ","".join(temp))

# Use ASCII value to determine if char is part of alphabet
def isLetter(char):
    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
        return True
    return False

# Parse commands for values
def readCommands(line):
    temp = line.split(" ")
    return int(temp[1]), int(temp[3]), int(temp[5]) # amount, from, destination

# Remove amt of elements from the end of src
# Append these to the end of dest
# If part one, items are moved in reverse order
def moveItems(stacks,amt,src,dest,p1=True):
    moving = stacks[src][0-amt:]
    if p1:
        moving = reversed(moving)
    size = len(stacks[src])
    stacks[src] = stacks[src][0:size-amt]
    stacks[dest].extend(moving)

def main():
    state = 0
    stacks = []
    with open("input.txt") as f:
        for line in f:
            if len(line) == 1: # Keep track of where we are in input for parsing
                state = 1
                continue

            if state == 0: # creating stacks
                if stacks == []: # init
                    stacks = [[] for i in range(len(line)//4)]
                # Assume item is a letter in every x%4==1 spot
                for i in range(len(line)):
                    if i%4 == 1:
                        if isLetter(line[i]):
                            stacks[i//4].insert(0,line[i])
                        
            elif state == 1: # reading commands
                amt,frm,dest = readCommands(line)
                moveItems(stacks,amt,frm-1,dest-1,p1=False)
            else:
                print("bad state")
    printTops(stacks)

if __name__ == "__main__":
    main()
