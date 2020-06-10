from utils import parenthetical_markers
from utils import attribution_verbs

def parenthetical(segment):
    try:
        if segment[0]['token'] in parenthetical_markers.keys():
            return 'parenthetical'
    except:
        print('Error looking for parenthetical. Continuing...')
    return None


def attribution(segment):
    for token in segment:
        if token['lemma'] in attribution_verbs:
            return 'attribution'
        # if ( ((trim(lc($lemma)) eq "conforme") and ($pos eq "prp")) or ((trim(lc($lemma)) eq "segundo") and ($pos eq "prp")) or ((trim(lc($lemma)) eq "consoante") and ($pos eq "prp"))  or ((trim(lc($lemma)) eq "de acordo") and ($pos eq "adv")) )
        # {
        #     print "attribut";
        #     $foundRelation = 1;
        # }
    return None


def relations_by_rules(segmented_text):
    relations = []

    paragraph_index = 0
    for sentences in segmented_text:
        relations.append([])
        sentence_index = 0
        for segment in sentences:
            relations[paragraph_index].append([])

            relation = parenthetical(segment)
            if relation is not None:
                relations[paragraph_index][sentence_index].extend([relation])

            relation = attribution(segment)
            if relation is not None:
                relations[paragraph_index][sentence_index].extend([relation])

            sentence_index += 1
        paragraph_index += 1

    # translation: can we train a NN to translate?

    # summarization: can we verify if two segments are very similar

    return relations
