from Photo import Photo

class Writer:
    @staticmethod
    def write(slides, answer_file):
        with open(answer_file, "r") as file:
            file.write(str(len(slides)) + "\n")

            for slide in slides:
                file.write(slide.image_index)
                if slide.other_index != -1:
                    file.write(" " + slide.other_index)
                file.write("\n")
