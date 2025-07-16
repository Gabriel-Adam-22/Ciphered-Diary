from cryptography.hazmat.primitives import hashes

def txt_to_hash(txt: str):
    """
    ### Hasher
    takes a word and returns its hash
    """
    digest = hashes.Hash(hashes.SHA256())
    digest.update(txt.encode())
    return digest.finalize().hex()

if __name__ == "__main__":
    txt_to_hash