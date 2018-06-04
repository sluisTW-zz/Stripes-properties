'''
usage: python PropToJson.py <filename.properties>
'''

import json
import sys

def load_properties(filepath, sep='=', comment_char='#'):
    """
    Read the file passed as parameter as a properties file.
    Found at:
    https://stackoverflow.com/a/31852401
    """
    props = {}
    with open(filepath, "rt") as f:
        for line in f:
            l = line.strip()
            if l and not l.startswith(comment_char):
                key_value = l.split(sep)
                key = key_value[0].strip()
                value = sep.join(key_value[1:]).strip().strip('"')
                props[key] = value
    return props

labels_dictionary = load_properties(sys.argv[1])
with open(sys.argv[1].split('.')[0] + '.json', 'a') as json_file:
    json_file.write(json.dumps(labels_dictionary, indent=2))
