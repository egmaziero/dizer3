from preprocess import posprocessing


parenthetical_markers = {'(': ')', '[': ']', '{': '}'}

attribution_verbs = set()
with open('resources/attribVerbs.txt', 'r') as file:
    attrib_verbs = file.readlines()
    attribution_verbs = set([a.strip() for a in attrib_verbs])

discourse_markers = {}
with open('resources/discourseMarkers.txt', 'r') as file:
    markers = file.readlines()
    discourse_markers = {p.split(',')[0]: p.split(',')[
        1].strip() for p in markers}


def print_segments(segmented_text, file_path):
    counter = 1
    with open("{}.segments".format(file_path), 'w') as output:
        for sentences in segmented_text:
            for segment in sentences:
                segment = ' '.join([t['token'] for t in segment])
                output.write("{}: {}".format(counter, posprocessing(segment)))
                output.write("\n")
                counter += 1
