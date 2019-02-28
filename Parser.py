import re
import sys
import Logic
from Photo import Photo


class Parser:
    @staticmethod
    def parse_file(file_name):
        pictures = []
        photo_index = 0
        tag_dictionary = dict()
        with open(file_name, 'r') as file:
            pic_num = file.readline()
            for line in file:
                picture_data = line.split()
                is_vertical = True if picture_data[0] == 'V' else False
                photo_tags = picture_data[2:]
                cur_picture = Photo(photo_index, photo_tags, is_vertical)
                pictures.append(cur_picture)
                photo_index += 1
                for tag in photo_tags:
                    if tag in tag_dictionary:
                        tag_dictionary[tag].append(cur_picture)
                    else:
                        tag_dictionary[tag] = [cur_picture]

                if is_vertical:
                    if 'V' in tag_dictionary:
                        tag_dictionary['V'].append(cur_picture)
                    else:
                        tag_dictionary['V'] = [cur_picture]

        return pictures, tag_dictionary


if __name__ == '__main__':
    photos, photo_dict = Parser.parse_file(sys.argv[1])
    CodeLogic = Logic.Logic()
    CodeLogic.main(photo_dict, photos)
