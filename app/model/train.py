from sklearn.linear_model import LogisticRegression
from data.loader import load_train_test

def train_model():
    X_train, X_test, y_train, y_test = load_train_test()

    model = LogisticRegression(C=1, penalty='l2', max_iter=2000)
    model.fit(X_train, y_train)

    return model