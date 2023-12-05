import sqlite3


# @flaskapp.route("/")
# def index():
#     name = request.args.get("name")
#     author = request.args.get("author")
#     read = bool(request.args.get("read"))

#     if name:
#         cursor.execute(
#             "SELECT * FROM books WHERE name LIKE :name", {"name": f"%{name}%"}
#         )
#         books = [Book(*row) for row in cursor]

#     elif author:
#         cursor.execute(
#             "SELECT * FROM books WHERE author LIKE :author", {"author": f"%{author}%"}
#         )
#         books = [Book(*row) for row in cursor]

#     else:
#         cursor.execute("SELECT name, author, read FROM books")
#         books = [Book(*row) for row in cursor]

#     return render_template("books.html", books=books)


database_uri = ":memory"

database = sqlite3.connect(database_uri, check_same_thread=False)
cursor = database.cursor()

cursor.execute()

name = "jan"

if name:
    cursor.execute("SELECT * FROM books WHERE name LIKE :name", {"name": f"%{name}%"})

else:
    cursor.execute("SELECT name, author, read FROM books")
