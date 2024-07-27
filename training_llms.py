import torch
from typing import List, Tuple

class solution:
    def batch_loader(self, raw_dataset, context_length, batch_size):
        torch.manual_seed(0)
        list_of_words = raw_dataset.split()
        indices = torch.randint( low=0, high=len(list_of_words)-context_length, size=batch_size,).to_list()

        X=[]
        Y=[]

        for idx in indices:
            X.append(list_of_words[idx: idx + context_length])
            Y.append(list_of_words[idx: idx+1+ context_length])