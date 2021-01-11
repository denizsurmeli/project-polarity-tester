

negations = ["not", "no", "don't", "didn't", "wasn't", "weren't", "can't",
             "couldn't", "isn't", "aren't", "haven't", "hasn't", "hadn't"]
# The list of punctuations to trim punctuations from words

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

#@TODO:Resolve last punctuation problem in first test
#@TODO:Is verifiying punctuation contained words necessary ?
output_sentence = ""
total_polarity=0
#Code starts under here
polarity_dictionary={}
with open("AFINN-en-165.txt","r") as polarity_scores:
    tl = polarity_scores.readlines()
    for line in tl:
        #Simply putting it to dictionary so access complexity can be O(1)
        line = line[:-1]
        pair=line.split("\t")
        polarity_dictionary[pair[0]] = pair[1]
    #Expecting garbage collector work after getting out from "with" statement since scope is closed.
def distribute_punctuation(text,punctuations):
    metaform_text = text
    if(punctuations):
        v = list(metaform_text)
        for key in punctuations.keys():
            v.insert(key,punctuations[key])
            metaform_text = ''.join(v)
    return metaform_text
user_input = input()
listed_input = user_input.split(" ")
restricted_list= ["",'',' '," "]

index_flag = 0
for item in listed_input:
    #using a dictionary, holding values as index:punctuation
    contains_punctuation=False
    hold_punctuation= {}
    pure_item = ""
    for letter in item:
        if letter in punctuations and letter!='\'':
            contains_punctuation=True
            hold_punctuation[item.index(letter)] = letter
    if contains_punctuation:
        pure_item= "".join([c for c in item if c not in punctuations])
    else:
        pure_item = item
    if pure_item in restricted_list:
        continue
    else:
        if index_flag == 0 and pure_item.lower() in polarity_dictionary.keys():
            total_polarity += int(polarity_dictionary[pure_item.lower()])
            listed_input[index_flag] = distribute_punctuation(pure_item.upper(),hold_punctuation)
        if index_flag > 0 and (pure_item.lower() in polarity_dictionary.keys()):
            if listed_input[index_flag-1] in negations:
                total_polarity += - int(polarity_dictionary[pure_item.lower()])
                listed_input[index_flag] = distribute_punctuation(pure_item.upper(), hold_punctuation)
                listed_input[index_flag-1] = listed_input[index_flag-1].upper()
            else:
                total_polarity += int(polarity_dictionary[pure_item.lower()])
                listed_input[index_flag] = distribute_punctuation(pure_item.upper(), hold_punctuation)
    index_flag += 1
output_sentence=" ".join(listed_input)
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print(output_sentence)
print(total_polarity)

