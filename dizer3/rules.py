import logging
from utils import parenthetical_markers
from utils import attribution_verbs

def parenthetical(left, righ):
    try:
        if right[0]['token'] in parenthetical_markers.keys():
            return 'parenthetical, ns'
        elif left[0]['token'] in parenthetical_markers.keys():
            return 'parenthetical, sn'
    except:
        logging.warning('Error looking for parenthetical. Continuing...')
    return None


def attribution(left, right):
    for token in left:
        if token['lemma'] in attribution_verbs:
            return 'attribution,sn'
    for token in right:
        if token['lemma'] in attribution_verbs:
            return 'attribution,ns'
        # if ( ((trim(lc($lemma)) eq "conforme") and ($pos eq "prp")) or ((trim(lc($lemma)) eq "segundo") and ($pos eq "prp")) or ((trim(lc($lemma)) eq "consoante") and ($pos eq "prp"))  or ((trim(lc($lemma)) eq "de acordo") and ($pos eq "adv")) )
        # {
        #     print "attribut";
        #     $foundRelation = 1;
        # }
    return None


def relations_by_rules(left, right):
    relations = []
    relation = parenthetical(left, right)
    if relations is not None:
        relations.append(relation)
    relation = attribution(left, right)
    if relations is not None:
        relations.append(relation)
    # translation: can we train a NN to translate?

    # summarization: can we verify if two segments are very similar

    return relations
