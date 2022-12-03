# Given a common letter, return its value. Use ASCII value for quickmaths
def getVal(comm):
    sub = 96
    if comm == comm.upper():
        sub = 38
    # ASCII value needs a different offset for upper/lowercase
    return ord(comm) - sub

def part1():
    sum = 0
    with open("input.txt") as f:
        for line in f:
            line = line.split()[0]
            # Split the line into two halves, convert to sets
            comp1 = set(line[:len(line)//2])
            comp2 = set(line[len(line)//2:])
            # Return the AND of both to find reoccuring element
            common = list(comp1 & comp2)[0]
            sum += getVal(common)
    print("Part One: ", sum)

def part2():
    sum = 0
    temp = []
    counter = 0
    with open("input.txt") as f:
        for line in f:
            line = line.split()[0]
            temp.append(set(line))
            counter += 1
            # When we have three lines, find the common letter
            if counter == 3:
                common = temp[0]
                for l in temp:
                    common = common & l
                common = list(common)[0]
                sum += getVal(common)
                # reset some vars
                temp = []
                counter = 0
    print("Part Two: ", sum)

# Parts One and Two as they would be in one function
def allTogetherNow():
    sum1,sum2,counter = 0,0,0
    temp = []
    with open("input.txt") as f:
        for line in f:
            line = line.split()[0]
            temp.append(set(line))
            comp1 = set(line[:len(line)//2])
            comp2 = set(line[len(line)//2:])
            common = list(comp1 & comp2)[0]
            sum1 += getVal(common)
            counter += 1
            if counter == 3:
                common = temp[0]
                for l in temp:
                    common = common & l
                common = list(common)[0]
                sum2 += getVal(common)
                temp = []
                counter = 0
    print("Part One: ", sum1)
    print("Part Two: ", sum2)

def main():
    #part1()
    #part2()
    allTogetherNow()

if __name__ == "__main__":
    main()
