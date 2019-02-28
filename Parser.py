import re
import sys
import Logic
import Writer
import os
from Photo import Photo


class Parser:
    @staticmethod
    def parse_file(file_name):
        photos = []
        photo_index = 0
        tag_dictionary = dict()
        with open(file_name, 'r') as file:
            photo_num = file.readline()
            for line in file:
                picture_data = line.split()
                is_vertical = True if picture_data[0] == 'V' else False
                photo_tags = picture_data[2:]
                cur_photo = Photo(photo_index, set(photo_tags), is_vertical)
                photos.append(cur_photo)
                photo_index += 1
                for tag in photo_tags:
                    if tag in tag_dictionary:
                        tag_dictionary[tag].append(cur_photo)
                    else:
                        tag_dictionary[tag] = [cur_photo]

                if is_vertical:
                    photo_tags.append('V')

                for tag in photo_tags:
                    if tag in tag_dictionary:
                        tag_dictionary[tag].append(cur_photo)
                    else:
                        tag_dictionary[tag] = [cur_photo]

        return photos, tag_dictionary


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: Parser <input>")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("Invalid file given: " + sys.argv[1])

    print("Start parsing.. ")
    photos, photo_dict = Parser.parse_file(sys.argv[1])
    print("OK")
    CodeLogic = Logic.Logic()
    print("Started Logic")
    presentation = CodeLogic.main(photo_dict, photos)
    print("OK")
    Writer.write(presentation, sys.argv[1] + '.sol')
    print("Done")