import re
import sys

def get_kernel_version(file_path):
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            match = re.search(b'Linux version (\\S+)', content)
            if match:
                version = match.group(1).decode('utf-8', errors='ignore')
                print(version)
    except FileNotFoundError:
        sys.exit(f"Error: File not found at {file_path}")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        kernel_file = sys.argv[1]
        get_kernel_version(kernel_file)
    else:
        get_kernel_version('kernel')
