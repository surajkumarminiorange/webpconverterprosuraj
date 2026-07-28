# pyrefly: ignore [missing-import]
import customtkinter as ctk
from pathlib import Path


class FileList(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=12,
            fg_color="#18181b"
        )

        self.file_rows = []

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Color mapping for format badges
        self.format_colors = {
            "PNG": "#38bdf8",
            "JPG": "#34d399",
            "JPEG": "#34d399",
            "AVIF": "#c084fc",
            "BMP": "#f43f5e",
            "TIFF": "#fbbf24",
            "TIF": "#fbbf24",
            "GIF": "#a78bfa",
            "ICO": "#38bdf8",
        }

        # ==================================================
        # Header Bar (Title + Batch Size Badge)
        # ==================================================

        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(16, 8)
        )

        self.heading = ctk.CTkLabel(
            self.header_frame,
            text="Selected Files (0)",
            font=("Segoe UI", 18, "bold"),
            text_color="#f4f4f5"
        )
        self.heading.pack(side="left")

        self.summary_badge = ctk.CTkLabel(
            self.header_frame,
            text="",
            font=("Segoe UI", 12, "bold"),
            text_color="#60a5fa"
        )
        self.summary_badge.pack(side="right")

        # ==================================================
        # File Scrollable Container
        # ==================================================

        self.file_frame = ctk.CTkScrollableFrame(
            self,
            corner_radius=10,
            fg_color="#202023",
            scrollbar_button_color="#27272a",
            scrollbar_button_hover_color="#3f3f46"
        )

        self.file_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=16,
            pady=8
        )

        # Show empty state placeholder initially
        self.show_placeholder()

        # ==================================================
        # Footer Progress Bar & Status Log
        # ==================================================

        self.progress = ctk.CTkProgressBar(
            self,
            height=8,
            corner_radius=4,
            progress_color="#2563eb",
            fg_color="#27272a"
        )
        self.progress.set(0)

        self.progress.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=20,
            pady=(8, 4)
        )

        self.status = ctk.CTkLabel(
            self,
            text="Status: Ready",
            anchor="w",
            font=("Segoe UI", 12),
            text_color="#a1a1aa"
        )

        self.status.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 14)
        )

    # ==================================================
    # Empty State Placeholder
    # ==================================================

    def show_placeholder(self):
        for widget in self.file_frame.winfo_children():
            widget.destroy()

        placeholder_card = ctk.CTkFrame(
            self.file_frame,
            fg_color="transparent"
        )
        placeholder_card.pack(expand=True, fill="both", pady=80)

        icon_label = ctk.CTkLabel(
            placeholder_card,
            text="📥",
            font=("Segoe UI", 52)
        )
        icon_label.pack(pady=(0, 10))

        title = ctk.CTkLabel(
            placeholder_card,
            text="Add Images to Convert",
            font=("Segoe UI", 18, "bold"),
            text_color="#e4e4e7"
        )
        title.pack(pady=(0, 4))

        subtitle = ctk.CTkLabel(
            placeholder_card,
            text="Use Files or Folder on the sidebar to select images",
            font=("Segoe UI", 13),
            text_color="#a1a1aa"
        )
        subtitle.pack(pady=(0, 16))

        # Supported Formats Pills
        tags_frame = ctk.CTkFrame(placeholder_card, fg_color="transparent")
        tags_frame.pack()

        for ext in ["PNG", "JPG", "AVIF", "BMP", "TIFF", "GIF"]:
            color = self.format_colors.get(ext, "#94a3b8")
            pill = ctk.CTkFrame(
                tags_frame,
                fg_color="#18181b",
                border_width=1,
                border_color=color,
                corner_radius=6
            )
            pill.pack(side="left", padx=4)
            ctk.CTkLabel(
                pill,
                text=ext,
                font=("Segoe UI", 10, "bold"),
                text_color=color
            ).pack(padx=8, pady=2)

    # ==================================================
    # Table Header Row
    # ==================================================

    def create_header(self):
        header = ctk.CTkFrame(
            self.file_frame,
            fg_color="#18181b",
            corner_radius=6,
            height=34
        )
        header.pack(fill="x", pady=(0, 6), padx=2)

        ctk.CTkLabel(
            header,
            text="File Name",
            anchor="w",
            font=("Segoe UI", 12, "bold"),
            text_color="#a1a1aa"
        ).pack(side="left", padx=(12, 0), expand=True, fill="x")

        for text, width in [("Format", 75), ("Status", 130)]:
            ctk.CTkLabel(
                header,
                text=text,
                width=width,
                anchor="w",
                font=("Segoe UI", 12, "bold"),
                text_color="#a1a1aa"
            ).pack(side="left")

        # Header for Actions column
        ctk.CTkLabel(
            header,
            text="Actions",
            width=160,
            anchor="center",
            font=("Segoe UI", 12, "bold"),
            text_color="#a1a1aa"
        ).pack(side="right", padx=(0, 10))

    # ==================================================
    # Size Formatter
    # ==================================================

    def format_size(self, size):
        if size < 1024:
            return f"{size} B"
        elif size < 1024 ** 2:
            return f"{size / 1024:.1f} KB"
        elif size < 1024 ** 3:
            return f"{size / (1024 ** 2):.2f} MB"
        return f"{size / (1024 ** 3):.2f} GB"

    # ==================================================
    # Clear File List
    # ==================================================

    def clear(self):
        for row in self.file_rows:
            row.destroy()

        self.file_rows.clear()
        self.heading.configure(text="Selected Files (0)")
        self.summary_badge.configure(text="")
        self.progress.set(0)
        self.status.configure(text="Status: Ready")
        self.show_placeholder()

    # ==================================================
    # Populate Files
    # ==================================================

    def populate(self, files, statuses=None):
        for widget in self.file_frame.winfo_children():
            widget.destroy()

        self.file_rows.clear()
        total_bytes = sum(Path(f).stat().st_size for f in files if Path(f).exists())
        size_str = self.format_size(total_bytes)

        self.heading.configure(text=f"Selected Files ({len(files)})")
        self.summary_badge.configure(text=f"Total: {size_str}")

        self.create_header()

        for index, file in enumerate(files):
            path = Path(file)
            ext = path.suffix.upper().replace(".", "")
            format_col = self.format_colors.get(ext, "#94a3b8")
            status_text = (statuses or {}).get(path, "Waiting")

            row = ctk.CTkFrame(
                self.file_frame,
                fg_color="#18181b" if index % 2 == 0 else "#252528",
                corner_radius=6,
                height=34
            )
            row.pack(fill="x", pady=2, padx=2)

            # File Name Label
            ctk.CTkLabel(
                row,
                text=path.name,
                anchor="w",
                font=("Segoe UI", 12),
                text_color="#f4f4f5"
            ).pack(side="left", padx=(12, 0), expand=True, fill="x")

            # Format Badge Pill
            format_badge = ctk.CTkFrame(
                row,
                fg_color="#0f172a",
                border_width=1,
                border_color=format_col,
                corner_radius=4,
                width=55,
                height=22
            )
            format_badge.pack(side="left", padx=(0, 20))
            format_badge.pack_propagate(False)

            ctk.CTkLabel(
                format_badge,
                text=ext,
                font=("Segoe UI", 10, "bold"),
                text_color=format_col
            ).pack(expand=True)

            # Status Label
            is_converted = "Converted" in status_text or "✅" in status_text
            is_failed = "Failed" in status_text or "❌" in status_text

            status_col = "#4ade80" if is_converted else ("#f87171" if is_failed else "#a1a1aa")

            status = ctk.CTkLabel(
                row,
                text=status_text,
                width=130,
                font=("Segoe UI", 12),
                text_color=status_col
            )
            status.pack(side="left")
            row.status_label = status

            # Action Buttons Container (Convert + Remove)
            actions_frame = ctk.CTkFrame(row, fg_color="transparent")
            actions_frame.pack(side="right", padx=(5, 8))

            convert_btn = ctk.CTkButton(
                actions_frame,
                text="⚡ Convert",
                width=72,
                height=26,
                corner_radius=5,
                fg_color="#059669",
                hover_color="#047857",
                font=("Segoe UI", 11, "bold"),
                command=lambda idx=index: self.master.convert_single_file(idx)
            )
            convert_btn.pack(side="left", padx=(0, 6))

            remove_btn = ctk.CTkButton(
                actions_frame,
                text="✕ Remove",
                width=72,
                height=26,
                corner_radius=5,
                fg_color="#dc2626",
                hover_color="#b91c1c",
                font=("Segoe UI", 11, "bold"),
                command=lambda idx=index: self.master.remove_file(idx)
            )
            remove_btn.pack(side="left")

            self.file_rows.append(row)

    # ==================================================
    # Status & Progress Helpers
    # ==================================================

    def set_status(self, text):
        self.status.configure(text=f"Status: {text}")

    def set_progress(self, value):
        self.progress.set(value)

    def update_row(self, index, text):
        if 0 <= index < len(self.file_rows):
            status_label = self.file_rows[index].status_label
            status_label.configure(text=text)
            if "Converted" in text or "✅" in text:
                status_label.configure(text_color="#4ade80")
            elif "Failed" in text or "❌" in text:
                status_label.configure(text_color="#f87171")
            elif "Processing" in text:
                status_label.configure(text_color="#60a5fa")