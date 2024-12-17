import nltk
from nltk.tree import Tree

# Define a new sentence
sentence = "The dog barked loudly at the stranger."

# Define the parse tree in string format
parse_tree_string = "(S (NP (Det The) (N dog)) (VP (V barked) (ADVP (Adv loudly)) (PP (P at) (NP (Det the) (N stranger)))))"

# Create the parse tree from the string
parse_tree = Tree.fromstring(parse_tree_string)

# Visualize the parse tree
parse_tree.pretty_print()
