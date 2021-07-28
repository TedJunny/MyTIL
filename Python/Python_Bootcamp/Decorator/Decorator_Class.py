class Tagify:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        tagified_p = self.tagify("p", self.function(*args, **kwargs))
        tagified_b = self.tagify("b", tagified_p)
        tagified_i = self.tagify("i", tagified_b)
        return tagified_i

    def tagify(self, tag, text):
        return "<{tag}>{text}</{tag}>".format(tag=tag, text=text)


@Tagify
def set_text(text):
    return text


print(set_text("python"))
