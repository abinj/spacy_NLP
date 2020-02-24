import spacy
from spacy.lang.de import German
from spacy.lang.en import English
from spacy.lang.zh import Chinese
from spacy.matcher import Matcher


#Lexical Attributes
def print_lexical_attributes(doc):
    # Lexical Attributes
    print('Index: ', [token.i for token in doc])
    print('Text: ', [token.i for token in doc])
    # Checks whether the token consists of alphanumeric values or not
    print('is_alpha: ', [token.is_alpha for token in doc])
    # Checks whether token consists of punctuation
    print('is_punct: ', [token.is_punct for token in doc])
    # Checks whether token consists of a number
    print('like_num: ', [token.like_num for token in doc])


print("English")
nlp = English()
doc = nlp("Sen. Bernie Sanders, the Democratic presidential frontrunner, said in an interview that aired Sunday that he would take military actions if China decided to strike Taiwan.")
print_lexical_attributes(doc)


print("\n\nGerman")
nlp = German()
doc = nlp("Senator Bernie Sanders, der Spitzenreiter des demokratischen Präsidenten, sagte in einem Interview, das am Sonntag ausgestrahlt wurde, dass er militärische Maßnahmen ergreifen würde, wenn China beschließen würde, Taiwan anzugreifen.")
print_lexical_attributes(doc)


print("\n\nChinese")
nlp = Chinese()
nlp.use_jieba = False
doc = nlp("民主党总统候选人领先者参议员伯尼·桑德斯在周日播出的一次采访中说，如果中国决定打击台湾，他将采取军事行动。")
print_lexical_attributes(doc)



print("\n\nStatistical Models")
# POS, Syntactic Dependencies, Named Entities
#Make sure you downloaded the model using command 'python -m spacy download en_core_web_sm'
nlp = spacy.load('en_core_web_sm')
doc = nlp("Why do you stay in prison when the door is so wide open?")

#pos_ is part-of-speech , dep_ isdepecdency label and head.text returns syntactic head token
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

print("\n\n")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
#predicting Named Entities
for ent in doc.ents:
    print(ent.text, ent.label_)

print("\n\n")
print(spacy.explain('GPE'))
print(spacy.explain('NNP'))
print(spacy.explain('dobj'))

def print_matched_span(doc):
    matches = matcher(doc)
    for match_id, start, end in matches:
        # Get the matched span
        matched_span = doc[start:end]
        print(matched_span.text)

print("\n\n")
matcher = Matcher(nlp.vocab)
pattern = [{'TEXT': 'iPhone'}, {'TEXT': 'X'}]
matcher.add('IPHONE_PATTERN', None, pattern)
doc = nlp("New iPhone X release date leaked")
print_matched_span(doc)

pattern = [
    {'IS_DIGIT': True},
    {'LOWER': 'fifa'},
    {'LOWER': 'world'},
    {'LOWER': 'cup'},
    {'IS_PUNCT': True}
]

matcher.add('FIFA_PATTERN', None, pattern)
doc = nlp("2018 FIFA World Cup: France won!")
print_matched_span(doc)


pattern = [
    {'LEMMA': 'love', 'POS': 'VERB'},
    {'POS': 'NOUN'}
]
matcher.add('LOVE_PATTERN', None, pattern)
doc = nlp("I loved dogs but now I love cats more.")
print_matched_span(doc)

pattern = [
    {'LEMMA': 'buy'},
    {'POS': 'DET', 'OP': '?'},  # optional: match 0 or 1 times
    {'POS': 'NOUN'}
]
matcher.add('BUY_PATTERN', None, pattern)
doc = nlp("I bought a smartphone. Now I'm buying apps.")
print_matched_span(doc)

