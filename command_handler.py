from pc_control import PCControl
from app_launcher import AppLauncher


class CommandHandler:

    def __init__(self):
     
        self.launcher = AppLauncher()
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

        # Built-in commands
        if app in self.commands:
           return self.commands[app]()

        # AI App Launcher
        result = self.launcher.open(app)

        if result:
           return result

        return f"Sorry, I couldn't find '{app}'."