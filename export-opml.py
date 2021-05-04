from xml.dom.minidom import Document
from xml.etree import ElementTree as ET


def save_file(out_filename, xml_str):
    with open(out_filename, "w") as f:
        f.write(xml_str)


def export(in_filename, out_filename):
    podcasts = parse_plist(in_filename)
    opml = to_opml(podcasts)
    save_file(out_filename, opml.toprettyxml(indent="\t"))


def parse_plist(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    elements = root.find('array/dict/array/dict/array')
    podcasts = []
    for element in elements:
        keyValues = [v.text for v in element]
        iterator = iter(keyValues)
        podcast = dict((k, v) for k, v in zip(iterator, iterator))
        podcasts.append(podcast)
    return podcasts


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
    export(
        '/Users/davidandreasson/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist',
        '/Users/davidandreasson/Downloads/podcasts.opml'
    )
