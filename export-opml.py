import xml.dom.minidom


def export(filename):
    doc = xml.dom.minidom.parse(filename)
    print(doc.nodeName)


if __name__ == '__main__':
    # File containing podcasts is located here: ~/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist
    export('/Users/davidandreasson/Library/Containers/com.apple.podcasts/Data/Documents/PodcastsDB.plist')
