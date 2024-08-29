from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

def tune_hyperparameters(data, labels):
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }
    model = RandomForestClassifier()
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(data, labels)
    return grid_search.best_params_

if __name__ == "__main__":
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    labels = [0, 1, 0, 1]
    best_params = tune_hyperparameters(data, labels)
    print(f"Best hyperparameters: {best_params}")
