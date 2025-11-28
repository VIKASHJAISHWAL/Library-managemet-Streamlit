import streamlit as st

# --- Your Code, Not Modified: Only Converted for Streamlit UI ---
class Library:
    def __init__(self):
        self.books = []
        self.issue_books = {}

    def Add_books(self, book_name):
        self.books.append(book_name)
        return "Book added successfully!"

    def Remove_books(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            return "Book removed!"
        else:
            return "Book not found!"

    def Issue_books(self, book_name, student):
        if book_name in self.books:
            self.issue_books[book_name] = student
            self.books.remove(book_name)
            return "Book Issued Successfully!"
        else:
            return "Book not Available!"

    def Return_books(self, book_name):
        if book_name in self.issue_books:
            self.books.append(book_name)
            del self.issue_books[book_name]
            return "Book returned successfully!"
        else:
            return "This book was not issued!"

    def Show_all_books(self):
        if len(self.books) == 0:
            return ["No books available!"]
        else:
            return self.books


# ---------- Streamlit UI ----------
st.title("📚 Library Management System !")

# Create single library object
if "lib" not in st.session_state:
    st.session_state.lib = Library()

lib = st.session_state.lib

menu = st.radio("Choose an option:", 
    ["Add Book", "Remove Book", "Issue Book", "Return Book", "Show All Books"]
)

st.write("---")

# ADD BOOK
if menu == "Add Book":
    name = st.text_input("Enter book name to add:")
    if st.button("Add"):
        msg = lib.Add_books(name)
        st.success(msg)

# REMOVE BOOK
elif menu == "Remove Book":
    name = st.text_input("Enter book name to remove:")
    if st.button("Remove"):
        msg = lib.Remove_books(name)
        st.info(msg)

# ISSUE BOOK
elif menu == "Issue Book":
    name = st.text_input("Enter book name to issue:")
    student = st.text_input("Enter student name:")
    if st.button("Issue"):
        msg = lib.Issue_books(name, student)
        st.success(msg)

# RETURN BOOK
elif menu == "Return Book":
    name = st.text_input("Enter book name to return:")
    if st.button("Return"):
        msg = lib.Return_books(name)
        st.warning(msg)

# SHOW ALL BOOKS
elif menu == "Show All Books":
    st.subheader("Available Books:")
    books = lib.Show_all_books()
    for b in books:
        st.write("•", b)
