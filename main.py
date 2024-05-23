import fitz  # PyMuPDF
import pandas as pd
import re
import os  # Import the os module to handle file paths
import typer
from typing import List

app = typer.Typer()


@app.command()
def merge_csv_files(
    csv_files: List[str],
    output_file: str = typer.Option("./output.csv", help="Output file path"),
) -> None:
    """
    Merges several CSV files into one, ensuring unique IDs.

    Args:
        csv_files: A list of paths to the CSV files to merge.
        output_file: The path to save the merged CSV file.
    """
    dfs = []
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        # Ensure the 'id' column is numeric for sorting
        df["id"] = pd.to_numeric(df["id"], errors="coerce")
        # Sort by 'id' and drop duplicates
        df = df.sort_values(by="id").drop_duplicates(subset=["id"])
        dfs.append(df)

    # Concatenate all dataframes
    merged_df = pd.concat(dfs, ignore_index=True)

    # Save the merged dataframe to a CSV file
    merged_df.to_csv(output_file, index=False)
    typer.echo(f"Merged CSV saved to {output_file}")


@app.command()
def extract_and_save(
    pdf_path: str,
    csv_path: str = typer.Option(
        ".",
        help="Path to save the extracted items",
    ),
) -> None:
    """
    Extracts list items from a PDF and saves them to a CSV file.

    Args:
        pdf_path: The path to the PDF file.
        csv_path: The path to save the extracted items.
    """
    items = extract_list_items_from_pdf(pdf_path)
    save_items_to_csv(items, pdf_path, csv_path)
    typer.echo(f"Items saved to {csv_path}")


def extract_list_items_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    items = []

    # Pattern to match list items with various delimiters
    list_pattern = re.compile(r"^\s*([*-]|\d+\.)\s+(.*)")

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    line_text = " ".join(
                        [span["text"] for span in line["spans"]]
                    ).strip()
                    # Handle lines that might have excessive spaces
                    line_text = re.sub(r"\s+", " ", line_text)
                    match = list_pattern.match(line_text)
                    if match:
                        item_number, item_text = match.groups()
                        # Replace ";" or "," with slashes
                        item_text = item_text.replace(";", "/").replace(",", "/")
                        items.append(item_text.strip())

    return items


def save_items_to_csv(items, pdf_path, csv_path):
    # Extract the base name of the PDF file
    base_name = os.path.basename(pdf_path).split(".")[0]
    # Append the desired suffix to create the output filename
    csv_path = f"{base_name} items list output.csv"
    df = pd.DataFrame({"id": range(1, len(items) + 1), "items": items})
    df.to_csv(csv_path, index=False)
    print(f"Items saved to {csv_path}")  # Print the output path


if __name__ == "__main__":
    app()
