def main():

    # Get path to book
    book_path = "books/frankenstein.txt"
        
    # Get the text from the book and count the words
    text = get_bok_text(book_path)
    print(f"Text from the book:\n {text}")
    
    word_c = word_count(text)
    print(f"{word_c} number of words found in the book")
    
    # Count characters
    char_counts = character_count(text)
    print("character counts:", char_counts)
    
def character_count(text):
    
    # initialize the count
    counts = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    
    # Count the characters in the Frankenstein book.
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        
        
    return counts

def word_count(text):
    
    # Count the words in the Frankenstein book.
    words = text.split()
    return len(words)
    
def get_bok_text(path):
    
    # Get the text from the book
    with open(path, "r") as file:
        return file.read()
    
main()