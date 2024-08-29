import spacy

def extract_entities(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

if __name__ == "__main__":
    text = "This is a sample text for entity extraction."
    entities = extract_entities(text)
    print(entities)
