from file_scanner import FileScanner
from file_index import FileIndex


def build():

    scanner = FileScanner()
    index = FileIndex()

    print("\nBuilding File Index...\n")

    index.clear()

    total = 0

    for name, path in scanner.scan():

        index.add(name, path)

        total += 1

        if total % 500 == 0:
            print(f"{total} files indexed...")

    index.save()

    print(f"\nFinished indexing {total} files.")


if __name__ == "__main__":

    build()