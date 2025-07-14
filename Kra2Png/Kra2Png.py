import os
from krita import Krita, Extension, InfoObject
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QLabel
from PyQt5.QtCore import QTimer, Qt

class Kra2PngExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("Kra2Png", "Export all KRA files in folder as PNG")
        action.triggered.connect(self.select_folders)


    def show_toast(self, message, duration=3000, parent=None):
        if parent is None:
            parent = Krita.instance().activeWindow().qwindow()

        toast = QLabel(message, parent)
        toast.setWindowFlags(
            Qt.ToolTip | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint
        )
        toast.setStyleSheet("""
            QLabel {
                background-color: rgba(30, 30, 30, 230);
                color: white;
                padding: 10px 15px;
                border-radius: 8px;
                font-size: 12pt;
            }
        """)
        toast.adjustSize()

        # Center on screen or parent
        screen_geometry = toast.screen().geometry()
        x = screen_geometry.center().x() - toast.width() // 2
        y = screen_geometry.top() + 100
        toast.move(x, y)

        toast.show()
        QTimer.singleShot(duration, toast.close)


    def select_folders(self):
        # Step 1: Prompt the user to select the folder containing .kra files
        folder_path = QFileDialog.getExistingDirectory(
            None,
            "Step 1: Select Folder Containing .kra Files",
            "",
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        # Step 2: Create a new folder in the same directory as the selected folder
        if folder_path:
            output_folder = os.path.join(folder_path, "Exported_PNGs")

        # Check if either folder path is empty
        if not folder_path or not output_folder:
            QMessageBox.warning(QWidget(), "Selection Error", "Export process abandoned.")
            return

        # Call the export function with the selected folders
        self.batch_export(folder_path, output_folder)

    def batch_export(self, folder_path, output_folder):
        app = Krita.instance()

        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)

        # Iterate through each file in the folder
        for filename in os.listdir(folder_path):
            if filename.endswith(".kra"):
                file_path = os.path.join(folder_path, filename)
                
                # Open the document
                document = app.openDocument(file_path)
                
                # Check if the document was opened successfully
                if document:
                    print(f"File {filename} opened successfully")

                    self.show_toast(f"Exporting {filename} to PNG...")

                    
                    # Set the active document
                    app.setActiveDocument(document)


                    document.setBatchmode(True)
                    
                    # Create and configure InfoObject for export settings
                    export_info = InfoObject()
                    export_info.setProperty("alpha", True)  # Enable transparency
                    export_info.setProperty("compression", 9)  # Set compression level (0-9 for PNG)
                    
                    # Export the document as PNG
                    png_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")
                    document.exportImage(png_path, export_info)
                    
                    # Close the document
                    document.close()

                else:
                    print(f"Failed to open file {filename}")

        QMessageBox.information(QWidget(), "Export Complete", "Batch export completed.")


    

    

# Register the extension with Krita
app = Krita.instance()
extension = Kra2PngExtension(app)
app.addExtension(extension)