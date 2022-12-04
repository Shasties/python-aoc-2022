def getOverlap(s1,e1,s2,e2):
    x = range(s1,e1+1)
    y = range(s2,e2+1)
    xs = set(x)
    return xs.intersection(y)

def main():
    full_overlaps, part_overlaps = 0,0
    with open("input.txt") as f:
        for line in f:
            simp = line.strip().split(",")
            e1 = simp[0]
            e2 = simp[1]
            e1_start = int(e1.split("-")[0])
            e1_end = int(e1.split("-")[1])
            e2_start = int(e2.split("-")[0])
            e2_end = int(e2.split("-")[1])
            overlap = getOverlap(e1_start,e1_end,e2_start,e2_end)
            if len(overlap) > 0:
                part_overlaps += 1
                if len(overlap) == len(range(e1_start,e1_end+1)) or len(overlap) == len(range(e2_start,e2_end+1)):
                    full_overlaps += 1
    print("Part One: ", full_overlaps)
    print("Part Two: ", part_overlaps)
            
if __name__ == "__main__":
    main()