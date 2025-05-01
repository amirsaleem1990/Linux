from amir_analysis_functions import get_image_hash
import os
from PIL import Image
import imagehash
import pandas as pd
from collections import defaultdict
import pickle

hash_file_name = "/home/amir/.duplicates.pkl"
try:
    os.remove(hash_file_name)
except:
    pass

def get_image_hashes(directory):
    hashes = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                try:
                    path = os.path.join(root, file)
                    hashes[ get_image_hash(path) ].append(path)
                    pickle.dump(hashes, open(hash_file_name, 'wb'))
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    return hashes

def find_duplicates(hashes):
    """Return only hash groups with duplicates."""
    return {k: v for k, v in hashes.items() if len(v) > 1}

def save_results(duplicates, output_file="duplicates.csv"):
    """Save duplicates to a CSV file."""
    data = []
    for hash_key, paths in duplicates.items():
        data.append({"hash": hash_key, "count": len(paths), "paths": "; ".join(paths)})
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    directory = "path/to/your/images"  # Replace with your folder path
    print("Generating hashes...")
    hashes = get_image_hashes(directory)
    print("Finding duplicates...")
    duplicates = find_duplicates(hashes)
    print(f"Found {len(duplicates)} groups of duplicates.")
    save_results(duplicates)