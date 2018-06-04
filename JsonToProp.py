'''
usage: python JsonToProp.py <filename.json>
'''

import json
import sys

with open(sys.argv[1]) as json_labels:
    labels = json.load(json_labels)

    with open(sys.argv[1].split('.')[0] + '.properties', 'a') as properties:
        for key, value in labels.items():
            properties.write(key + '=' + value + '\n')
