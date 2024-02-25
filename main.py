def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    cdict = {}
    for char in text:
        if char.isalpha():
            if char in cdict:
                cdict[char] += 1
            else:
                cdict[char] = 1
    return cdict

def print_report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print()
    dict_list = [{"letter": k, "count": v} for k,v in count_letters(text).items()]
    dict_list.sort(reverse=True, key=lambda x: x["count"])
    for item in dict_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as file:
        text = file.read()

    print_report(text)
    
    
if __name__ == "__main__":
    main()