from ui.main_window import WebPConverterApp
from windows.splash import SplashScreen


if __name__ == "__main__":

    app = WebPConverterApp()

    # Hide main window
    app.withdraw()

    # Show Splash Screen
    SplashScreen(app)

    # Start Application
    app.mainloop()