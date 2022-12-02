# Part One - what are unknowns
translation_1 = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

# Part Two - what are unknowns
translation_2 = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

#Rock/Paper/Scissors values 
played_points = {
    "A": 1,
    "B": 2,
    "C": 3
}

#Result of match values
result_points = {
    "lose": 0,
    "draw": 3,
    "win": 6
}

# Logic of game
logic = {
    "A": {"loses_to": ["B"], "beats": ["C"]},
    "B": {"loses_to": ["C"], "beats": ["A"]},
    "C": {"loses_to": ["A"], "beats": ["B"]},
}

# Check win/lose/tie
def getResult(mine, opponent):
    result = "win"
    if mine == opponent:
        result = "draw"
    elif opponent in logic[mine]["loses_to"]:
        result = "lose"
    return result_points[result]

# Given desired result and what opponent played, decide what we need to play
def getPlay(res, opp):
    if res == "draw":
        return opp
    elif res == "lose":
        return logic[opp]["beats"][0]
    else:
        return logic[opp]["loses_to"][0]

def main():
    my_score_1 = 0
    my_score_2 = 0
    with open("input.txt") as f:
        for line in f:
            inputs = line.strip().split()
            op = inputs[0]
            me_raw = inputs[1]
            my_play = translation_1[me_raw]
            my_res = translation_2[me_raw]
            # part1 is straightforward, we are told what to play
            my_score_1 += played_points[my_play] + getResult(my_play,op)
            # part2 we have to decide what to play
            my_score_2 += played_points[getPlay(my_res,op)] + result_points[my_res]

    print("Part One: ",my_score_1)
    print("Part Two: ",my_score_2)

if __name__ == "__main__":
    main()
