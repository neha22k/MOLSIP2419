def count_words_chars_lines(revisionstry):
    try:
        # Open the file in read mode
        with open(revisionstry, 'r') as file:
            # Read the entire file
            contents = file.read()
            
            # Count words
            words = len(contents.split())
            
            # Count characters
            characters = len(contents)
            
            # Count lines
            lines = contents.count('\n') + 1
            
            print("Number of words:", words)
            print("Number of characters:", characters)
            print("Number of lines:", lines)
    except FileNotFoundError:
        print("File not found.")

# Example usage
filename = "C:/Users/prasa/Desktop/micrOrbitals/revision-word count/revisionstry.txt"  
count_words_chars_lines(filename)
