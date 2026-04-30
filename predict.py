import pickle

model = pickle.load(open('models/spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))

msg = input("Enter message: ")

data = vectorizer.transform([msg])

prediction = model.predict(data)

if prediction[0] == 1:
    print("Spam")
else:
    print("Not Spam")
