# Standard libraries
import pandas as pd
import matplotlib.pyplot as plt
import os
import functools

# Sklearn
import sklearn.metrics as metrics
from sklearn.model_selection import train_test_split

# MLFlow
import mlflow
from mlflow.models.signature import infer_signature

# External modules
from module_path import plots_data_path, mlruns_data_path

def mlflow_logger(func):
    """Decorator to automatically start and close an mlflow run"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #create a new experiment if not in mlruns directory
        mlruns_path = mlruns_data_path()
        mlflow.set_tracking_uri(mlruns_path)
        print(mlflow.get_artifact_uri())
        experiment_name = 'WIDS2025'

        try:
            exp_id = mlflow.create_experiment(name=experiment_name)
        except Exception as e:
            exp_id = mlflow.get_experiment_by_name(experiment_name).experiment_id

        with mlflow.start_run(experiment_id=exp_id):
            return func(*args, **kwargs)
    return wrapper


class ModelEvaluation:
    """
    Supports the evaluation of classification models (multinomial), collecting the results.
    """

    def __init__(self, X: pd.DataFrame, y: pd.Series, test_size: float = 0.3, shuffle: bool = True, random_state: int = 42):
        """
        :param X: the inputs
        :param y: the prediction targets
        :param test_size: the fraction of the data to reserve for testing
        :param shuffle: whether to shuffle the data prior to splitting
        :param random_state: the random seed
        """

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
            random_state=random_state, test_size=test_size, shuffle=shuffle)

    @mlflow_logger
    def evaluate_model(self, model) -> float:
        """
        :param model: the model to evaluate
        :return: the f1-score
        """
        model.fit(self.X_train, self.y_train)
        y_pred = model.predict(self.X_test)
        f1_score = metrics.f1_score(self.y_test, y_pred)
        print(f"{model}: f1_score={f1_score:.1f}")

        # log parameters and metrics in MLFlow
        mlflow.log_param("Model Type", type(model).__name__)
        for hyperparameter, value in model.get_params().items():
            mlflow.log_param(hyperparameter, value)
        mlflow.log_metric("f1_score", f1_score)
        signature = infer_signature(self.X_train, model.predict(self.X_train))
        mlflow.sklearn.log_model(model, "model", signature=signature)

        return f1_score