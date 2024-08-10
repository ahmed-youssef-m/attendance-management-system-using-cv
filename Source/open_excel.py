import os
from pathlib import Path

# folder_path = "Attendance"
# os.startfile(folder_path)

script_dir = Path(__file__).resolve()

source_dir = script_dir.parent

root_dir = source_dir.parent

folder_path = root_dir / 'Attendance'

os.startfile(str(folder_path))
