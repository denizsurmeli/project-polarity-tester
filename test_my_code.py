"""
MELIH GIBI INTIHAL YAPMAYALIM:
    The MARKOV CHAIN GENERATOR used in this code:https://github.com/jsvine/markovify @author:https://www.jsvine.com/

    Rest of the code is property of CMPE150, but you should not copy any code from other files since TeachingCodes will capture your INTIHAL.


    Cases generated in this code are styled as in example input's style. Do not expect to generate cases like "Th&*s thi**s we a#re,, doing some"3 things like yo@#u",
    There is a little chance since the mentioned case would generate enormous amounts of edge cases which is not rational when you think that we are in CMPE150, an
    introductry course.

    I hope that we can benefit this tool one way or another, if you want to test your code manually the generated sentences will contain in file navi-desvita.txt.
    The format will be INPUT // EXPECTED-OUTPUT //SCORE
    T
"""

import polarity_case_generator
negations = ["not", "no", "don't", "didn't", "wasn't", "weren't", "can't",
             "couldn't", "isn't", "aren't", "haven't", "hasn't", "hadn't"]
# The list of punctuations to trim punctuations from words

punctuations = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def my_code(get):
    #INSTRUCTIONS ABOUT USAGE(EN):
    #Between the lines DO_NOT_EDIT_ANYTHING_XXXX_THIS_LINE you have your code.Copy&Paste it after this line.
    #After doing that at some point you need to get input from user. BE CAREFUL: YOU NEED TO REPLACE variable = input() with variable = get.
    #get is the paramater that passing input, testing your code is dependent on whether correct input passed or not.
    #At this point you must hold your formatted(uppercased words) sentence in a variable called "output_sentence" and the polarity score in a variable called "total_polarity.
    #YOU MUST RETURN THEM in this function such:(Add the next line to the end of this function)
    #   return output_sentence,total_polarity.



def run_tests(n):
    #This function generates test cases for your code.
    #n is the number of cases you want to test, the code will automatically create sentences for you to test your code.
    p,f,c = 0,0,0
    print("Generating "+str(n)+" cases... --> foxy-tests.txt")
    polarity_case_generator.generate_sentences("foxy-tests.txt",n)
    print("Running tests...")
    with open("foxy-tests.txt") as cases:
        lines = cases.readlines()
        for line in lines:
            temp = line.split("\t")
            user_input,expected_output,polarity_score = temp[0],temp[1],temp[2]
            user_output,user_score = my_code(user_input)
            if user_score == int(polarity_score) and expected_output == user_output:
                p+=1
                print("+++CASE "+str(c)+" passed")
            else:
                f+=1
                print("--CASE"+str(c)+" failed")
            c+=1
            rate = 0
            if(f==0):
                rate = 100
            else:
                rate = p/f*100

    print("TOTAL PASSED:"+str(p)+" TOTAL FAILED:"+str(f)+ " %RATE: " + str(rate))

#Run file after you complete the steps explained in the my_code function's description. Since this
#function uses markov chains, you can arrange test numbers as you wish but it can spin up your fans if you pass big
#numbers.I hope that you can use it
run_tests(60)