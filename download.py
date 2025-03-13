import requests
import os
import sys
from tqdm import tqdm

# Define file paths
originals_file = 'originals.txt'
photoshops_file = 'photoshops.txt'
originals_save_path = 'originals'
photoshops_save_path = 'photoshops'
error_log = 'error_log.txt'

# Create directories if not exist
os.makedirs(originals_save_path, exist_ok=True)
os.makedirs(photoshops_save_path, exist_ok=True)

def down_pic(down_url, save_path, picname):
    """Download an image and save it to the specified path"""
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(down_url, headers=header, timeout=10)
        response.raise_for_status()
        with open(os.path.join(save_path, f"{picname}.png"), "wb") as f:
            f.write(response.content)
    except Exception as e:
        with open(error_log, "a") as log:
            log.write(f"Error downloading {down_url}: {str(e)}\n")

def download_images(file_path, save_path):
    """Read URLs from a file and download images"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            url_list = [line.strip() for line in f.readlines()]
        
        for i, url in enumerate(tqdm(url_list, desc=f"Downloading {file_path}")):
            down_pic(url, save_path, i + 1)
    
    except Exception as e:
        with open(error_log, "a") as log:
            log.write(f"Error reading {file_path}: {str(e)}\n")

if __name__ == "__main__":
    download_images(originals_file, originals_save_path)
    download_images(photoshops_file, photoshops_save_path)
