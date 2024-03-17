import shutil

def file_compress_decompress(file_to_compress):
    shutil.compress_file(file_to_compress)
    print(f"File compressed: {file_to_compress}.gz")
