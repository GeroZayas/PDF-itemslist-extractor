# 📄 PDF and CSV Utility Tool

A versatile tool designed to streamline the extraction of list items from PDF documents and the merging of CSV files, ensuring unique identification across datasets.

## 🛠️ Features

- **Extract Items from PDF**: Convert list-like structures in PDF documents into structured CSV format.
- **Merge CSV Files**: Combine multiple CSV files into a single file, maintaining unique IDs through a newly generated sequential ID column.

## 🖥️ Prerequisites

- Python 3.6+
- PyMuPDF (fitz)
- Pandas
- Typer

## 🚀 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/GeroZayas/PDF-itemslist-extractor.git

cd PDF-itemslist-extractor

pip install -r requirements.txt
```

## 📝 Usage

Extract Items from PDF

```bash
python your_script_name.py extract_and_save./path/to/your/pdf/file.pdf./desired/output/path/

```

Merge Multiple CSV Files

```bash
python your_script_name.py merge_csv_files./file1.csv./file2.csv./merged_output.csv
```

## 📁 Example

Assuming you have a PDF named **_example.pdf_** and two CSV files named **_data1.csv_** and **_data2.csv_**, you can extract items from the PDF and merge the CSV files as follows:

```bash
python your_script_name.py extract_and_save./example.pdf./extracted_items.csv

python your_script_name.py merge_csv_files./data1.csv./data2.csv./merged_data.csv
```

## 🎯 Contributing

Contributions are welcome Feel free to submit a pull request or open an issue to discuss improvements or report bugs.

## 👤 Author

Gero Zayas - @gerozayas

## 📧 Contact

gerozayas@gmail.com
