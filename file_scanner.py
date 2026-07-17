import os

# Files that Neo will index
SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".xlsx",
    ".xls",
    ".ppt",
    ".pptx",
    ".csv",
    ".py",
    ".json",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".mp3",
    ".wav",
    ".mp4",
    ".mkv",
    ".avi",
    ".zip",
    ".rar",
    ".7z",
}

# Folders to skip
SKIP_FOLDERS = {
    "$Recycle.Bin",
    "System Volume Information",
    "__pycache__",
    ".git",
    ".venv",
    "venv",
}


class FileScanner:

    @staticmethod
    def scan():

        print("\n========== Neo File Scanner ==========")

        folders = [
            os.path.expanduser("~/Desktop"),
            os.path.expanduser("~/Documents"),
            os.path.expanduser("~/Downloads"),
            os.path.expanduser("~/Pictures"),
            os.path.expanduser("~/Videos"),
            os.path.expanduser("~/Music"),
        ]

        # Scan OneDrive if available
        one_drive = os.path.expanduser("~/OneDrive")

        if os.path.exists(one_drive):
            folders.append(one_drive)

        total = 0

        for folder in folders:

            if not os.path.exists(folder):
                continue

            print(f"Scanning: {folder}")

            try:

                for root, dirs, files in os.walk(folder):

                    # Skip unnecessary folders
                    dirs[:] = [
                        d for d in dirs
                        if d not in SKIP_FOLDERS
                    ]

                    for file in files:

                        ext = os.path.splitext(file)[1].lower()

                        if ext not in SUPPORTED_EXTENSIONS:
                            continue

                        total += 1

                        yield (
                            file.lower(),
                            os.path.join(root, file)
                        )

            except PermissionError:
                continue

            except Exception as e:
                print(f"Error scanning {folder}: {e}")

        print(f"\nIndexed {total} files.")
        print("========== Scan Complete ==========\n")