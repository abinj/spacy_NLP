from spacy.lang.en import English

nlp = English()
doc = nlp("Sen. Bernie Sanders, the Democratic presidential frontrunner, said in an interview that aired Sunday that he would take military actions if China decided to strike Taiwan.")

for token in doc:
    print(token.text)