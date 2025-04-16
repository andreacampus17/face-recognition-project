import numpy as np


# Calculating Similarities
def compare_faces(encoding1, encoding2):
    dot_product = np.dot(encoding1, encoding2)
    norm_encoding1 = np.linalg.norm(encoding1)
    norm_encoding2 = np.linalg.norm(encoding2)
    similarity = dot_product / (norm_encoding1 * norm_encoding2)#Doing the cosine
    return similarity