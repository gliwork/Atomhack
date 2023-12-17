import numpy as np

frame_file_path = r"C:\Users\rohht\Downloads\Трубы\Трубы\DATASET\FRAMES\frame0000.frame"

# Try different encodings if 'utf-8' does not work
try:
    # Attempt to read with 'utf-8' encoding
    matrix = np.loadtxt(frame_file_path, delimiter=',', encoding='utf-8')
except UnicodeDecodeError:
    # If 'utf-8' fails, you can try another encoding here
    matrix = np.loadtxt(frame_file_path, delimiter=',', encoding='latin1')

print(matrix)
