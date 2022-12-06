def getStartofPacket(msg,mSize):
    i = mSize
    while i <= len(msg):
        # Set will only have unique characters, look for the first one of mSize
        if len(set(msg[i-mSize:i])) == mSize:
            break
        i += 1
       
    return i

def main():
    inp = "input.txt"
    with open(inp) as f:
        for line in f:
            line = line.strip()
            start1 = getStartofPacket(line,4)
            start2 = getStartofPacket(line,14)
    print("Part One: ",start1)
    print("Part Two: ",start2)
    
if __name__ == "__main__":
    main()
