# put your code here.

def count_words(filename):

    data = open(filename)

    dict_words = {}

    for line in data:

        words = line.split(' ')

        for word in words:
            
            dict_words[word] = dict_words.get(word, 0) + 1

    return dict_words

print(count_words('test.txt'))
print(count_words('twain.txt'))