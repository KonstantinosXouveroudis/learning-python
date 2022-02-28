import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


if __name__ == '__main__':
    df = pd.read_csv("data\\spam.csv")
    print(df.head())

    # How many normal (ham) and spam messages are included in our dataset?
    print("\n", df.groupby('Category').describe())

    # New column for classifying spam messages numerically.
    df['Spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)
    print("\n", df.head())

    x_train, x_test, y_train, y_test = train_test_split(df['Message'], df['Spam'])

    # Used to convert the messages to a matrix of token counts so we can train our model.
    v = CountVectorizer()
    x_train_count = v.fit_transform(x_train.values)

    # Creating and training our model
    model = MultinomialNB()
    model.fit(x_train_count, y_train)

    emails = [
        'Hey mohan, can we get together to watch football game tomorrow?',
        'Upto 20% discount on parking, exclusive offer just for you. Dont miss this reward!'
    ]
    emails_count = v.transform(emails)  # Again, transforming the strings so we can use them in our prediction.
    prediction = model.predict(emails_count)
    print("\nPREDICTION:", prediction)

    x_test_count = v.transform(x_test)
    accuracy = model.score(x_test_count, y_test)
    print("Accuracy:", accuracy)

    # IMPORTANT: Instead of calling CountVectorizer on every occasion, we can use sklearn's Pipeline like below:
    clf = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('nb', MultinomialNB())
    ])

    clf.fit(x_train, y_train)

    prediction = clf.predict(emails)
    print("\nPREDICTION (Pipeline):", prediction)

    accuracy = clf.score(x_test, y_test)
    print("Accuracy (Pipeline): ", accuracy)

