def number_of_words(text):
    wrds = text.split()
    return len(wrds)

def count_characters(text):
    d = dict()
    for i in range(0,len(text)):
        l=(text[i]).lower()
        d[l] = d.get(l,0) + 1
    return d

def sort_on(itm):
    return itm["num"]

def list_char_dicts(char_counts_dict):
    l = []

    for k in char_counts_dict:
        #print("addding char" + k)
        #print("with count char" + str(char_counts_dict[k]))
        l.append({"char":k,"num":char_counts_dict[k]})
    #sort list
    #print("printing list")
    #print(l)
    #print("returning sorted list")
    l.sort(reverse=True, key=sort_on)
    return l