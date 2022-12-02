input_values = open("day_2\input.txt")

game_sets = []

rps = {
    "r": 1,
    "p": 2,
    "s": 3
}

lwd = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

score = 0

for value in input_values:
    game_sets.append(value.strip())

input_values.close()

for game in game_sets:
    match game[0]:
        case "A": # rock
            match game[2]:
                case "X": # loss
                    score += lwd["X"]
                    score += rps["s"]
                case "Y": # draw
                    score += lwd["Y"]
                    score += rps["r"]
                case "Z": #win
                    score += lwd["Z"]
                    score += rps["p"]
        case "B": # paper
            match game[2]:
                case "X":
                    score += lwd["X"]
                    score += rps["r"]
                case "Y":
                    score += lwd["Y"]
                    score += rps["p"]
                case "Z":
                    score += lwd["Z"]
                    score += rps["s"]
        case "C": # scissors
            match game[2]:
                case "X":
                    score += lwd["X"]
                    score += rps["p"]
                case "Y":
                    score += lwd["Y"]
                    score += rps["s"]
                case "Z":
                    score += lwd["Z"]
                    score += rps["r"]

print(score)