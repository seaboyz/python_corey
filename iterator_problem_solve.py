class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.words = sentence.split(' ')
        self.current_index = 0
        self.length = len(self.words)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.length:
            raise StopIteration
        current_word = self.words[self.current_index]
        self.current_index += 1
        return current_word


def sentence(sentence):
    for word in sentence.split():
        yield word


# my_sentence = Sentence('This is a test')
my_sentence = sentence("This is a test")

# for word in my_sentence:
#     print(word)

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
