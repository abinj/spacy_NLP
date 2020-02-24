from spacy.lang.de import German
from spacy.lang.en import English
from spacy.lang.zh import Chinese


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
