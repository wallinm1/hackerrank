from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
docs = []
with open('trainingdata.txt') as f:
    for idx, line in enumerate(f):
        if idx == 0:
            N_train = int(line)
        else:
            docs.append(line)
classes = []
for i in range(len(docs)):
    classes.append(int(docs[i][0]))
    docs[i] = docs[i][2:]
N_test = int(raw_input())
docs_test = []
for i in range(N_test):
    docs_test.append(raw_input())
all_docs = docs + docs_test
vect = TfidfVectorizer(ngram_range = (1, 1))
vect.fit(all_docs)
x_train = vect.transform(docs)
x_test = vect.transform(docs_test)
clf = LinearSVC(C = 100, random_state = 42)
clf.fit(x_train, classes)
preds = list(clf.predict(x_test))
for pred in preds:
    print pred