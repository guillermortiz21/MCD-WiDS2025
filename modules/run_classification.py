# Standar libraries
from datetime import datetime

# Scikit learn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA

# External modules
from module_path import test_data_path, train_data_path, plots_data_path
from module_data import Dataset
from module_model import ModelEvaluation


def main():
    # get current date and time
    start_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Start date & time : ", start_datetime)

    df = Dataset()
    df_train, df_test, labels = df.load_data_frame() # train dataframe, test dataframe, y targets dataframe

    targets = ['ADHD_Outcome',  'Sex_F']

    # evaluate models (adhd)
    ev = ModelEvaluation(X=df_train, y=labels[targets[0]])
    ev.evaluate_model(LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=1000))

    # evaluate models (sex_f)
    ev = ModelEvaluation(X=df_train, y=labels[targets[1]])
    ev.evaluate_model(LogisticRegression(solver='lbfgs', multi_class='multinomial', max_iter=1000))
    


if __name__ == '__main__':
    main()