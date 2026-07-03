def count_lines_and_words(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()

        lines = content.splitlines()
        words = content.split()

        print(f"\nNumber of lines: {len(lines)}")
        print(f"Number of words: {len(words)}")

    except FileNotFoundError:
        print("File not found!")
    
    except Exception:
        print("Something went wrong!")


if __name__ == "__main__":
    filename = input("Enter a filename: ")
    count_lines_and_words(filename)