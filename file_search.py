import os

from file_index import FileIndex


class FileSearch:

    def __init__(self):

        self.index = FileIndex()

    def open(self, filename):

        filename = filename.lower().strip()

        print(f"\nSearching file: {filename}")

        results = self.index.search(filename)

        if not results:

            print("No file found.")

            return None

        name, path = results[0]

        print("Found:", path)

        if not os.path.exists(path):

            print("File missing from disk.")

            return "File exists in database but not on disk."

        try:

            os.startfile(path)

            return f"Opening {name}"

        except Exception as e:

            print(e)

            return str(e)