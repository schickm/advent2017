import sys
from ipdb import launch_ipdb_on_exception, set_trace

input = sys.argv[1]

def word_to_frequency_dict(word):
    d = {}
    for char in word:
        d[char] = d.get(char, 0) + 1

    return d

with launch_ipdb_on_exception():
    valid_count = 0
    with open(input) as f:
        for line in f:
            line = line.rstrip()
            seen_words = []
            valid_phrase = True
            for word in line.split(' '):
                word_dict = word_to_frequency_dict(word)
                if next((obj for obj in seen_words if obj == word_dict), None):
                    valid_phrase = False
                    break
                else:
                    seen_words.append(word_dict)
            if valid_phrase:
                valid_count += 1
                print('VALID: {}'.format(line))
            else:
                print('INVALID: {}'.format(line))

    print(valid_count)

