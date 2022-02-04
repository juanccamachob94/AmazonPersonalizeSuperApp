class StringHelper:
    @classmethod
    def last_substring(cls, text, separator):
        array = text.split(separator)
        return array[len(array) - 1]


    @classmethod
    def first_string(cls, text, separator):
        return text.split(separator)[0]
