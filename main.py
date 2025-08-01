from stats import number_of_words,count_characters,list_char_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    


    fname=sys.argv[1] #'books/frankenstein.txt'
    text = get_book_text(fname)
    cnt = number_of_words(text)
    #print(f'{cnt} words found in the document')
    d_char = count_characters(text)
    #print(d_char)
    #print("new dict:")
    l=list_char_dicts(d_char)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {fname}...')
    print('----------- Word Count ----------')
    print(f'Found {cnt} total words')
    print('--------- Character Count -------')
    for n in l:
        a=n["char"]
        c=n["num"]

        if a.isalpha():
            print(f'{a}: {c}')
            #e: 44538
            #t: 29493
    print('============= END ===============')

main()