import markovify
"""
    Simple test kit for polarity project. Using NLTK and Markov Chains
    we will generate random word groups(not sentences, since we do not have 
    such obligation) and test our algorithms. Some base constraints:
        <1>)Inputs will be processed word by word.
        <2>)The output will contain two values:
            <2.1>) The mutated sentence with full punctuation.
            <2.2>) Polarity score of given input. 
                @EXAMPLE:return (output_sentence,polarity_score)
        <3>)Test suit will need your algorithm to be wrapped in a function, 
        and return a pair based on mentioned constraints <2.1>,<2.2>.
        <4>)The Github page will contain more detailed information about usage
        and installation.
        <5>)Have fun ! We are just helping out each other, no need for worries such 
        as:"They are so far ahead","I suck at programming",etc.
    
"""


#for calculating polarity scores
negations = ["not", "no", "don't", "didn't", "wasn't", "weren't", "can't",
             "couldn't", "isn't", "aren't", "haven't", "hasn't", "hadn't"]
# The list of punctuations to trim punctuations from words

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

#generated sentences and their polarity scores will be contained in a list of tuples.
#we will clean the data from their polarity scores in the beginning
polarity_dictionary={}
with open("AFINN-en-165.txt","r") as polarity_scores:
    with open("AFINN-en-165-CLEAN.txt","w") as words:
        tl = polarity_scores.readlines()
        for line in tl:
            #Simply putting it to dictionary so access complexity can be O(1)
            line = line[:-1]
            pair=line.split("\t")
            polarity_dictionary[pair[0]] = pair[1]
            words.write(pair[0]+'\n')


generated_sentences=[]
def polarity_score(get):
    output_sentence = ""
    total_polarity = 0
    # Code starts under here
    polarity_dictionary = {}
    with open("AFINN-en-165.txt", "r") as polarity_scores:
        tl = polarity_scores.readlines()
        for line in tl:
            # Simply putting it to dictionary so access complexity can be O(1)
            line = line[:-1]
            pair = line.split("\t")
            polarity_dictionary[pair[0]] = pair[1]
        # Expecting garbage collector work after getting out from "with" statement since scope is closed.
        # IT does not. I really hate python, you damn memory monster
    # def insert(string, index, element):
    #     return string[:index] + element + string[index:]

    def distribute_punctuation(text, punctuations):
        metaform_text = text
        if (punctuations):
            v = list(metaform_text)
            for key in punctuations.keys():
                v.insert(key, punctuations[key])
                metaform_text = ''.join(v)
        return metaform_text

    user_input = get
    listed_input = user_input.split(" ")
    restricted_list = ["", '', ' ', " "]

    index_flag = 0
    for item in listed_input:
        # using a dictionary, holding values as index:punctuation
        contains_punctuation = False
        hold_punctuation = {}
        pure_item = ""
        for letter in item:
            if letter in punctuations and letter != '\'':
                contains_punctuation = True
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
                listed_input[index_flag] = distribute_punctuation(pure_item.upper(), hold_punctuation)
            if index_flag > 0 and (pure_item.lower() in polarity_dictionary.keys()):
                if listed_input[index_flag - 1] in negations:
                    total_polarity += - int(polarity_dictionary[pure_item.lower()])
                    listed_input[index_flag] = distribute_punctuation(pure_item.upper(), hold_punctuation)
                    listed_input[index_flag - 1] = listed_input[index_flag - 1].upper()
                else:
                    total_polarity += int(polarity_dictionary[pure_item.lower()])
                    listed_input[index_flag] = distribute_punctuation(pure_item.upper(), hold_punctuation)
        index_flag += 1
    output_sentence = " ".join(listed_input)
    return output_sentence,total_polarity

def generate_sentences(path_to_file,n):
    '''
    :param n: Number of sentences to generate
    :return: Tuple(Mutated sentence, Polarity Score)
    '''
    with open("tale-of-two-cities-text.txt") as f:
        text = f.read()

    text_model = markovify.Text(text)
    with open(path_to_file,"w") as write_to:
        for i in range(n):
            generated = text_model.make_short_sentence(280)
            sentence,score = polarity_score(generated)
            write_to.write(generated+"\t"+sentence+"\t"+str(score)+"\n")

generate_sentences("navi-desvita.txt",300)



