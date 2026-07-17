from file_index import FileIndex

db = FileIndex()

results = db.search("dbms")

print(results)