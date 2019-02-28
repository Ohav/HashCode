import math
from Photo import *


class Logic:
    def main(self, photo_dict, photos):
        photo_count = len(photos)
        current = photos[0]
        presentation = [current]
        while photo_count:
            next_p = self.get_next(photo_dict, photos, current)
            if not next_p:
                next_p = self.find_any_photo(photos)

            next_p.is_taken = True
            current = next_p
            if current.vertical:
                photo_count -= 1
            photo_count -= 1
            presentation.append(current)

        return presentation

    def get_next(self, photo_dict, start):
        max_photo = None
        max_score = -1
        for tag in start.tags:
            for photo in photo_dict[tag]:
                # Preparing the photo
                if photo.is_taken:
                    continue
                if photo.vertical:
                    real_photo = self.find_companion(photo, photo_dict)  # Verticals are merged
                    if not real_photo:
                        continue
                else:
                    real_photo = photo

                # Calculating the score of the photo
                score = start.score(real_photo)
                if score == len(start) - 1 == len(real_photo) - 1:
                    return real_photo
                secondary_score = min(abs(len(start) - score), abs(len(real_photo) - score))
                if max_score <= secondary_score:
                    max_score = secondary_score
                    max_photo = real_photo

        return max_photo

    def find_any_photo(self, photos):
        for photo in photos:
            if not photo.is_taken:
                return photo

    def find_companion(self, candidate, photo_dict):
        max_common = -1
        max_photo = None
        for photo in photo_dict['vertical']:
            if not photo.is_taken:
                common = len(candidate.tags & photo.tags)
                if common > max_common:
                    max_photo = photo
                    max_common = common
        if not max_photo:
            return None
        candidate.merge(max_photo)
        return candidate



