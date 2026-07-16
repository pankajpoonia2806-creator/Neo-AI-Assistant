from pc_control import PCControl


class CommandHandler:

    def __init__(self):

        self.commands = {
            "chrome": PCControl.open_chrome,
            "notepad": PCControl.open_notepad,
            "calculator": PCControl.open_calculator,
            "explorer": PCControl.open_explorer,
            "vscode": PCControl.open_vscode,
            "vs code": PCControl.open_vscode,
        }

    def handle(self, user_input):

        lower = user_input.lower().strip()

        print("Command:", lower)

        if lower.startswith("open "):

            app = lower.replace("open ", "").strip()

            print("App:", app)

            command = self.commands.get(app)

            print("Found:", command)

            if command:
                return command()

        return None