import hashlib
import os

# Load known virus signatures (MD5 hashes)
def load_signatures(signature_file):
    with open(signature_file, 'r') as f:
        return set(line.strip() for line in f if line.strip())

# Calculate the MD5 hash of a file
def md5_hash(file_path):
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        print(f"Could not read {file_path}: {e}")
        return None

# Scan a directory for infected files
def scan_directory(directory, signatures):
    for root, _, files in os.walk(directory):
        for name in files:
            file_path = os.path.join(root, name)
            file_hash = md5_hash(file_path)
            if file_hash and file_hash in signatures:
                print(f"[INFECTED] {file_path}")
            else:
                print(f"[CLEAN]    {file_path}")

if __name__ == "__main__":
    signatures = load_signatures("virus_signatures.txt")  # Each line: one MD5 hash
    directory_to_scan = input("Enter directory to scan: ")
    scan_directory(directory_to_scan, signatures)
