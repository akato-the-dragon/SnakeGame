"""
"""

# Import modules
from typing import Any
from PySide6.QtWidgets import QLabel


def insert_data(label: QLabel, data: Any, separator: str = ":") -> None:
    text, _data = label.text().split(separator)
    
    label.setText(f"{text}{separator} {data}")
