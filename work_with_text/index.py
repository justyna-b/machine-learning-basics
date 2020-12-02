from spacy.matcher import Matcher
from spacy import displacy
import spacy
from spacy.tokenizer import Tokenizer
import re
from collections import Counter

# Load the language model instance in spaCy
nlp = spacy.load("pl_core_news_sm")

# the string is converted to is converted to object that spacy understand
introduction_text = (
    'This tutorial is about Natural' ' Language Processing in Spacy.')
introduction_doc = nlp(introduction_text)
print([token.text for token in introduction_doc])

# path to file
file_name = 'text_file.txt'
# read file (Unicode string object)
introduction_file_text = open(file_name).read()
# convert to doc obj that is understood by spacy (spaCy’s language model object)
introduction_file_doc = nlp(introduction_file_text)
print([token.text for token in introduction_file_doc])

# Sentence Dedection - programme is looking for start and end part of the sentence (default ".")
# In spaCy, the sents property is used to extract sentences.
about_text = ('Litwo! Ojczyzno moja! ty jesteś jak zdrowie: '
              'Ile cię trzeba cenić, ten tylko się dowie, '
              'Kto cię stracił. Dziś piękność twą w całej ozdobie '
              'Widzę i opisuję, bo tęsknię po tobie.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)
for sentence in sentences:
    print(sentence)

# function to customize delimiter, now it will be "..."


def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc


ellipsis_text = ('Panno święta, ... co Jasnej bronisz Częstochowy' ' I w Ostrej świecisz Bramie ! Ty, ... co gród zamkowy Nowogródzki... ochraniasz. z jego wiernym ludem! ...')
custom_nlp = spacy.load('pl_core_news_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)

# Sentence Detection with no customization
custom_nlp = spacy.load('pl_core_news_sm')
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
print('sentence Detection with no customization')
for sentence in ellipsis_sentences:
    print(sentence)


# basic units in text are called tokens
# Tokenization is useful because it breaks a text into meaningful units
# show on which char (starting from 0) word occure
for token in about_doc:
    print(token, token.idx)


# text_with_ws prints token text with trailing space (if present).
# is_alpha detects if the token consists of alphabetic characters or not.
# is_punct detects if the token is a punctuation symbol or not.
# is_space detects if the token is a space or not.
# shape_ prints out the shape of the word.
# is_stop detects if the token is a stop word or not.
for token in about_doc:
    print(token, token.idx, token.text_with_ws,
          token.is_alpha, token.is_punct, token.is_space, token.shape_, token.is_stop)


# spaCy already detects hyphenated words as individual tokens

# nlp.vocab is a storage container for special cases and is used to handle cases like contractions and emoticons.
# prefix_search is the function that is used to handle preceding punctuation, such as opening parentheses.
# infix_finditer is the function that is used to handle non-whitespace separators, such as hyphens.
# suffix_search is the function that is used to handle succeeding punctuation, such as closing parentheses.
# token_match is an optional Boolean function that is used to match strings that should never be split. It overrides the previous rules and is useful for entities like URLs or numbers.
custom_nlp = spacy.load('pl_core_news_sm')
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')


def customize_tokenizer(nlp):
    # Adds support to use `-` as the delimiter for tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search, suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer, token_match=None)


custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_about_doc = custom_nlp(about_text)
print([token.text for token in custom_tokenizer_about_doc])

# stop words are the most common words in the concrete language
# it bother in word frequency analisys so it's removed
# above code show stop words for polish language
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
print(len(spacy_stopwords))
for stop_word in list(spacy_stopwords)[:20]:
    print(stop_word)

# remove stop words from your input text
for token in about_doc:
    if not token.is_stop:
        # show stop words
        print(token)

# create spaCy’s language model object without stop words
about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
print(about_no_stopword_doc)

# lemmatization - thanks to that we can treat collocations like one and the same word
# For example, organizes, organized and organizing are all forms of organize. Here, organize is the lemma.
conference_help_text = ('Jak mnie dziecko do zdrowia powróciłaś cudem'
                        '(Gdy od płaczącej matki, pod Twoją opiekę' 'Ofiarowany, martwą podniosłem powiekę;'
                        'I zaraz mogłem pieszo, do Twych świątyń progu''Iść za wrócone życie podziękować Bogu),''Tak nas powrócisz cudem na Ojczyzny łono.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print(token, token.lemma_)

# word frequency
complete_text = ('Tymczasem przenoś moją duszę utęsknioną'
                 'Do tych pagórków leśnych, do tych łąk zielonych,'
                 'Szeroko nad błękitnym Niemnem rozciągnionych;'
                 'Do tych pól malowanych zbożem rozmaitem,'
                 'Wyzłacanych pszenicą, posrebrzanych żytem;'
                 'Gdzie bursztynowy świerzop, gryka jak śnieg biała,'
                 'Gdzie panieńskim rumieńcem dzięcielina pała,'
                 'A wszystko przepasane jakby wstęgą, miedzą'
                 'Zieloną, na niej z rzadka ciche grusze siedzą.')
...
complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print(common_words)
# Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print(unique_words)

# word frequency with stop words
# If you consider stop words while doing word frequency analysis, then you won’t be able to derive meaningful insights from the input text. This is why removing stop words is so important.
words_all = [token.text for token in complete_doc if not token.is_punct]
word_freq_all = Counter(words_all)
# 5 commonly occurring words with their frequencies
common_words_all = word_freq_all.most_common(5)
print(common_words_all)

# Part of speech or POS is a grammatical role that explains how a particular word is used in a sentence.
# Part of speech tagging is the process of assigning a POS tag to each token depending on its usage in the sentence. POS tags are useful for assigning a syntactic category like noun or verb to each word.
for token in about_doc:
    print(token, token.tag_, token.pos_, spacy.explain(token.tag_))

# dependency parse or named entities vizualization in a browser
nouns = []
adjectives = []
for token in about_doc:
    if token.pos_ == 'NOUN':
        nouns.append(token)
    if token.pos_ == 'ADJ':
        adjectives.append(token)

# about_interest_text = (
#     'Możesz zwizualizować swó text w przeglądarce'' Sprawdź http://127.0.0.1:5000/')
# about_interest_doc = nlp(about_interest_text)
# displacy.serve(about_interest_doc, style='dep')

# create preprocessing function which allows you to: lowercase your text, lemmatizes each token, remove punctuation symbols, removes stop words


def is_token_allowed(token):
    # '''
    #     Only allow valid tokens which are not stop words
    #     and punctuation symbols.
    # '''
    if (not token or not token.string.strip() or
            token.is_stop or token.is_punct):
        return False
    return True


def preprocess_token(token):
    # Reduce token to its lowercase lemma form
    return token.lemma_.strip().lower()


# leminized lowercase tokens with removed stop words and punctuation symbols
complete_filtered_tokens = [preprocess_token(token)
                            for token in complete_doc if is_token_allowed(token)]
print(complete_filtered_tokens)

# Rule-based matching is one of the steps in extracting information from unstructured text. It’s used to identify and extract tokens and phrases according to patterns (such as lowercase) and grammatical features (such as part of speech).
matcher = Matcher(nlp.vocab)
conference_org_text = ('Śród takich pól przed laty, nad brzegiem ruczaju,'
                       'Na pagórku niewielkim, we brzozowym gaju,'
                       'Stał dwór szlachecki, z drzewa, lecz podmurowany;'
                       'Świeciły się z daleka pobielane ściany,'
                       'Tym bielsze, że odbite od ciemnej zieleni'
                       'Topoli, co go bronią od wiatrów jesieni.'
                       ' napisz 333-333-333')
# extract phone number from text
# ORTH gives the exact text of the token.
# SHAPE transforms the token string to show orthographic features.
# OP defines operators. Using ? as a value means that the pattern is optional, meaning it can match 0 or 1 times.


def extract_phone_number(nlp_doc):
    pattern = [{'SHAPE': 'ddd'}, {'ORTH': '-', 'OP': '?'}, {'SHAPE': 'ddd'}, {'ORTH': '-', 'OP': '?'},
               {'SHAPE': 'ddd'}]
    matcher.add('PHONE_NUMBER', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text


conference_org_doc = nlp(conference_org_text)
print(extract_phone_number(conference_org_doc))

# Dependency parsing helps you know what role a word plays in the text and how different words relate to each other. It’s also used in shallow parsing and named entity recognition.
dummy_text = 'Pingwiny są jedynymi ptakami, które zachowują wyprostowaną postawę ciała.'
dummy_doc = nlp(dummy_text)
for token in dummy_doc:
    print(token.text, token.tag_, token.head.text, token.dep_)
# in output :
# nsubj is the subject of the word. Its headword is a verb.
# aux is an auxiliary word. Its headword is a verb.
# dobj is the direct object of the verb. Its headword is a verb.

# visualize in browser
displacy.serve(dummy_doc, style='dep')

# Navigating the Tree and Subtree
# This tree contains information about sentence structure and grammar and can be traversed in different ways to extract relationships.
one_line_about_text = ('Pingwiny połykają dużo wody morskiej podczas polowania na ryby, ale specjalny gruczoł za oczami – gruczoł nadoczodołowy – filtruje słoną wodę ze strumienia krwi.'' Pingwiny wydalają ją przez dzioby lub przez kichanie.')
one_line_about_doc = nlp(one_line_about_text)
# Extract children of `developer`
print([token.text for token in one_line_about_doc[5].children])
# Extract previous neighboring node of `developer`
print(one_line_about_doc[5].nbor(-1))
# Extract next neighboring node of `developer`
print(one_line_about_doc[5].nbor())
# Extract all tokens on the left of `developer`
print([token.text for token in one_line_about_doc[5].lefts])
# Extract tokens on the right of `developer`
print([token.text for token in one_line_about_doc[5].rights])
# Print subtree of `developer`
print(list(one_line_about_doc[5].subtree))

# a function that takes a subtree as an argument and returns a string by merging words in it
def flatten_tree(tree):
    return ''.join([token.text_with_ws for token in list(tree)]).strip()
# Print flattened subtree of `developer`
print (flatten_tree(one_line_about_doc[5].subtree))


