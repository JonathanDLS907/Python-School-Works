import hashlib
import os

# Adjusted directory path
recovered_dir = r"D:\Programming\CTF\deleted_files"

# Your target hashes
target_hashes = {
    "6cff6c25e4198e2b26fb5c7118694092ada6bdc7ef1a344b86d36929cd2d40f5",
    "5aa6d31bc63069d9e85f810a14d96e085d822b06b7de9516599aa3d209ba9614",
    "ae6448234393c9ccf7895c0b98e52dac65248eda15016b4b247e3fb1ef1087e3",
}

# Hash matching
for filename in os.listdir(recovered_dir):
    if filename.endswith(".txt"):
        filepath = os.path.join(recovered_dir, filename)
        with open(filepath, "rb") as f:
            content = f.read()
            file_hash = hashlib.sha256(content).hexdigest()
            if file_hash in target_hashes:
                print(f"✅ Match found: {filename}")
                print(f"📄 Full path: {filepath}")
                print(f"🔑 SHA-256: {file_hash}\n")
