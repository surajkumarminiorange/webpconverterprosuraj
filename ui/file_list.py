import customtkinter as ctk
from pathlib import Path


class FileList(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, corner_radius=0)

        self.file_rows = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # -------------------------
        # Heading
        # -------------------------

        self.heading = ctk.CTkLabel(
            self,
            text="Selected Files",
            font=("Segoe UI", 24, "bold")
        )

        self.heading.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=(20, 10)
        )

        # -------------------------
        # File Table
        # -------------------------

        self.file_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=8
        )

        self.file_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=10
        )

        self.create_header()

        # -------------------------
        # Progress Bar
        # -------------------------

        self.progress = ctk.CTkProgressBar(self)

        self.progress.set(0)

        self.progress.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(5, 5)
        )

        # -------------------------
        # Status
        # -------------------------

        self.status = ctk.CTkLabel(
            self,
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

    # ======================================

    def create_header(self):

        header = ctk.CTkFrame(
            self.file_frame,
            fg_color="transparent"
        )

        header.pack(fill="x", pady=(0, 8))

        headers = [

            ("File", 300),

            ("Type", 80),

            ("Size", 100),

            ("Status", 140),

        ]

        for text, width in headers:

            ctk.CTkLabel(
                header,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 14, "bold")
            ).pack(side="left")

    # ======================================

    def clear(self):

        for row in self.file_rows:
            row.destroy()

        self.file_rows.clear()

    # ======================================

    def populate(self, files):

        self.clear()

        for file in files:

            path = Path(file)

            row = ctk.CTkFrame(
                self.file_frame,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                pady=2
            )

            size = path.stat().st_size / (1024 * 1024)

            ctk.CTkLabel(
                row,
                text=path.name,
                width=300,
                anchor="w"
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=path.suffix.upper().replace(".", ""),
                width=80
            ).pack(side="left")

            ctk.CTkLabel(
                row,
                text=f"{size:.2f} MB",
                width=100
            ).pack(side="left")

            status = ctk.CTkLabel(
                row,
                text="Waiting",
                width=140
            )

            status.pack(side="left")

            row.status_label = status

            self.file_rows.append(row)

    # ======================================

    def set_status(self, text):

        self.status.configure(text=text)

    # ======================================

    def set_progress(self, value):

        self.progress.set(value)

    # ======================================

    def update_row(self, index, text):

        if 0 <= index < len(self.file_rows):

            self.file_rows[index].status_label.configure(
                text=text
            )