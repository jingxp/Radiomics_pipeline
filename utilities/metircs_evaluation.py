import numpy as np
from sklearn.metrics import confusion_matrix,  accuracy_score, balanced_accuracy_score


def conf_matrix(y_true, y_pred):
    
    target_labels = np.array(y_true)
    predictions = np.array(y_pred)
    matrix = confusion_matrix(target_labels, predictions)
    
    return matrix


def metrics(y_true, y_pred):
    
    # tp = conf_matrix[1][1]
    # tn = conf_matrix[0][0]
    # fp = conf_matrix[0][1]
    # fn = conf_matrix[1][0]

    
    accuracy = accuracy_score(y_true, y_pred)
    balanced_acc_score = balanced_accuracy_score(y_true, y_pred)
    #sensitivity = (tp / float(tp + fn))
    #specificity = (tn / float(tn + fp))

    return accuracy, balanced_acc_score
