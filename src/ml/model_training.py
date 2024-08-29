from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(data, labels):
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return model, accuracy

if __name__ == "__main__":
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    labels = [0, 1, 0, 1]
    model, accuracy = train_model(data, labels)
    print(f"Model accuracy: {accuracy}")
