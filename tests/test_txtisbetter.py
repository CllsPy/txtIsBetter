
from unittest.mock import mock_open, patch
from io import StringIO
import pytest

def test_load_pdf(capsys):
    # Mock file content
    fake_pdf_content = "This is a test PDF content."

    # Mock the 'open' function
    with patch("builtins.open", mock_open(read_data=fake_pdf_content)):
        loadPdf("dummy.pdf")  # Call the function with a dummy file name

    # Capture printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == fake_pdf_content
