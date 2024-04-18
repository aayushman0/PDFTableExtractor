import sys
import ntpath
import pdfplumber
from pdfminer.pdfdocument import PDFPasswordIncorrect


def table_extraction(pdf: pdfplumber.PDF, file_name: str) -> None:
    """Extracts all available table form the PDF and saves it as CSV files in output/ folder.

    Args:
        pdf (pdfplumber.PDF): PDF object that is currently open.
        file_name (str): Name of the PDF file.
    """
    list_of_tables = list()
    with pdf:
        for pages in pdf.pages:
            list_of_tables += pages.extract_tables()

    if not list_of_tables:
        print(f"No table found in {file_name}")
        return None

    for i, table in enumerate(list_of_tables):
        with open(f"output/{file_name}_{i}.csv", "w", encoding="utf-8") as output_file:
            for row in table:
                for col_no, column in enumerate(row):
                    if column is None:
                        column = ""
                    if type(column) is str and "," in column:
                        column = f'"{column}"'
                    if type(column) is str and "\n" in column:
                        column = column.replace("\n", " ")
                    output_file.write(f"{',' if col_no != 0 else ''}{column}")
                output_file.write("\n")
    print(f"Outputs stored at output/{file_name}_xxx.csv")


def protected_pdf(file_path: str) -> None:
    """This function is called when the PDF has password protection.

    Args:
        file_path (str): Path to the PDF file.
    """
    print("Enter Password:", end=" ")
    password: str = input()
    try:
        pdf_file = pdfplumber.open(file_path, password=password)
    except PDFPasswordIncorrect:
        print("Incorrect Password!")
    else:
        file_name = ntpath.basename(file_path)
        table_extraction(pdf_file, file_name)


def main(file_path: str) -> None:
    """Main function called when running the application.

    Args:
        file_path (str): Path to the PDF file.
    """
    try:
        pdf_file = pdfplumber.open(file_path)
    except FileNotFoundError:
        print(f"{file_path} doesn't exist.")
    except PDFPasswordIncorrect:
        protected_pdf(file_path)
    else:
        file_name = ntpath.basename(file_path)
        table_extraction(pdf_file, file_name)


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("Please pass filepath to pdf.")
    else:
        file_path = argv[1]
        main(file_path=file_path)
