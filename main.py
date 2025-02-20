
def main():
    book = read_book()
    print(book)

def read_book():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

main()
