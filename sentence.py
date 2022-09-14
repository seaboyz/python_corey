class Sentence:
    def __init__(self, sentence):
        self.list = sentence.split(' ')
        self.current_index = 0
        self.length = len(self.list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.length
        raise StopIteration
        self.current_index += 1
        return self.list[self.current_index]
