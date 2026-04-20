import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    ans = np.zeros(len(vocab),dtype=int)
    dict = {}

    for x in tokens:
        dict[x]= dict.get(x,0)+1

    for i,y in enumerate(vocab):
        ans[i]=dict.get(y,0)
        
    return ans
        
    pass