from transformers import AutoModel, AutoTokenizer

BART = AutoModel.from_pretrained("facebook/bart-large")
print(BART)

