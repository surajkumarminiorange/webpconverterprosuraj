import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            width=260,
            corner_radius=0
        )

        self.grid_propagate(False)

        # ==================================================
        # Title
        # ==================================================

        self.title_label = ctk.CTkLabel(
            self,
            text="🖼 WebP Converter Pro",
            font=("Segoe UI", 22, "bold")
        )

        self.title_label.pack(
            pady=(25, 5)
        )

        self.subtitle = ctk.CTkLabel(
            self,
            text="Batch Image Converter",
            font=("Segoe UI", 13)
        )

        self.subtitle.pack(
            pady=(0, 30)
        )

        # ==================================================
        # Browse Buttons
        # ==================================================

        self.browse_images_btn = ctk.CTkButton(
            self,
            text="📂 Browse Images",
            height=38
        )

        self.browse_images_btn.pack(
            padx=20,
            pady=6,
            fill="x"
        )

        self.browse_folder_btn = ctk.CTkButton(
            self,
            text="📁 Browse Folder",
            height=38
        )

        self.browse_folder_btn.pack(
            padx=20,
            pady=6,
            fill="x"
        )

        # ==================================================
        # Quality
        # ==================================================

        self.quality_title = ctk.CTkLabel(
            self,
            text="WebP Quality",
            font=("Segoe UI", 16, "bold")
        )

        self.quality_title.pack(
            pady=(30, 5)
        )

        self.quality_slider = ctk.CTkSlider(
            self,
            from_=1,
            to=100,
            command=self.update_quality
        )

        self.quality_slider.set(80)

        self.quality_slider.pack(
            padx=20,
            fill="x"
        )

        self.quality_label = ctk.CTkLabel(
            self,
            text="80%"
        )

        self.quality_label.pack(
            pady=5
        )

        # ==================================================
        # Output Folder
        # ==================================================

        self.output_title = ctk.CTkLabel(
            self,
            text="Output Folder",
            font=("Segoe UI", 16, "bold")
        )

        self.output_title.pack(
            pady=(30, 5)
        )

        self.output_entry = ctk.CTkEntry(
            self,
            placeholder_text="Same as source",
            state="readonly"
        )

        self.output_entry.pack(
            padx=20,
            fill="x"
        )

        self.output_button = ctk.CTkButton(
            self,
            text="📁 Choose Folder",
            height=36
        )

        self.output_button.pack(
            padx=20,
            pady=(10, 5),
            fill="x"
        )

        # ==================================================
        # Open Output Folder
        # ==================================================

        self.open_output_btn = ctk.CTkButton(
            self,
            text="📂 Open Output Folder",
            height=36,
            state="disabled"
        )

        self.open_output_btn.pack(
            padx=20,
            pady=(5, 5),
            fill="x"
        )

        # ==================================================
        # Clear All
        # ==================================================

        self.clear_btn = ctk.CTkButton(
            self,
            text="🗑️ Clear All",
            height=36,
            fg_color="#C0392B",
            hover_color="#A93226"
        )

        self.clear_btn.pack(
            padx=20,
            pady=(5, 20),
            fill="x"
        )

        # ==================================================
        # Convert Button
        # ==================================================

        self.convert_btn = ctk.CTkButton(
            self,
            text="🚀 Convert",
            height=45,
            state="disabled",
            font=("Segoe UI", 15, "bold")
        )

        self.convert_btn.pack(
            side="bottom",
            padx=20,
            pady=20,
            fill="x"
        )

    # ==================================================
    # Update Quality Label
    # ==================================================

    def update_quality(self, value):

        self.quality_label.configure(
            text=f"{int(value)}%"
        )

    # ==================================================
    # Set Output Folder
    # ==================================================

    def set_output_folder(self, folder_path: str):

        self.output_entry.configure(state="normal")

        self.output_entry.delete(0, "end")

        self.output_entry.insert(0, folder_path)

        self.output_entry.configure(state="readonly")

        self.open_output_btn.configure(
            state="normal"
        )

    # ==================================================
    # Clear Output Folder
    # ==================================================

    def clear_output_folder(self):

        self.output_entry.configure(state="normal")

        self.output_entry.delete(0, "end")

        self.output_entry.configure(state="readonly")

        self.open_output_btn.configure(
            state="disabled"
        )