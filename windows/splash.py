import customtkinter as ctk
from PIL import Image


class SplashScreen(ctk.CTkToplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        # -----------------------------
        # Window
        # -----------------------------

        self.overrideredirect(True)

        width = 600
        height = 360

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = int((screen_width - width) / 2)
        y = int((screen_height - height) / 2)

        self.geometry(f"{width}x{height}+{x}+{y}")

        self.configure(fg_color="#1e1e1e")

        # -----------------------------
        # Main Frame
        # -----------------------------

        container = ctk.CTkFrame(
            self,
            corner_radius=20,
            fg_color="#252526"
        )

        container.pack(
            expand=True,
            fill="both",
            padx=8,
            pady=8
        )

        # -----------------------------
        # App Icon
        # -----------------------------

        icon = Image.open("assets/icon.ico")

        self.logo = ctk.CTkImage(
            light_image=icon,
            dark_image=icon,
            size=(80, 80)
        )

        ctk.CTkLabel(
            container,
            image=self.logo,
            text=""
        ).pack(pady=(35, 15))

        # -----------------------------
        # Title
        # -----------------------------

        ctk.CTkLabel(
            container,
            text="WebP Converter Pro",
            font=("Segoe UI", 30, "bold")
        ).pack()

        ctk.CTkLabel(
            container,
            text="Fast • Modern • Batch Image Converter",
            font=("Segoe UI", 15),
            text_color="#bfbfbf"
        ).pack(pady=(5, 25))

        # -----------------------------
        # Version
        # -----------------------------

        ctk.CTkLabel(
            container,
            text="Version 1.0.0",
            font=("Segoe UI", 14)
        ).pack()

        # -----------------------------
        # Developer
        # -----------------------------

        ctk.CTkLabel(
            container,
            text="Developed by Surajvansh",
            font=("Segoe UI", 15)
        ).pack(pady=(10, 0))

        ctk.CTkLabel(
            container,
            text="Powered by miniOrange",
            font=("Segoe UI", 13),
            text_color="#9d9d9d"
        ).pack()

        # -----------------------------
        # Loading
        # -----------------------------

        self.loading_label = ctk.CTkLabel(
            container,
            text="Loading...",
            font=("Segoe UI", 13)
        )

        self.loading_label.pack(pady=(35, 8))

        self.progress = ctk.CTkProgressBar(
            container,
            width=420,
            height=12,
            corner_radius=10
        )

        self.progress.pack()

        self.progress.set(0)

        # -----------------------------
        # Start Animation
        # -----------------------------

        self.after(50, self.animate)

    # ==================================================

    def animate(self):

        value = self.progress.get()

        if value < 1:

            value += 0.02

            self.progress.set(value)

            self.after(35, self.animate)

        else:

            self.destroy()

            self.parent.deiconify()