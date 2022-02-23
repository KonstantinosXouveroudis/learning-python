from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, cross_val_score


def get_score(model, x_trainl, x_testl, y_trainl, y_testl):
    model.fit(x_trainl, y_trainl)
    return model.score(x_testl, y_testl)


def simple_kfold_example(kfl):
    for train_indexl, test_indexl in kfl.split([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        print(train_indexl, test_indexl)


if __name__ == '__main__':
    digits = load_digits()

    x_train, x_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.3)

    # We needed to increase the number of iterations to avoid an error.
    lr = LogisticRegression(solver='lbfgs', max_iter=5000)
    accuracy_lr = get_score(lr, x_train, x_test, y_train, y_test)

    svc = SVC()
    accuracy_svc = get_score(svc, x_train, x_test, y_train, y_test)

    rfc = RandomForestClassifier(n_estimators=20)
    accuracy_rfc = get_score(rfc, x_train, x_test, y_train, y_test)

    print("Accuracy of the different classifiers:"
          "\nLogistic Regression: ", accuracy_lr,
          "\nSVC: ", accuracy_svc,
          "\nRandom Forest Classifier: ", accuracy_rfc, "\n")

    # Using k-fold cross validation, we will attempt to determine which classifier is best suited for this dataset
    kf = KFold(n_splits=3)  # 3 folds
    # simple_kfold_example(kf)

    # StratifiedKFold maintains the same class ratio throughout the K folds as the ratio in the original dataset
    folds = StratifiedKFold(n_splits=3)

    scores_lr = []
    scores_svc = []
    scores_rhc = []

    for train_index, test_index in kf.split(digits.data):
        x_train, x_test, y_train, y_test = digits.data[train_index], digits.data[test_index], \
                                           digits.target[train_index], digits.target[test_index]

        scores_lr.append(get_score(lr, x_train, x_test, y_train, y_test))
        scores_svc.append(get_score(svc, x_train, x_test, y_train, y_test))
        scores_rhc.append(get_score(rfc, x_train, x_test, y_train, y_test))

    print("Logistic Regression:", scores_lr)
    print("SVC:", scores_svc)
    print("Random Forest Classifier:", scores_rhc)

    # Instead of using a for loop, we can do the same thing with the cross_val_score method.
    print("\nLogistic Regression:", cross_val_score(lr, digits.data, digits.target))
    print("SVC:", cross_val_score(svc, digits.data, digits.target))
    print("Random Forest Classifier:", cross_val_score(rfc, digits.data, digits.target))
