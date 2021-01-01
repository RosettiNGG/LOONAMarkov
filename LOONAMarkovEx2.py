import markovify

# Get raw text as string.
with open('corpus.txt', encoding='utf8') as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text, well_formed=False)

# Print five randomly-generated sentences
for i in range(10):
    print(text_model.make_sentence())

