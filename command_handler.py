from pc_control import PCControl
from app_launcher import AppLauncher
from website_launcher import WebsiteLauncher
from file_search import FileSearch


class CommandHandler:

    def __init__(self):

        self.launcher = AppLauncher()
        self.file_search = FileSearch()

        self.commands = {
            "chrome": PCControl.open_chrome,
            "notepad": PCControl.open_notepad,
            "calculator": PCControl.open_calculator,
            "calc": PCControl.open_calculator,
            "explorer": PCControl.open_explorer,
            "vscode": PCControl.open_vscode,
            "vs code": PCControl.open_vscode,
        }

    def handle(self, user_input):

        lower = user_input.lower().strip()

        if lower.startswith(("open ", "launch ", "start ")):

            app = (
                lower.replace("open ", "")
                     .replace("launch ", "")
                     .replace("start ", "")
                     .strip()
            )

            # ---------------- Built-in Commands ---------------- #

            if app in self.commands:
                return self.commands[app]()

            # ---------------- Website Launcher ---------------- #

            result = WebsiteLauncher.open(app)

            if result:
                return result

            # ---------------- Windows App Launcher ---------------- #

            result = self.launcher.open(app)

            if result:
                return result

            # ---------------- AI File Search ---------------- #

            result = self.file_search.open(app)

            if result:
                return result

            return f"Sorry, I couldn't find '{app}'."

        return None