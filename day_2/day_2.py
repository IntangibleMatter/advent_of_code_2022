input_values = open("day_2\input.txt")

game_sets = []

rps = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

lwd = {
    "l": 0,
    "w": 6,
    "d": 3
}

score = 0

for value in input_values:
    game_sets.append(value.strip())

input_values.close()

for game in game_sets:
    match game[0]:
        case "A":
            match game[2]:
                case "X":
                    score += rps["X"]# rock
                    score += lwd["d"]
                case "Y":
                    score += rps["Y"]
                    score += lwd["w"]
                case "Z":
                    score += rps["Z"]
                    score += lwd["l"]
        case "B":
            match game[2]:
                case "X":
                    score += rps["X"]# rock
                    score += lwd["l"]
                case "Y":
                    score += rps["Y"]
                    score += lwd["d"]
                case "Z":
                    score += rps["Z"]
                    score += lwd["w"]
        case "C":
            match game[2]:
                case "X":
                    score += rps["X"]# rock
                    score += lwd["w"]
                case "Y":
                    score += rps["Y"]
                    score += lwd["l"]
                case "Z":
                    score += rps["Z"]
                    score += lwd["d"]

print(score)