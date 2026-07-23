import customtkinter as ctk


class WebPConverterApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ----------------------------
        # Window Settings
        # ----------------------------
        self.title("WebP Converter Pro")
        self.geometry("1100x700")
        self.minsize(950, 650)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # ----------------------------
        # Build UI
        # ----------------------------
        self.create_widgets()

    def create_widgets(self):

        # =====================================
        # Main Window Layout
        # =====================================

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # =====================================
        # LEFT SIDEBAR
        # =====================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=260,
            corner_radius=0
        )

        self.sidebar.grid(row=0, column=0, sticky="ns")
        self.sidebar.grid_propagate(False)

        # Logo / Title

        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="🖼 WebP Converter Pro",
            font=("Segoe UI", 22, "bold")
        )

        self.title_label.pack(pady=(25, 5))

        self.subtitle = ctk.CTkLabel(
            self.sidebar,
            text="Batch Image Converter",
            font=("Segoe UI", 13)
        )

        self.subtitle.pack(pady=(0, 30))

        # Browse Buttons

        self.browse_images_btn = ctk.CTkButton(
            self.sidebar,
            text="📂 Browse Images",
            width=200
        )

        self.browse_images_btn.pack(pady=8)

        self.browse_folder_btn = ctk.CTkButton(
            self.sidebar,
            text="📁 Browse Folder",
            width=200
        )

        self.browse_folder_btn.pack(pady=8)

        # Quality

        quality_title = ctk.CTkLabel(
            self.sidebar,
            text="WebP Quality",
            font=("Segoe UI", 16, "bold")
        )

        quality_title.pack(pady=(35, 5))

        self.quality_slider = ctk.CTkSlider(
            self.sidebar,
            from_=1,
            to=100
        )

        self.quality_slider.set(80)

        self.quality_slider.pack(
            padx=20,
            fill="x"
        )

        self.quality_label = ctk.CTkLabel(
            self.sidebar,
            text="80%"
        )

        self.quality_label.pack(pady=5)

        # Output Folder

        output_title = ctk.CTkLabel(
            self.sidebar,
            text="Output Folder",
            font=("Segoe UI", 16, "bold")
        )

        output_title.pack(pady=(30, 5))

        self.output_entry = ctk.CTkEntry(
            self.sidebar,
            placeholder_text="Same as source"
        )

        self.output_entry.pack(
            padx=20,
            fill="x"
        )

        self.output_button = ctk.CTkButton(
            self.sidebar,
            text="Choose Folder"
        )

        self.output_button.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        # Convert Button

        self.convert_btn = ctk.CTkButton(
            self.sidebar,
            text="🚀 Convert",
            height=42,
            font=("Segoe UI", 15, "bold")
        )

        self.convert_btn.pack(
            side="bottom",
            padx=20,
            pady=20,
            fill="x"
        )

        # =====================================
        # RIGHT PANEL
        # =====================================

        self.content = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=15,
            pady=15
        )

        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_rowconfigure(1, weight=1)

        # Heading

        heading = ctk.CTkLabel(
            self.content,
            text="Selected Files",
            font=("Segoe UI", 24, "bold")
        )

        heading.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        # File List

        self.filebox = ctk.CTkTextbox(
            self.content,
            font=("Consolas", 14)
        )

        self.filebox.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.filebox.insert(
            "1.0",
            "No files selected.\n\n"
            "Click 'Browse Images' or 'Browse Folder' to begin.\n\n"
            "Drag & Drop support will be added soon."
        )

        # Progress

        self.progress = ctk.CTkProgressBar(
            self.content
        )

        self.progress.set(0)

        self.progress.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(5, 5)
        )

        # Status

        self.status = ctk.CTkLabel(
            self.content,
            text="Status : Ready",
            anchor="w"
        )

        self.status.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 15)
        )