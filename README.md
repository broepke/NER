# An Accessible Guide to Named Entity Recognition

[Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition) or NER is a technique for identifying and classifying named entities in text. These entities are a level above [Part of Speech Tagging](https://www.dataknowsall.com/pos.html) and [Noun Phrase Chunking](https://www.dataknowsall.com/nounphrase.html) where instead of identifying grammatical parts; it's identifying and classifying words as their proper entities. The main categories that are recognized are:

```text
PERSON:      People, including fictional.
NORP:        Nationalities or religious or political groups.
FAC:         Buildings, airports, highways, bridges, etc.
ORG:         Companies, agencies, institutions, etc.
GPE:         Countries, cities, states.
LOC:         Non-GPE locations, mountain ranges, bodies of water.
PRODUCT:     Objects, vehicles, foods, etc. (Not services.)
EVENT:       Named hurricanes, battles, wars, sports events, etc.
WORK_OF_ART: Titles of books, songs, etc.
LAW:         Named documents made into laws.
LANGUAGE:    Any named language.
DATE:        Absolute or relative dates or periods.
TIME:        Times smaller than a day.
PERCENT:     Percentage, including ”%“.
MONEY:       Monetary values, including unit.
QUANTITY:    Measurements, as of weight or distance.
ORDINAL:     “first”, “second”, etc.
CARDINAL:    Numerals that do not fall under another type.
```

There are many libraries to choose from; my tool of choice these days is [SpaCy](https://spacy.io/) [^SPACY]. Its powerful API and models are ready to go with a few lines of code, and as we'll see later, we can use it to train our models. To demonstrate the power, let's take a look at it in action. 

Read more here: https://www.dataknowsall.com/ner.html
