from xml.dom.minidom import Document
from xml.etree import ElementTree as ET


def export(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    elements = root.find('array/dict/array/dict/array')

    podcasts = []
    for element in elements:
        keyValues = [v.text for v in element]
        iterator = iter(keyValues)
        podcast = dict((k, v) for k, v in zip(iterator, iterator))
        podcasts.append(podcast)

    opml = to_opml(podcasts)
    print(opml.toprettyxml(indent="\t"))

    # TODO save file
    # save_path_file = "gfg.xml"

    # with open(save_path_file, "w") as f:
    #    f.write(xml_str)


def to_opml(podcasts):
    root = Document()

    xml = root.createElement('opml')
    root.appendChild(xml)

    body = root.createElement('body')
    xml.appendChild(body)

    for pod in podcasts:
        outline = root.createElement('outline')
        outline.setAttribute('type', 'rss')
        outline.setAttribute('text', pod['title'])
        outline.setAttribute('xmlUrl', pod['feedUrl'])
        body.appendChild(outline)

    return xml


if __name__ == '__main__':
    # File containing podcasts is located here: ~/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist
    export('/Users/davidandreasson/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist')
