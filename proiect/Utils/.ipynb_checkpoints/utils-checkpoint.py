import os

def clear_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        print(f"[ERROR] Error removing file: {e}")

def handle_error(message, exception=None):
    if exception:
        print(f"[ERROR] {message}: {exception}")
    else:
        print(message)
    return message