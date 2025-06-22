# PickleParquetReader

## Description

PickleParquetReader is a utility for viewing `.pkl` (pickle) and `.parquet` files in Microsoft Excel by converting them to CSV format.

## Prerequisites

- Python 3.x
- Git and MicrosoftExcel installed on your system
- Administrative privileges for setting up file associations
- Requirements:
   ```
   pip install pandas pyarrow psutil
   ```

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/vikassharma545/PickleParquetReader.git "C:/Program Files/PickleParquetReader"
   ```

   **Note:** clone into "C:/Program Files", you may need to run the command with administrative privileges due to permission restrictions on Windows.


## Setting Up File Associations
To automatically open `.pkl` and `.parquet` files with PickleParquetReader, you can set up file associations manually using the "Always use this app" option in Windows.

1. **Locate a `.pkl` or `.parquet` file** on your computer.
2. **Right-click** the file and select **"Open with"** > **"Choose another app."**
3. In the dialog box, select **"More apps"** if necessary, then choose **"Look for another app on this PC."**
4. Navigate to the location of `PickleParquetReader.bat`. For example:
   - If you cloned the repository to `C:\Program Files\PickleParquetReader`, the batch file is at `C:\Program Files\PickleParquetReader\PickleParquetReader.bat`.
5. Select the batch file and check the box that says **"Always use this app to open .pkl files"** (or `.parquet` files, depending on the file you selected).
6. Click **"OK"** to set the association.
7. **Repeat the process** for the other file type (`.parquet` if you started with `.pkl`, and vice versa).

After completing these steps, double-clicking a `.pkl` or `.parquet` file will launch `PickleParquetReader.bat`, which will open the file in Excel.