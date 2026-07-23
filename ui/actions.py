import threading
from pathlib import Path
from tkinter import filedialog

from converter import convert_image


class AppActions:

    # -----------------------------
    # Browse Images
    # -----------------------------

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

        self.selected_files = list(files)

        self.file_list.populate(self.selected_files)

        self.file_list.set_status(
            f"Status : {len(self.selected_files)} file(s) selected"
        )

        self.sidebar.convert_btn.configure(
            state="normal"
        )

    # -----------------------------
    # Browse Folder
    # -----------------------------

    def browse_folder(self):

        folder = filedialog.askdirectory(
            title="Select Folder"
        )

        if not folder:
            return

        folder = Path(folder)

        self.selected_files = []

        for file in folder.rglob("*"):

            if (
                file.is_file()
                and file.suffix.lower() in self.supported_extensions
            ):

                self.selected_files.append(file)

        self.file_list.populate(
            self.selected_files
        )

        self.file_list.set_status(
            f"Status : {len(self.selected_files)} image(s) found"
        )

        self.sidebar.convert_btn.configure(
            state="normal" if self.selected_files else "disabled"
        )

    # -----------------------------
    # Start Thread
    # -----------------------------

    def start_conversion(self):

        self.sidebar.convert_btn.configure(
            state="disabled"
        )

        thread = threading.Thread(
            target=self.convert_images,
            daemon=True
        )

        thread.start()

    # -----------------------------
    # Convert Images
    # -----------------------------

    def convert_images(self):

        total = len(self.selected_files)

        if total == 0:
            return

        self.file_list.set_progress(0)

        success = 0

        quality = self.sidebar.quality_slider.get()

        for index, file in enumerate(self.selected_files):

            self.file_list.update_row(
                index,
                "Processing..."
            )

            result, message = convert_image(
                file,
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
                f"Converting {index+1}/{total}"
            )

            self.update()

        self.file_list.set_status(
            f"Completed • {success}/{total} converted"
        )

        self.sidebar.convert_btn.configure(
            state="normal"
        )