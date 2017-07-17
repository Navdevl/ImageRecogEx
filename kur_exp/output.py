import pickle
import codecs
with codecs.open('output.pkl', 'r', encoding='utf-8') as file:
    data = pickle.load(file)

print(data)
