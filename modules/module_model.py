# Standard libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

# Sklearn
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split

# External modules
from module_path import plots_data_path



class ModelEvaluation:
    """
    Supports the evaluation of classification models (multinomial), collecting the results.
    """

    def __init__(self, X: pd.DataFrame, y: pd.DataFrame, test_size: float = 0.3, shuffle: bool = True, random_state: int = 42):
        """
        :param X: the inputs
        :param y: the prediction targets
        :param test_size: the fraction of the data to reserve for testing
        :param shuffle: whether to shuffle the data prior to splitting
        :param random_state: the random seed
        """

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
            random_state=random_state, test_size=test_size, shuffle=shuffle)

    def evaluate_model(self, model) -> float:
        """
        :param model: the model to evaluate
        :return: the f1-score
        """
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        f1_score = metrics.f1_score(self.y_test, y_pred)
        print(f"{model}: f1_score={f1_score:.1f}")
        return f1_score