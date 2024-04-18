# PDF Table Extractor
Extract tables from a PDF file and save it as CSV files.

- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Usage](#usage)
- [Special Cases](#special-cases)

## Requirements
1. Python
2. PIP
3. Git
4. CSV Viewer

## Project Setup
1. Clone the repo from github
2. Navigate to project directory using terminal
3. Create a virtual environment using Python
   ```
   > python -m venv venv
   ```
4. Activate the virtual environment<br>
   For windows:
   ```
   > .\venv\Scripts\Activate.ps1
   ```
   For Linux:
   ```
   > source ./venv/bin/activate
   ```
5. Install required python packages from requirements.txt
   ```
   > pip install -r requirements.txt
   ```

## Usage
- Execute the following command to run the application:
    ```
    > python table_extractor.py path/to/the/pdf/file.pdf
    ```
    <u>For example:</u><br>
    If the pdf file is named input.pdf and is located at the root of the project:
    ```
    > python table_extractor.py input.pdf
    ```
- The CSV files will be saved in output/ folder if any tables are present.
  ```
  Outputs stored at output/input.pdf_xxx.csv
  ```

## Special Cases
### Password protected PDF
- When the PDF is password protected, then the user needs to enter the password in the terminal when prompted.
  ```
  Enter Password: |
  ```
- If the password is wrong:
  ```
  Incorrect Password!
  ```

### Wrong/No file path
- If no file path is given during execution:
  ```
  Please input filepath of pdf.
  ``` 
- If the file path is wrong:
  ```
  path/to/file.pdf doesn't exist.
  ```

### Corrupted PDF
- If PDFException of PSException is during operation on the PDF file, then the file is assumed to be corrupted and following message is raised:
  ```
  Corrupt PDF file detected.
  ```
