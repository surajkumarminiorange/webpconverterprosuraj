import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.file_list import FileList
from ui.actions import AppActions


class WebPConverterApp(ctk.CTk, AppActions):

    def __init__(self):
        super().__init__()

        # ==================================================
        # Window Settings
        # ==================================================

        self.title("WebP Converter Pro")
        self.geometry("1100x700")
        self.minsize(950, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ==================================================
        # Application Data
        # ==================================================

        # Selected input images
        self.selected_files = []

        # None = Save beside original image
        self.output_folder = None

        # Supported image formats
        self.supported_extensions = {
            ".png",
            ".jpg",
            ".jpeg",
            ".bmp",
            ".tiff",
            ".tif",
            ".gif",
            ".avif",
            ".ico",
        }

        # ==================================================
        # Window Layout
        # ==================================================

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ==================================================
        # Sidebar
        # ==================================================

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # ----------------------------
        # Button Events
        # ----------------------------

        self.sidebar.browse_images_btn.configure(
            command=self.browse_images
        )

        self.sidebar.browse_folder_btn.configure(
            command=self.browse_folder
        )

        self.sidebar.output_button.configure(
            command=self.choose_output_folder
        )

        self.sidebar.convert_btn.configure(
            command=self.start_conversion
        )

        # ==================================================
        # File List
        # ==================================================

        self.file_list = FileList(self)

        self.file_list.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )