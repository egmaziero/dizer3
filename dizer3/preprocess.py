import re
import nltk
import unidecode
import string

sent_tokenizer = nltk.data.load('tokenizers/punkt/portuguese.pickle')

stopwords = ["a", "à", "ah", "ai", "algo", "alguém", "algum", "alguma", "algumas",
             "alguns", "alô", "ambos", "ante", "ao", "apenas", "após", "aquela",
             "aquelas", "aquele", "aqueles", "aquilo", "as", "até", "bis", "cada",
             "certa", "certas", "certo", "certos", "chi", "com", "comigo", "conforme",
             "conosco", "consigo", "contigo", "contra", "convosco", "cuja", "cujas",
             "cujo", "cujos", "da", "das", "de", "dela", "delas", "dele", "deles",
                     "desde", "dessa", "dessas", "desse", "desses", "disso", "desta", "destas",
                     "deste", "destes", "disto", "daquela", "daquelas", "daquele", "daqueles",
                     "daquilo", "do", "dos", "e", "eia", "ela", "elas", "ele", "eles", "em",
                     "embora", "enquanto", "entre", "essa", "essas", "esse", "esses", "esta",
                     "este", "estes", "estou", "eu", "hem", "hum", "ih", "isso", "isto", "lhe",
                     "lhes", "logo", "mais", "mas", "me", "menos", "mesma", "mesmas", "mesmo",
                     "mesmos", "meu", "meus", "mim", "minha", "minhas", "muita", "muitas",
                     "muito", "muitos", "na", "nada", "nas", "nela", "nelas", "nele", "neles",
                     "nem", "nenhum", "nenhuma", "nenhumas", "nenhuns", "ninguém", "no", "nos",
                     "nós", "nossa", "nossas", "nosso", "nossos", "nela", "nelas", "nele",
                     "neles", "nessa", "nessas", "nesse", "nesses", "nisso", "nesta", "nestas",
                     "neste", "nestes", "nisto", "naquela", "naquelas", "naquele", "naqueles",
                     "naquilo", "o", "ó", "ô", "oba", "oh", "olá", "onde", "opa", "ora", "os",
                     "ou", "outra", "outras", "outrem", "outro", "outros", "para", "pelo",
                     "pela", "pelos", "pelas", "per", "perante", "pois", "por", "porém",
                     "porque", "portanto", "pouca", "poucas", "pouco", "poucos", "próprios",
                     "psit", "psiu", "quais", "quaisquer", "qual", "qualquer", "quando",
                     "quanta", "quantas", "quanto", "quantos", "que", "quem", "se", "sem",
                     "seu", "seus", "si", "sob", "sobre", "sua", "suas", "talvez", "tanta",
                     "tantas", "tanto", "tantos", "te", "teu", "teus", "ti", "toda", "todas",
                     "todo", "todos", "trás", "tu", "tua", "tuas", "tudo", "ué", "uh", "ui",
                     "um", "uma", "umas", "uns", "vária", "várias", "vário", "vários", "você",
                     "vós", "vossa", "vossas", "vosso", "vossos", "ser", "estar"]


def tokenize_sentences(text):
    return sent_tokenizer.tokenize(text)


def tokenize_paragraphs(text):
    return text.split("\n")


def tokenize_text(text):
    paragraphd = paragraph_tokenization(text)
    sentenced = [sentence_tokenization(paragraph)
                 for paragraph in paragraphd]

    return sentenced


def normalize(text, remove_stopwords=True, remove_punctuation=True, remove_accents=True, lower=True):
    if remove_punctuation:
        text = text.translate(str.maketrans('', '', string.punctuation))
    if remove_accents:
        text = unidecode.unidecode(text)
    if lower:
        text = text.lower()
    if remove_stopwords:
        tokens = nltk.tokenize.word_tokenize(text)
        tokens = [t for t in tokens if t not in stopwords]
        text = ' '.join(tokens)

    return text


def word_tokenization(sentence):
    return nltk.word_tokenize(sentence, language='portuguese')


def join_punctuation(match_object):
    return re.sub('\s+', '', match_object.group(0))


def posprocessing(text):
    # join punctuation
    text = re.sub(
        "\s+[\.\,\:\!\?\-\$\%\@\)\]\}]+", join_punctuation, text)
    text = text.replace('( ', '(').replace('[ ', '[').replace('{ ', '}')
    return text
