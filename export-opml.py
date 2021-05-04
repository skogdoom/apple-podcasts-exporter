import xml.dom.minidom
import xml.etree.ElementTree as ET


def export(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    elements = root.find('array/dict/array/dict/array')

    podcasts = []
    for element in elements:
        keyValues = [v.text for v in element]
        iterator = iter(keyValues)
        podcast = [(k, v) for k, v in zip(iterator, iterator)]
        podcasts.append(podcast)

    print(len(podcasts))


if __name__ == '__main__':
    # File containing podcasts is located here: ~/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist
    export('/Users/davidandreasson/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist')
