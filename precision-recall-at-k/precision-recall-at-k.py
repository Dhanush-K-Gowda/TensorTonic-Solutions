import numpy as np

def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended = np.asarray(recommended)
    relevant = np.asarray(relevant)

    hits = np.intersect1d(recommended[:k], relevant)
    precision  = len(hits)/k
    recall = len(hits)/len(relevant) if len(relevant) > 0 else 0
    return [precision ,recall]