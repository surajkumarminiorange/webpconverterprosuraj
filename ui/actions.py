import threading
import shlex
from pathlib import Path
from tkinter import filedialog

from converter import convert_image


class AppActions:

    # ==================================================
    # Common Add Files Method
    # ==================================================

    def add_files(self, files):

        added = False

        for file in files:

            file = Path(file)

            if file.is_dir():

                for img in file.rglob("*"):

                    if (
                        img.is_file()
                        and img.suffix.lower() in self.supported_extensions
                        and img not in self.selected_files
                    ):
                        self.selected_files.append(img)
                        added = True

            elif (
                file.is_file()
                and file.suffix.lower() in self.supported_extensions
                and file not in self.selected_files
            ):

                self.selected_files.append(file)
                added = True

        if added:

            self.file_list.populate(self.selected_files)

            self.file_list.set_status(
                f"{len(self.selected_files)} file(s) selected"
            )

            self.sidebar.convert_btn.configure(
                state="normal"
            )

    # ==================================================
    # Browse Images
    # ==================================================

    def browse_images(self):

        filetypes = [
            (
                "Supported Images",
                "*.png *.jpg *.jpeg *.bmp *.tiff *.tif *.gif *.avif *.ico"
            )
        ]

        files = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=filetypes
        )

        if not files:
            return

        self.add_files(files)

    # ==================================================
    # Browse Folder
    # ==================================================

    def browse_folder(self):

        folder = filedialog.askdirectory(
            title="Select Folder"
        )

        if not folder:
            return

        self.add_files([folder])

    # ==================================================
    # Drag & Drop
    # ==================================================

    def handle_drop(self, event):

        paths = shlex.split(event.data)

        self.add_files(paths)

    # ==================================================
    # Choose Output Folder
    # ==================================================

    def choose_output_folder(self):

        folder = filedialog.askdirectory(
            title="Select Output Folder"
        )

        if not folder:
            return

        self.output_folder = folder

        self.sidebar.set_output_folder(folder)

        self.file_list.set_status(
            "Output folder selected"
        )

    # ==================================================
    # Start Conversion
    # ==================================================

    def start_conversion(self):

        if not self.selected_files:
            return

        self.sidebar.convert_btn.configure(
            state="disabled"
        )

        self.file_list.set_progress(0)

        thread = threading.Thread(
            target=self.convert_images,
            daemon=True
        )

        thread.start()

    # ==================================================
    # Convert Images
    # ==================================================

    def convert_images(self):

        total = len(self.selected_files)

        success = 0

        quality = int(
            self.sidebar.quality_slider.get()
        )

        for index, file in enumerate(self.selected_files):

            self.file_list.update_row(
                index,
                "Processing..."
            )

            result, message = convert_image(
                file,
                output_folder=self.output_folder,
                quality=quality
            )

            if result:

                success += 1

                self.file_list.update_row(
                    index,
                    "Converted ✅"
                )

            else:

                self.file_list.update_row(
                    index,
                    "Failed ❌"
                )

            self.file_list.set_progress(
                (index + 1) / total
            )

            self.file_list.set_status(
                f"Converting {index + 1} of {total}"
            )

            self.update_idletasks()

        self.file_list.set_progress(1)

        self.file_list.set_status(
            f"Completed • {success}/{total} converted"
        )

        self.sidebar.convert_btn.configure(
            state="normal"
        )