# bert_embeddings

Here is how to use it:
```python
from src import extract_features

brt = extract_features.BERT('uncased_L-24_H-1024_A-16/vocab.txt',
			'uncased_L-24_H-1024_A-16/bert_config.json',
			'uncased_L-24_H-1024_A-16/ert_model.ckpt')

temp_vectors = brt.get_vectors(["i see you", "you saw him"], True)

print(len(temp_vectors))
```
