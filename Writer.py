import datetime


def write(slides, answer_file):
    answer_file = answer_file.split(".")[0]
    now = datetime.datetime.now()
    answer_file += str(now.hour) + ":" + str(now.minute) + ".sol"

    score = 0
    with open(answer_file, "w") as file:
        file.write(str(len(slides)) + "\n")

        for i, slide in enumerate(slides):
            file.write(str(slide.image_index))
            if slide.other_index != -1:
                file.write(" " + str(slide.other_index))

            # checks vertical 2 in slide and horizontal 1 in slide
            if slide.vertical and slide.other_index == -1:
                print("vertical alone in slide" + str(i))
            elif not slide.vertical and slide.other_index != -1:
                print("horizontal not alone in slide" + str(i))

            file.write("\n")
            if i + 1 != len(slides):
                score += slide.score(slides[i + 1])
    print(score)