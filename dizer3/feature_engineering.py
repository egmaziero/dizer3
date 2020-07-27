
def extract_features(segmented_text):
    features_per_pair = []
    p = 0
    while p < len(segmented_text):
        sentences = segmented_text[p]
        s = 0
        while s < len(sentences):
            segments = sentences[s]
            i = 0
            while i < len(segments):
                if i < len(segments) - 1:
                    left = segments[i]
                    right = segments[i+1]
                    features = extract(
                        left, right, same_par=True, same_sent=True)
                    features_per_pair.append(
                        [('segments', p, s, i, i+1), [features]])
                i += 1
            if s < len(sentences) - 1:
                left = [token for segment in sentences[s] for token in segment]
                len_left_edus = len(sentences[s])
                right = [token for segment in sentences[s+1]
                         for token in segment]
                len_right_edus = len(sentences[s+1])
                features = extract(left, right, same_par=True,
                                   left_sentences=1, right_sentences=1,
                                   left_edus=len_left_edus, right_edus=len_right_edus)
                features_per_pair.append(
                    [('sentences', p, s, s+1), [features]])
            s += 1
        if p < len(segmented_text) - 1:
            left = [token for sentence in segmented_text[p]
                    for segment in sentence for token in segment]
            len_left_edus = sum([len(sentence)
                                 for sentence in segmented_text[p]])
            right = [token for sentence in segmented_text[p+1]
                     for segment in sentence for token in segment]
            len_right_edus = sum([len(sentence)
                                  for sentence in segmented_text[p+1]])
            len_left_sentence = len(segmented_text[p])
            len_right_sentence = len(segmented_text[p+1])
            features = extract(left, right,
                               left_sentences=len_left_sentence, right_sentences=len_right_sentence,
                               left_edus=len_left_edus, right_edus=len_right_edus)
            features_per_pair.append([('paragraphs', p, p+1), [features]])
        p += 1
    return features_per_pair


def extract(left, right, same_par=False, same_sent=False,
            left_sentences=0, right_sentences=0, left_edus=1, right_edus=1):
    features = []
    features.append(1 if same_par else 0)  # same paragraph
    features.append(1 if same_sent else 0)  # same sentence
    features.append(left_sentences)  # size in sentences
    features.append(right_sentences)  # size in sentences
    features.append(len(left))  # size in tokens
    features.append(len(right))  # size in tokens
    features.append(left_edus)
    features.append(right_edus)

    # distance (in tokens) to begin of sentence
    # len segment / sentence, in tokens
    # len segment / sentence, in edus
    # len pair segment / sentence, in edus
    # distance (in edus) to begin of sentence
    # distance (in tokens) to begin of text
    # distance (in tokens) to end of sentence
    # first token
    # second token
    # third token
    # last token
    # penultimate token
    # antepenult token
    # is it interrogative
    # is it exclamatory

    # type of first conjunction
    # type of last conjuntion
    # number of verbs / len segments, in tokens
    # number of nouns / len segments, in tokens
    # number of adverbs / len segments, in tokens
    # number of adjectives / len segments, in tokens
    # number of conjunctions / len segments, in tokens
    # number of content words / len segments, in tokens

    # distance to root of sintactical tree
    # distance to commom ancestor
    # avg distance to commom ancestor
    # head of segment
    # pos of commom ancestor
    # head of commom ancestor
    # ...

    # number of synonym verbs
    # number of synonym nouns
    # number of antonym verbs
    # number of antonym nouns
    # number of antonym adverbs
    # number of antonym adjectives
    # number of named entities
    # number of lexical chains
    # number of commom lexical chains

    # first discourse marker

    return features
