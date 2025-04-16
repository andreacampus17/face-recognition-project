import matplotlib
matplotlib.use('TkAgg')  # Configura il backend
from sklearn.metrics import auc
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import det_curve



def plot_roc_curve(fpr_list, tpr_list):
    plt.figure(figsize=(8, 6))
    plt.plot(fpr_list, tpr_list, linestyle='-', color='b', label='ROC Curve')
    roc_auc = auc(fpr_list, tpr_list)
    plt.plot([0, 1], [0, 1], linestyle='--', color='r', label='Random Curve')  #  #Random curve
    plt.xlabel('False Positives Rate (FPR)')
    plt.ylabel(' True Positives Rate (TPR)')
    plt.title(f'Receiver Operating Characteristics(ROC)- AUC: {roc_auc:.2f}')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.close()




def plot_similarity_distributions(similarity_scores_match, similarity_scores_non_match):

    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.hist(similarity_scores_match, bins=50, alpha=0.5, label='Genuine', color='g', density=True, histtype='step')
    plt.hist(similarity_scores_non_match, bins=50, alpha=0.5, label='Impostors', color='r', density=True, histtype='step')
    plt.xlabel('Score')
    plt.ylabel('Density')
    plt.title('Score Distributions')
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.show()
    plt.close()


def plot_cmc_curve(similarity_results, bool_similarity_results, k_values):

    # Estract the dictionary values
    bool_similarity_values = list(bool_similarity_results.values())

    #Sorts the scores by similarity score in increasing order
    sorted_indices = np.argsort(similarity_results)[::-1]
    sorted_labels = np.array(bool_similarity_values)[sorted_indices]

    # Calculating the CMC
    cmc = np.zeros(len(k_values))
    for i, k in enumerate(k_values):
        cmc[i] = np.sum(sorted_labels[:k]) / np.sum(bool_similarity_values)

    # Creazione del grafico
    plt.figure(figsize=(10, 6))
    plt.plot(k_values, cmc, linestyle='-', color='b')
    plt.xlabel('rank')
    plt.ylabel('Recognition Rate')
    plt.title('Cumulative Match Characteristics (CMC)')
    plt.grid(True)
    plt.show()
    plt.close()

def plot_det_curve(fpr, fnr):

    plt.figure(figsize=(10, 6))
    plt.plot(fpr, fnr, linestyle='-', color='b')
    plt.xlabel('False Positive Rate')
    plt.ylabel('False Negative Rate')
    plt.title(' Detection Error Trade Off (DET)')
    plt.grid(True)
    plt.show()
    plt.close()