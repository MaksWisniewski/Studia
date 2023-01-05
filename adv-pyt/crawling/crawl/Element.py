class Element():

    def __init__(self, url, depth, max_depth):
        self.url   = url
        self.depth = depth
        self.max_depth = max_depth

    def get_url(self):
        return self.url

    def get_depth(self):
        return self.depth

    # def isValid(self):
    #     return self.depth in range(0, self.max_depth)

    def isValid(self):
        return self.depth >= 0 and self.depth < self.max_depth