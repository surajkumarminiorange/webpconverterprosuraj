import sys
import ctypes
from ui.main_window import WebPConverterApp
from windows.splash import SplashScreen


if __name__ == "__main__":

    # Set explicit AppUserModelID so Windows taskbar uses custom app icon
    if sys.platform == "win32":
        try:
            myappid = "surajkumar.webpconverterpro.app.1.0"
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass

    app = WebPConverterApp()

    # Hide main window
    app.withdraw()

    # Show Splash Screen
    SplashScreen(app)

    # Start Application
    app.mainloop()