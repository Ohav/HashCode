import re
import sys
import Logic
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

        return cur_photo, tag_dictionary


if __name__ == '__main__':
    photos, photo_dict = Parser.parse_file(sys.argv[1])
    CodeLogic = Logic.Logic()
    CodeLogic.main(photo_dict, photos)
