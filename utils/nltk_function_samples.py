## User defined functions for pre-processing of natural language
# Code slightly adapted from John Hogue, Natural Language Processing with Spark ML, https://github.com/dreyco676/nlp_spark
# Last adapted: 30th January 2022

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tag.perceptron import PerceptronTagger
import string
import re
from langid.langid import LanguageIdentifier, model


## Detecting the language of a string with "langid"
# cf. https://github.com/saffsd/langid.py
identifier = LanguageIdentifier.from_modelstring(model, norm_probs=True)

def check_lang(data_str):
    predict_lang = identifier.classify(data_str.lower()) # testing has shown, that this function is indeed case-sensitive!
    if predict_lang[1] >= .9:
        language = predict_lang[0]
    else:
        language = 'NA'
    return language


## Remove certain "stopwords" (most used words in English)
def remove_stops(data_str):
    stops = set(stopwords.words("english"))
    list_pos = 0
    cleaned_str = ''
    text = data_str.split()
    
    for word in text:
        if word not in stops:
            # rebuild cleaned_str
            if list_pos == 0:
                cleaned_str = word
            else:
                cleaned_str = cleaned_str + ' ' + word
            list_pos += 1
    return cleaned_str


## Remove other features like URLs, numbers and punctuation marks
def remove_features(data_str):
    # compile regex
    url_re = re.compile('https?://(www.)?\w+\.\w+(/\w+)*/?')
    punc_re = re.compile('[%s]' % re.escape(string.punctuation))
    num_re = re.compile('(\\d+)')
    mention_re = re.compile('@(\w+)')
    alpha_num_re = re.compile("^[a-z0-9_.]+$")
    
    # convert to lowercase
    data_str = data_str.lower()
    
    # remove hyperlinks
    data_str = url_re.sub(' ', data_str)
    
    # remove @mentions
    data_str = mention_re.sub(' ', data_str)
    
    # remove puncuation
    data_str = punc_re.sub(' ', data_str)
    
    # remove numeric 'words'
    data_str = num_re.sub(' ', data_str)
    
    # remove non a-z 0-9 characters and words shorter than 3 characters
    list_pos = 0
    cleaned_str = ''
    for word in data_str.split():
        if list_pos == 0:
            if alpha_num_re.match(word) and len(word) > 2:
                cleaned_str = word
            else:
                cleaned_str = ' '
        else:
            if alpha_num_re.match(word) and len(word) > 2:
                cleaned_str = cleaned_str + ' ' + word
            else:
                cleaned_str += ' '
        list_pos += 1
    return cleaned_str


## Parts-of-speech tagging
# cf. http://www.nltk.org/book/ch05.html
# cf. https://pythonexamples.org/nltk-pos-tagging/
tagger = PerceptronTagger()

def tag_and_remove(data_str):
    cleaned_str = ' '
    
    # noun tags
    nn_tags = ['NN', 'NNP', 'NNPS', 'NNS']
    
    # adjectives
    jj_tags = ['JJ', 'JJR', 'JJS']
    
    # verbs
    vb_tags = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
    
    # total tags to keep
    nltk_tags = nn_tags + jj_tags + vb_tags

    # break string into 'words'
    text = data_str.split()

    # tag the text and keep only those with the right tags
    tagged_text = tagger.tag(text)
    for tagged_word in tagged_text:
        if tagged_word[1] in nltk_tags:
            cleaned_str += tagged_word[0] + ' '

    return cleaned_str



## Lemmatization of text
# cf. http://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html
def lemmatize(data_str):
    list_pos = 0
    cleaned_str = ''
    
    lmtzr = WordNetLemmatizer()
    text = data_str.split()
    tagged_words = tagger.tag(text)
    
    for word in tagged_words:
        if 'v' in word[1].lower():
            lemma = lmtzr.lemmatize(word[0], pos='v')
        else:
            lemma = lmtzr.lemmatize(word[0], pos='n')
        if list_pos == 0:
            cleaned_str = lemma
        else:
            cleaned_str = cleaned_str + ' ' + lemma
        list_pos += 1
    return cleaned_str


## Indicates if a string is empty or only contains whitespace
def check_blanks(data_str):
    is_blank = str(data_str.isspace())
    
    if is_blank == "False" and len(data_str) == 0:
        is_blank = "True"
        
    return is_blank
