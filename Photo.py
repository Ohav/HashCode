class Photo:
    def __init__(self, index, tags, v_or_h):
        self.tags = tags # a set
        self.image_index = index
        self.v_or_h = v_or_h
        self.is_taken = False

    def __contains__(self, a):
        return a in self.tags

    def __len__(self):
        return len(self.tags)

    def score(self, other):
        common_tags = self.tags & other.tags
        self_tags = self.tags - common_tags
        other_tags = other.tags - common_tags
        return min(common_tags, self_tags, other_tags)

