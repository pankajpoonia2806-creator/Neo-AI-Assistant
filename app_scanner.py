import os


class AppScanner:

    @staticmethod
    def scan():

        folders = [
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
            os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"),
            os.path.expandvars(r"%USERPROFILE%\Desktop"),
            r"C:\Program Files",
            r"C:\Program Files (x86)"
        ]

        apps = {}

        for folder in folders:

            if not os.path.exists(folder):
                continue

            print(f"Scanning: {folder}")

            for root, _, files in os.walk(folder):

                for file in files:

                    if file.lower().endswith((".lnk", ".exe")):

                        name = os.path.splitext(file)[0].lower()

                        if name not in apps:
                            apps[name] = os.path.join(root, file)

        print(f"Found {len(apps)} apps")

        return apps