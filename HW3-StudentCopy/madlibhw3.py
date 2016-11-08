# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk
from nltk.book import text2
import random
print(text2)
print(len(text2))
# print(sorted(set(text2))[:151])
tokens = text2[:151]
tagged_tokens = nltk.pos_tag(tokens)
print("TOKENS")
print(tokens)
print("TAGGED TOKENS")
print(tagged_tokens)
for tup in tagged_tokens[:5]:
	print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"JJ":.1}

final_words = []

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))
print("\n\nEND*******")
