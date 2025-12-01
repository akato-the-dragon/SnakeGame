from os import system, listdir
from os.path import join, dirname, isfile


def convert(ui_directory: str, py_directory: str) -> None:
    for file_name in listdir(ui_directory):
        ui_file_path = join(ui_directory, file_name)
        py_file_name = file_name.replace(".ui", ".py")
        py_file_path = join(py_directory, py_file_name)

        if isfile(ui_file_path) and file_name.endswith(".ui"):
            print(f"Converting {ui_file_path}")
            status = system(f"PySide6-uic {ui_file_path} -o {py_file_path}")

            if status == 0:
                print(f"Ui {ui_file_path} converted")
            else:
                print(f"Ui {ui_file_path} converting failed. Exit code: {status}")


if __name__ == "__main__":
    ui_directory = dirname(__file__)
    py_directory = join(ui_directory, "../")

    convert(ui_directory, py_directory)

    input("Press enter for closing...")
