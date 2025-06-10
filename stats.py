# creates list of words in text and prints the count
def get_num_words(book_text):
     book_words = book_text.split()
     word_count = len(book_words)
     print(f"{word_count} words found in the document")