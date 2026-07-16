import os


class FileSearch:

    def __init__(self):

        from file_scanner import FileScanner

        print("Scanning Files...")

        self.files = FileScanner.scan()

    def open(self, filename):

        filename = filename.lower().strip()

        # Exact Match
        if filename in self.files:

            os.startfile(self.files[filename])

            return f"Opening {filename}"

        # Partial Match
        for name, path in self.files.items():

            if filename in name:

                os.startfile(path)

                return f"Opening {name}"

        return None