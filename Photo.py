import sys

class Photo:
    def __init__(self, index, tags, vertical, other_index=-1):
        self.tags = tags  # a set
        self.image_index = index
        self.other_index = other_index
        self.vertical = vertical
        self.is_taken = False
        self.sons = (None, None)

    def __contains__(self, a):
        return a in self.tags

    def __len__(self):
        return len(self.tags)

    def score(self, other):
        common_tags = self.tags & other.tags
        self_tags = self.tags - common_tags
        other_tags = other.tags - common_tags
        return min(len(common_tags), len(self_tags), len(other_tags))

    def merge(self, other):
        if not self.vertical or not other.vertical:
            sys.exit("We fucked up")
        new_photo = Photo(self.image_index, self.tags | other.tags, self.vertical,
                          other.image_index)
        new_photo.sons = self, other
        return new_photo

    def take(self):
        self.is_taken = True
        if self.sons[0]:
            for son in self.sons:
                son.take()
