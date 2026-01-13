import os

TEMP_DIR = "/home/username/temp"

def cleanup_temp():
    for filename in os.listdir(TEMP_DIR):
        path = os.path.join(TEMP_DIR, filename)
        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception as e:
            print(f"Error deleting {path}: {e}")

if __name__ == "__main__":
    cleanup_temp()

