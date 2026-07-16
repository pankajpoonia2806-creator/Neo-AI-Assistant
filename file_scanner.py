import os


class FileScanner:

    @staticmethod
    def scan():

        folders = [
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Downloads"),
            os.path.expanduser("~/Pictures"),
            os.path.expanduser("~/Videos"),
        ]

        files = {}

        for folder in folders:

            if not os.path.exists(folder):
                continue

            print(f"Scanning {folder}")

            for root, _, filenames in os.walk(folder):

                for file in filenames:

                    name = file.lower()

                    files[name] = os.path.join(root, file)

        print(f"Found {len(files)} files")

        return files