from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import log_loss
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from creds import RAW_DATA_S3_LINK

import pandas as pd

def compute(test_row):
    df = pd.read_csv(RAW_DATA_S3_LINK)

    # First we'll do department...
    lb = preprocessing.LabelBinarizer()
    lb.fit(df.department)
    #print(lb.classes_)
    department = lb.transform(df.department)
    #print(department[0:2])
    #print(type(department))
    df_dep = pd.DataFrame(data = department, columns = lb.classes_)
    df_dep.columns = ['dep_' + str(col) for col in df_dep.columns]
    df_dep.head()

    # And Next We'll do Salary
    lb = preprocessing.LabelBinarizer()
    lb.fit(df.salary)
    salary = lb.transform(df.salary)
    #print(department[0:2])
    #print(type(department))
    df_sal = pd.DataFrame(data = salary, columns = lb.classes_)
    df_sal.columns = ['sal_' + str(col) for col in df_sal.columns]
    df_sal.head()

    df_od = pd.concat([df, df_sal], axis=1)
    df_od = pd.concat([df_od, df_dep], axis=1)
    df_od = df_od.drop('salary', axis = 1)
    df_od = df_od.drop('department', axis = 1)
    df_od.head()

    target = df_od['employee_left_company']
    new_df = df_od.drop('employee_left_company', axis = 1)

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(new_df, target, test_size = 0.25, random_state = 0)

    # different parameteres to tune
    parameters_rf = {'n_estimators':[10, 50, 100, 200, 300], 'random_state':[0]}

    # Creating a Random Forest classifier using grid search to identify optimal tuning for algo.
    rand_forest_clf = RandomForestClassifier()
    cv_rf = GridSearchCV(rand_forest_clf, parameters_rf)

    #rand_forest_clf = RandomForestClassifier(n_estimators=200, random_state=0)
    cv_rf = cv_rf.fit(X_train, y_train)
    # print("Best estimator: ", cv_rf.best_estimator_)

    # test_row that is passed in should be here, and pred returned!
    #pred = cv_rf.predict_proba(X_test)[:,1]
    #return pred[1]
    twod = [test_row]
    pred = cv_rf.predict_proba(twod)[:,1]
    print(pred)
    return pred[0]
