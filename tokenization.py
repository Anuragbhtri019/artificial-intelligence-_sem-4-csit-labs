# Step 1: Import the NLTK module
import nltk

# Step 2: Download the necessary NLTK resources
nltk.download("punkt")  # For tokenization
nltk.download("averaged_perceptron_tagger_eng")  # For part-of-speech tagging

# Step 3: Define a paragraph of text
paragraph = """Natural Language Processing (NLP) is a field of artificial intelligence 
on the interaction between computers and humans through natural language."""

# Step 4: Tokenize the paragraph into sentences
sentences = nltk.sent_tokenize(paragraph)
print("Sentences:")
for i, sentence in enumerate(sentences, start=1):
    print(f"Sentence {i}: {sentence}")

    tokens = nltk.word_tokenize(sentence)
    print("  Tokens:", tokens)
    tagged = nltk.pos_tag(tokens)
    print("  Tagged:", tagged)
