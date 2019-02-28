class Photo:
    def __init__(self, index, tags, vertical):
        self.tags = tags  # a set
        self.image_index = index
        self.vertical = vertical
        self.is_taken = False

    def __contains__(self, a):
        return a in self.tags

    def __len__(self):
        return len(self.tags)

    def score(self, other):
        common_tags = self.tags & other.tags
        self_tags = self.tags - common_tags
        other_tags = other.tags - common_tags
        return min(len(common_tags), len(self_tags), len(other_tags))

