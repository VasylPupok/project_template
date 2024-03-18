from app.io.input import read_text, read_file, read_csv_pandas
from app.io.output import write_text, write_file, overwrite_file


def main():
    write_text(read_text("Print some text: "))
    write_file("data/output_file.txt", read_file("data/test.txt"))
    overwrite_file("data/overwritten_file.txt", read_csv_pandas("data/test.txt").to_string())


if __name__ == "__main__":
    main()
