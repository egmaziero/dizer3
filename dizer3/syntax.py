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
    for line in lines:
        if re.match("^\d+", line):
            parts = line.split("\t")
            token = {'token': parts[1],
                     'lemma': parts[2],
                     'pos': parts[3],
                     'morpho': parts[5],
                     'head': parts[6],
                     'dep': parts[7]}
            annotation.append(token)

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
