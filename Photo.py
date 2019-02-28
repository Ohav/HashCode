class Photo:
    def __init__(self, index, tags):
        self.tags = tags
        self.image_index = index

    def __contains__(self, a):
        return a in self.tags