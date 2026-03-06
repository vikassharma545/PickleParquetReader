import os
import sys
import tempfile
import uuid
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pyarrow.parquet as pq

def show_error(message):
    """Displays a graphical error message to the user, forced to the top layer."""
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True) # Ensures popup doesn't hide behind other windows
    messagebox.showerror("PickleParquetReader Error", message)
    root.destroy()

def convert_parquet_to_csv(input_path, output_path):
    """Reads and writes Parquet files in memory-safe chunks."""
    parquet_file = pq.ParquetFile(input_path)
    first_chunk = True
    
    # Avoids Out-of-Memory (OOM) crashes on large files
    for batch in parquet_file.iter_batches():
        df = batch.to_pandas()
        df.to_csv(output_path, mode='a', header=first_chunk, index=False)
        first_chunk = False

def convert_pickle_to_csv(input_path, output_path):
    """Loads a Pickle file into a DataFrame and saves to CSV."""
    df = pd.read_pickle(input_path)
    df.to_csv(output_path, index=False)

def main():
    try:
        # 1. Argument Validation
        if len(sys.argv) < 2:
            show_error("No input file provided. Please open a .pkl or .parquet file.")
            sys.exit(1)

        file_path = sys.argv[1]

        if not os.path.exists(file_path):
            show_error(f"File not found:\n{file_path}")
            sys.exit(1)

        ext = os.path.splitext(file_path)[1].lower()
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # 2. Concurrency Safety: Generate a unique temp file path
        temp_dir = tempfile.gettempdir()
        unique_id = uuid.uuid4().hex[:8]
        csv_file_path = os.path.join(temp_dir, f"{base_name}_{unique_id}.csv")

        # 3. Process Data based on type
        if ext == '.parquet':
            convert_parquet_to_csv(file_path, csv_file_path)
            
        elif ext in ['.pkl', '.pickle']:
            convert_pickle_to_csv(file_path, csv_file_path)
            
        else:
            show_error(f"Unsupported file extension: {ext}\nOnly .parquet and .pkl are supported.")
            sys.exit(1)

        # 4. Hand off to OS default CSV viewer (e.g., Excel)
        os.startfile(csv_file_path)
        
    except Exception as e:
        # Catch any pandas/pyarrow/memory errors and display them directly on screen
        show_error(f"An unexpected runtime error occurred:\n\n{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()