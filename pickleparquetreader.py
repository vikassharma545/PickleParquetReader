import os
import sys
from time import sleep, time
from psutil import process_iter
from pandas import read_parquet, read_pickle
import gc

file_path = sys.argv[1]
os.makedirs("C:\\.temp", exist_ok=True)
excel_file_path = f"C:\\.temp\\{os.path.splitext(os.path.basename(file_path))[0]}.csv"

if file_path.endswith('.parquet'):
    df = read_parquet(file_path)
elif file_path.endswith('.pkl') or file_path.endswith('.pickle'):
    df = read_pickle(file_path)
else:
    sys.exit(1)

df.to_csv(excel_file_path, index=False)

del df
gc.collect()
os.startfile(excel_file_path)

def is_excel_running():
    try:
        for proc in process_iter():
            if proc.name() == 'EXCEL.EXE':
                return any([f.path==excel_file_path for f in proc.open_files()])
    except:
        pass

    return False

start_time = time()
while not is_excel_running():
    if time() - start_time > 300:  # 5 minutes timeout
        break
    sleep(5)

while is_excel_running():
    sleep(5)

if os.path.exists(excel_file_path):
    os.remove(excel_file_path)