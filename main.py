import os

def main():

    while True:
    
        # Get path to book
        try:
            book_path = str(input("Enter the path to the book: "))
            if not book_path:
                raise FileNotFoundError
            
            allowed_extensions = ['.txt', '.pdf', '.docx', '.doc', '.epub', '']
            _, ext = os.path.splitext(book_path)
            if ext not in allowed_extensions:
                print("Invalid file extension! Try again")
                continue
            
        except (FileNotFoundError, IsADirectoryError):
            print("Invalid path! Try again")
            continue
        # Print the start of output
        print(f"--- Analyzing the book {book_path} --- \n")
            
            
        # Get the text from the book and count the words
        text = get_book_text(book_path)
        if not text:
            print("Are you sure you entered the correct path to the book? Try again")
            continue
        word_c = word_count(text)
        print(f"Word Count:\n{word_c} number of words found in the book\n")
        
        # Count characters
        char_counts = character_count(text)
        
        # Sort the characters by their count
        print(f"Character Count: \n")
        sorting(char_counts)

        print(f"--- End of analysis ---\n\n")
        
        if str(input("Do you want to analyze another book? press Enter for yes or type in n for no : ")) == "n":
            break 
            
            
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
    
def get_book_text(path):
    
    # Get the text from the book
    try:
        with open(path, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Error reading the book: {e}")
        return None
    
    
main()