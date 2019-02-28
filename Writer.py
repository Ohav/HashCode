import datetime

import os

def write(slides, answer_file):
    score = 0
    answer_file += '.sol'
    with open(answer_file, "w+") as file:
        print ("Writing..")
        file.write(str(len(slides)) + "\n")
        print("WR")
        for i, slide in enumerate(slides):
            print(i)
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
    print("Score: " + str(score))