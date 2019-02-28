from Photo import Photo


def write_presentation(slides, answer_file):
    with open(answer_file, "w") as file:
        file.write(str(len(slides)) + "\n")

        for slide in slides:
            file.write(str(slide.image_index))
            if slide.other_index != -1:
                file.write(" " + str(slide.other_index))
            file.write("\n")
