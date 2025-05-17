import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog,
    QLabel, QMessageBox, QInputDialog
)
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PDFTool(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Tool - Merge & Split")
        self.setGeometry(300, 200, 400, 300)

        layout = QVBoxLayout()

        self.info_label = QLabel("Choose what you want to do:")
        layout.addWidget(self.info_label)

        self.merge_btn = QPushButton("Merge PDFs")
        self.merge_btn.clicked.connect(self.merge_pdfs)
        layout.addWidget(self.merge_btn)

        self.split_btn = QPushButton("Split PDF (by page range)")
        self.split_btn.clicked.connect(self.split_pdf)
        layout.addWidget(self.split_btn)

        self.setLayout(layout)

    def merge_pdfs(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setNameFilter("PDF Files (*.pdf)")
        if dialog.exec_():
            files = dialog.selectedFiles()
            if files:
                try:
                    merger = PdfMerger()
                    for pdf in files:
                        merger.append(pdf)

                    output_file, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF", "", "PDF Files (*.pdf)")
                    if output_file:
                        if not output_file.endswith(".pdf"):
                            output_file += ".pdf"
                        merger.write(output_file)
                        merger.close()
                        QMessageBox.information(self, "Success", f"Merged PDF saved as:\n{output_file}")
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred while merging:\n{str(e)}")

    def split_pdf(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select a PDF to Split", "", "PDF Files (*.pdf)")
        if file:
            try:
                reader = PdfReader(file)
                total_pages = len(reader.pages)

                start, ok1 = QInputDialog.getInt(self, "Start Page", f"Enter start page (1 - {total_pages}):", 1, 1, total_pages)
                end, ok2 = QInputDialog.getInt(self, "End Page", f"Enter end page (1 - {total_pages}):", start, start, total_pages)

                if ok1 and ok2 and start <= end:
                    writer = PdfWriter()
                    for i in range(start - 1, end):
                        writer.add_page(reader.pages[i])

                    output_file, _ = QFileDialog.getSaveFileName(self, "Save Split PDF", "", "PDF Files (*.pdf)")
                    if output_file:
                        if not output_file.endswith(".pdf"):
                            output_file += ".pdf"
                        with open(output_file, "wb") as f:
                            writer.write(f)
                        QMessageBox.information(self, "Success", f"Split PDF saved as:\n{output_file}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred while splitting:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFTool()
    window.show()
    sys.exit(app.exec_())
