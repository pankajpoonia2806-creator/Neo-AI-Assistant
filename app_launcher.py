import os
import subprocess

from app_scanner import AppScanner


class AppLauncher:

    def __init__(self):

        print("Scanning Windows Apps...")

        self.apps = AppScanner.scan()

        print(f"Loaded {len(self.apps)} applications.")

    def open(self, app_name):

        app_name = app_name.lower().strip()

        # Exact Match
        if app_name in self.apps:
            return self.launch(self.apps[app_name], app_name)

        # Partial Match
        for name, path in self.apps.items():

            if app_name in name:
                return self.launch(path, name)

        return None

    def launch(self, path, name):

        try:

            if path.endswith(".lnk"):
                os.startfile(path)

            else:
                subprocess.Popen(path)

            return f"Opening {name.title()}."

        except Exception as e:

            return str(e)