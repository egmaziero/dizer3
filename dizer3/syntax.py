import re
import nltk
import logging
from ufal.udpipe import Model, Pipeline, ProcessingError


model = Model.load('models/portuguese-bosque-ud-2.5-191206.udpipe')
pipeline = Pipeline(model, 'tokenize', Pipeline.DEFAULT,
                    Pipeline.DEFAULT, 'conllu')
error = ProcessingError()


def prepare_syn_annotation(sentence_annotation):
    annotation = []

    lines = sentence_annotation.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match("^\d+", line):
            parts = line.split("\t")
            try:
                if parts[3] == '_':
                    token_plus = lines[i + 1].split("\t")
                    token_plus_plus = lines[i + 2].split("\t")
                    if token_plus[3] == 'ADP' and token_plus_plus[3] == 'DET':
                        parts[3] = 'ADP+DET'
                        parts[5] = token_plus_plus[5]
                        parts[6] = token_plus[6]
                        parts[7] = token_plus[7]
                        i += 2
            except:
                logging.error("Error preparing syntax annotation")
            token = {'token': parts[1],
                     'lemma': parts[2],
                     'pos': parts[3],
                     'morpho': parts[5],
                     'head': parts[6],
                     'dep': parts[7]}
            annotation.append(token)
        i += 1

    return annotation


def nlu(sentences):
    annotations = []

    for sentence in sentences:
        ann = pipeline.process(sentence, error)
        if error.occurred():
            logging.info("An error occurred when running run_udpipe: ")
            logging.info(error.message)
        annotations.append(prepare_syn_annotation(ann))

    return annotations
