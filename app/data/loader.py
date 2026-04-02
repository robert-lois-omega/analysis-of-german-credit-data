import pandas as pd

def load_data():
    return pd.read_csv("../dataset/index.csv")

def load_train_test():
    df = pd.read_csv("../dataset/index.csv")

    X_train = df.drop(['Creditability', 'Occupation', 'Unnamed: 0'], axis=1)
    y_train = df.Creditability

    test_data = pd.read_csv("../dataset/test.csv")
    test_data.drop(['Occupation', 'Unnamed: 0'], axis=1, inplace=True)

    X_test = test_data.drop('Creditability', axis=1)
    y_test = test_data.Creditability

    return X_train, X_test, y_train, y_test