import os
import webbrowser


class PCControl:

    @staticmethod
    def open_chrome():
        try:
            chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

            if os.path.exists(chrome):
                os.startfile(chrome)
            else:
                webbrowser.open("https://google.com")

            return "Opening Chrome."

        except Exception as e:
            return str(e)

    @staticmethod
    def open_notepad():
        os.system("start notepad")
        return "Opening Notepad."

    @staticmethod
    def open_calculator():
        os.system("start calc")
        return "Opening Calculator."

    @staticmethod
    def open_explorer():
        os.system("start explorer")
        return "Opening File Explorer."

    @staticmethod
    def open_vscode():
        try:
            os.system("code")
            return "Opening VS Code."
        except:
            return "VS Code not found."