def main():
    sums = []
    curr = 0
    with open("input.txt") as f:
        for line in f:
            if line == "\n":
                sums.append(curr)
                curr = 0
            else:
                curr += int(line.strip())
    sums.sort()
    print("Part One: ", sums[-1])
    print("Part Two: ", sum(sums[-3:]))

if __name__ == "__main__":
    main()
