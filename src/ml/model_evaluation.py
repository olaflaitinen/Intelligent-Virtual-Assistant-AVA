from sklearn.metrics import classification_report

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    return report

if __name__ == "__main__":
    # Assuming model, X_test, y_test are already defined
    report = evaluate_model(model, X_test, y_test)
    print(report)
