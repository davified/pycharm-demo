import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier


def prepare_data_and_train_model():
    project_dir = os.path.dirname(os.path.dirname(__file__))
    train_df = pd.read_csv(f"{project_dir}/data/train.csv")
    test_df = pd.read_csv(f"{project_dir}/data/test.csv")
    df = pd.concat([train_df, test_df])

    df = df.drop(['Ticket', 'Cabin'], axis=1)

    # derive 'Title' column from 'Name' column
    df['Title'] = df.Name.str.extract(' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].replace(
        ['Lady','Countess','Capt', 'Col', 'Don', 'Dr', 'Major','Rev', 'Sir',   'Jonkheer', 'Dona'], 'Rare')

    df['Title'] = df['Title'].replace('Mlle', 'Miss')
    df['Title'] = df['Title'].replace('Ms', 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')

    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    df['Title'] = df['Title'].map(title_mapping)
    df['Title'] = df['Title'].fillna(0)

    df = df.drop(['Name', 'PassengerId'], axis=1)

    # Convert 'Sex' to categorical column
    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0}).astype(int)

    # fillna: 'Age'
    df['Age'] = df['Age'].fillna(df['Age'].dropna().median())

    # Derive 'IsAlone' column
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

    df = df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)


    freq_port = df.Embarked.dropna().mode()[0]
    df['Embarked'] = df['Embarked' ].fillna(freq_port)
    df['Embarked'] = df['Embarked'].map({'S': 0,   'C': 1, 'Q': 2}).astype(int)

    train_df = df[-df['Survived'].isna()]
    X = train_df.drop("Survived", axis=1)
    Y = train_df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

    rf_model = RandomForestClassifier(n_estimators=10)
    rf_model.fit(X_train, Y_train)
    rf_model.score(X_train, Y_train)
    acc_random_forest = round(rf_model.score(X_train, Y_train) * 100, 2)
    acc_random_forest

    return rf_model, X_test, Y_test
