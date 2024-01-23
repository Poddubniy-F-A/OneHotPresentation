import generating as g
import pandas as pd


def one_hot_presentation(data):
    labels = sorted(list(data[g.COL_NAME].unique()))
    labels_matching = []
    for label in labels:
        labels_matching.append([data[g.COL_NAME][i] == label for i in range(data.shape[0])])

    return pd.DataFrame({labels[i]: labels_matching[i] for i in range(len(labels))})


# для проверки эквивалентности результата работы программы результату использования pandas.get_dummies:
# sdata = g.gen()
# print(one_hot_presentation(data).equals(pd.get_dummies(data[g.COL_NAME])))
