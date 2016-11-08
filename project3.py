# Part1
# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
# furthered By Hanshen Wang for project 3
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
substitution_probabilities = {"NN":.2,"NNS":.1,"VB":.3,"JJ":.2}

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

