class Shortner:

    def __init__(self, items):
        self.original_items = items

    def print_original_items(self):
        print(self.original_items)


class ListCharShortner(Shortner):

    def print_shortened_items(self):
        print(self.original_items[0:3])


class DictionaryShortner(Shortner):

    def print_shortened_items(self):
        result_dict = {}
        counter = 1
        dictionary = self.original_items
        for (k, v) in dictionary.items():
            counter += 1
            result_dict.update({k: v})
            if counter > 3:
                break
        print(result_dict)


