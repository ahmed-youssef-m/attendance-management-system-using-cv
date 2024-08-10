from PyQt5.QtWidgets import QApplication, QFileDialog
from pathlib import Path


class YourClass:
    def start(self):
        app = QApplication([])

        script_dir = Path(__file__)

        source_dir = script_dir.parent

        root_dir = source_dir.parent

        folder_path = root_dir / 'Resources'

        initial_dir_path = str(folder_path)
        dialog = QFileDialog()
        dialog.setDirectory(initial_dir_path)
        if dialog.exec_() == QFileDialog.Accepted:
            selected_files = dialog.selectedFiles()
            file_path = selected_files[0]
            return file_path

# your_instance = YourClass()
# your_instance.start()
