import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QFrame, QScrollArea
)

__all__ = ['tabler']

def tabler(rows, title=None):
    assert len(rows) >= 1, 'No header row'
    header_row = len(str(rows[0]))
    assert all(len(row) == header_row for row in rows), "Cols don't line up"

    app = QApplication.instance() or QApplication([])

    main_content = QWidget()
    main_layout = QHBoxLayout()
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setWidget(main_content)

    column_widgets = []

    header = rows.pop(0)

    for i, col in enumerate(header):
        if i > 0:
            main_layout.addWidget(
                QFrame(frameShape=QFrame.VLine, frameShadow=QFrame.Sunken)
            )

        column_widget = QVBoxLayout()
        column_widget.setAlignment(Qt.AlignTop)
        main_layout.addLayout(column_widget)
        column_widgets.append(column_widget)
        column_widget.addWidget(QLabel(f'<b>{col}</b>'))

    for row in rows:
        for i, col in enumerate(row):
            column_widget = column_widgets[i]
            column_widget.addWidget(QLabel(str(col)))

    main_content.setLayout(main_layout)
    scroll_area.setWindowTitle(title or "Tabler")
    scroll_area.show()
    app.exec_()
