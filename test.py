import os
import io
from table_extractor import main as main_func


def test_file_path(capsys):
    main_func(file_path="pdfs/wrong_file.pdf")
    captured = capsys.readouterr()
    assert captured.out == "pdfs/wrong_file.pdf doesn't exist.\n"


def test_no_table(capsys):
    main_func(file_path="pdfs/pdf1.pdf")
    captured = capsys.readouterr()
    assert captured.out == "No table found in pdf1.pdf\n"
    output_exists = os.path.isfile("output/pdf1.pdf_0.csv")
    assert not output_exists


def test_corrupted(capsys):
    main_func(file_path="pdfs/corrupted.pdf")
    captured = capsys.readouterr()
    assert captured.out == "Corrupt PDF file detected.\n"
    output_exists = os.path.isfile("output/corrupted.pdf_0.csv")
    assert not output_exists


def test_wrong_password(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('12345'))
    main_func(file_path="pdfs/pdf5.pdf")
    captured = capsys.readouterr()
    assert captured.out == "Enter Password: Incorrect Password!\n"


def test_right_password(capsys, monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('123456'))
    main_func(file_path="pdfs/pdf5.pdf")
    captured = capsys.readouterr()
    assert captured.out == "Enter Password: Outputs stored at output/pdf5.pdf_xxx.csv\n"
    output_exists = os.path.isfile("output/pdf5.pdf_0.csv")
    assert output_exists


def test_normal_flow(capsys):
    main_func(file_path="pdfs/pdf2.pdf")
    captured = capsys.readouterr()
    assert captured.out == "Outputs stored at output/pdf2.pdf_xxx.csv\n"
    output_exists = os.path.isfile("output/pdf2.pdf_0.csv")
    assert output_exists
