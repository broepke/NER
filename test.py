import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("I ran quickly to the store")
print([token for token in doc])
    
print([token.pos_ for token in doc])


doc = nlp("I read a wonderful book. I booked a flight to Mexico.")
print([sent.text for sent in doc.sents])

print([chunk.text for chunk in doc.noun_chunks])

doc = nlp("Steve Jobs founded Apple Computer, Inc.")
print([(ent.text, ent.label_) for ent in doc.ents])



# displacy.serve(doc, style="ent")

print([(token.text, token.lemma_) for token in doc])