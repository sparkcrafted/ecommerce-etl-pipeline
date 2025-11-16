import pandas as pd

def split_csv(input_path, output_prefix, rows_per_file=100000):
    chunk_iter = pd.read_csv(input_path, chunksize=rows_per_file)
    for i, chunk in enumerate(chunk_iter):
        chunk.to_csv(f"{output_prefix}_part{i+1}.csv", index=False)
        print(f"Created {output_prefix}_part{i+1}.csv")

files_to_split = [
    "amazon/train.csv",
    "amazon/test.csv",
    "amazon/amazon_review_polarity_csv/test.csv",
    "amazon/amazon_review_polarity_csv/train.csv",
    "google/events1.csv",
    "google/items.csv",
    "google/users.csv",
]

for file_path in files_to_split:
    prefix = file_path.split('/')[-1].replace('.csv', '')
    split_csv(file_path, prefix, 10000)
