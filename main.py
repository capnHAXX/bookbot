def main():
    book_path = get_path()
    print(f"statistics for {book_path}")
    book_text = read_text(book_path)
    word_count(book_text)
    char_count = char_counter(book_text)
    a_list = alpha_dlist(char_count)
    prt_alphalist(a_list)
        

# pulls path to frankenstein
def get_path():
    book_path = "books/frankenstein.txt"
    return book_path

# creates list of words in text and prints the count
def word_count(book_text):
     book_words = book_text.split()
     word_count = len(book_words)
     print(f"Total word count = {word_count}")
     
# reads and returns the entire text   
def read_text(book_path):
    with open(book_path) as f:
         book_text = f.read()
         return book_text

# counts characters and adds character:count to char_count dictionary
def char_counter(sample_text):
    char_count = {}
    for char in sample_text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

# creates list of only alphabetical dicitionaries [{character:char,num:n},...] and sorts it in descending numerical
def alpha_dlist(char_count):
    a_list = []
    for a in char_count:
        a_dict = {}
        if a.isalpha():
                n = char_count[a]
                a_dict = {"character":a,"num":n}
                a_list.append(a_dict)
    a_list.sort(reverse = True,key = sort_on)
    return a_list

# defines sorting value for previous
def sort_on(a_list):
    return a_list["num"]

#prints the alphabetical dictionaries
def prt_alphalist(a_list):
    for d in a_list:
        char = d["character"]
        num = d["num"]
        print(f"The '{char}' character was found {num} times")

main()