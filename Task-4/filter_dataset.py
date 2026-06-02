import pandas as pd
import json

def dataset(input_file, output_file, filter):
    filtered_data=[]
    print("Starting the Process....")
    chunk_size=10000
    for chunk in pd.read_json(input_file, lines=True, chunksize=chunk_size):
        mask=chunk['categories'].str.contains(filter, na=False)
        filtered_data.append(chunk[mask])

    full_df=pd.concat(filtered_data)
    full_df.to_csv(output_file, index=False)
    print(f"Success!....Saved {len(full_df)} papers to {output_file}")

input_path=r"C:\Users\Admin\Downloads\arxiv-metadata-oai-snapshot.json"
output_path='Task-4/data/arxiv_subset/ai_papers.csv'

dataset(input_path, output_path, 'cs.AI')
