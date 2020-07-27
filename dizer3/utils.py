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
    with open("{}.segments".format(file_path), 'w') as output:
        for p, sentences in enumerate(segmented_text):
            for s, sentence in enumerate(sentences):
                for i, segment in enumerate(sentence):
                    segment = ' '.join([t['token'] for t in segment])
                    output.write("{}:{}:{}: {}".format(p+1, s+1, i+1,
                                                       posprocessing(segment)))
                    output.write("\n")


def print_relations(segmented_text, file_path, relations):
    with open("{}.relations".format(file_path), 'w') as output:
        p = 0
        while p < len(segmented_text):
            sentences = segmented_text[p]
            s = 0
            while s < len(sentences):
                segments = sentences[s]
                i = 0
                while i < len(segments):
                    if i < len(segments) - 1:
                        relation = relations.pop(0)
                        output.write("{}:{}:{}-{}: {}".format(p+1, s+1, i+1,
                                                              i+2, relation))
                        output.write("\n")
                    i += 1
                if s < len(sentences) - 1:
                    relation = relations.pop(0)
                    output.write(
                        "{}:{}-{}: {}".format(p+1, s+1, s+2, relation))
                    output.write("\n")
                s += 1
            if p < len(segmented_text) - 1:
                relation = relations.pop(0)
                output.write("{}-{}: {}".format(p+1, p+2, relation))
                output.write("\n")
            p += 1
