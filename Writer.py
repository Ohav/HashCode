import datetime

def write(slides, answer_file):
    answer_file = answer_file.split(".")[0]
    now = datetime.datetime.now()
    answer_file += str(now.hour) + ":" + str(now.minute) + ".sol"

    score = 0
    with open(answer_file, "r") as file:
        file.write(str(len(slides)) + "\n")

        for i, slide in enumerate(slides):
            file.write(slide.image_index)
            if slide.other_index != -1:
                file.write(" " + slide.other_index)
            file.write("\n")
            if i + 1 != len(slides):
                score += slide.score(slides[i + 1])
    print(score)