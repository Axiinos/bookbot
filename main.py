def main():

    # Get path to book
    book_path = "books/frankenstein.txt"
    
    # Print the start of output
    print(f"--- Analyzing the book {book_path} --- \n")
        
        
    # Get the text from the book and count the words
    text = get_bok_text(book_path)
    word_c = word_count(text)
    print(f"Word Count:\n{word_c} number of words found in the book\n")
    
    # Count characters
    char_counts = character_count(text)
    
    # Sort the characters by their count
    print(f"Character Count: \n")
    sorting(char_counts)

    print(f"--- End of analysis ---")
    
def sorting(char_counts):
    
    # Sort the characters by their count
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print the sorted characters
    for char, count in sorted_chars:
        print(f"The letter {char} encountered : {count}\n")
    
    return sorted_chars

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