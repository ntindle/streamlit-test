import streamlit as st
import requests

# Base URL for the API
BASE_URL = "https://api.sample.com/v1"

st.title("Book Management System")

# List all books
if st.button("List Books"):
    response = requests.get(f"{BASE_URL}/books")
    if response.status_code == 200:
        books = response.json()
        st.dataframe(books)
    else:
        st.error("Failed to retrieve books")

# Create a new book
with st.form(key="new_book_form"):
    new_book_title = st.text_input("Book Title")
    new_book_author = st.text_input("Book Author")
    new_book_isbn = st.text_input("Book ISBN")
    submit_new_book = st.form_submit_button("Create Book")
    if submit_new_book:
        new_book_data = {
            "title": new_book_title,
            "author": new_book_author,
            "isbn": new_book_isbn,
        }
        response = requests.post(f"{BASE_URL}/books", json=new_book_data)
        if response.status_code == 201:
            st.success("Book created successfully")
        else:
            st.error("Failed to create a new book")

# Get, Update or Delete a book by ID
book_id = st.text_input("Enter Book ID for Details, Update or Delete")

if book_id:
    # Get book details
    if st.button("Get Book Details"):
        response = requests.get(f"{BASE_URL}/books/{book_id}")
        if response.status_code == 200:
            book_details = response.json()
            st.json(book_details)
        else:
            st.error("Failed to retrieve book details")

    # Update a book
    with st.form(key="update_book_form"):
        update_book_title = st.text_input("Update Book Title")
        update_book_author = st.text_input("Update Book Author")
        update_book_isbn = st.text_input("Update Book ISBN")
        submit_update_book = st.form_submit_button("Update Book")
        if submit_update_book:
            update_book_data = {
                "title": update_book_title,
                "author": update_book_author,
                "isbn": update_book_isbn,
            }
            response = requests.put(
                f"{BASE_URL}/books/{book_id}", json=update_book_data
            )
            if response.status_code == 200:
                st.success("Book updated successfully")
            else:
                st.error("Failed to update the book")

    # Delete a book
    if st.button("Delete Book"):
        response = requests.delete(f"{BASE_URL}/books/{book_id}")
        if response.status_code == 204:
            st.success("Book deleted successfully")
        else:
            st.error("Failed to delete the book")
