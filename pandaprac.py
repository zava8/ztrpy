import pandas as pd
# trows = pd.read_csv("./dset/eng_hindi_translate_J5_s1.csv")
# print(trows)
import kagglehub

# Download latest version
path = kagglehub.dataset_download("aiswaryaramachandran/hindienglish-corpora")

print("Path to dataset files:", path)
"/home/viml/.cache/kagglehub/datasets/aiswaryaramachandran/hindienglish-corpora/versions/1/Hindi_English_Truncated_Corpus.csv"
output_path='./dset/eng_hindi_translate_J5_s1.csv'
