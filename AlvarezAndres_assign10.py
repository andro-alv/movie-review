"""
AlvarezAndres_assign10.py
Written by: Andres Alvarez
Worked with: Cindy Mata and Renaldo Hyacinthe
December 8 2019
Section: CSCI-UA.002-003
"""
#import needed modules
import time
# setting up dictionary called words
words = {}
# open the movie review file and split the lines
#start time
openfile = open("movie_reviews.txt","r")
alldata = openfile.read()
# split the string on \n
data_split = alldata.split("\n")
# have a review count
review_count = 0
start_time = time.time()
# for loop to check each review in the document 
for review in data_split:
    # split the review on " " so the program examines every word
    review_split = review.split(" ")
    # if the review is a blank like the program will skip the line
    if review == "":
        continue
    # add 1 to the review count
    review_count +=1
    # for loop to check each word in the review
    for review_word in review_split:
        # this converts the word into all lower case
        review_word = review_word.lower()
        # if the review word is not in the words dict
        if review_word not in words:
            # if the review word is a "" or "'s" the program will skip it
            if review_word == "" or review_word == "'s":
                continue
            # else it will add it to the words dictionary as a key
            # the value assigned to the key will be the score of the review and 1 since it is the first time seeing the word 
            else: 
                words[review_word] = [int(review[0]),int(1)]
        # if the review word is in the key
        elif review_word in words:
            # it adds the new corresponding score to the existing score
            words[review_word][0]+= int(review[0])
            # and it adds 1
            words[review_word][1] += 1
# end the timer
end_time = time.time()
# calculate the time spent for the program
duration = end_time - start_time
# count the words in the words dictionary using the len function
unique_words = len(words.keys())


# print statements from assignment
print("Initializing sentiment database.")
print("Sentiment database initialization complete.")
# tell user how many lines the program read
print("Read", review_count,"lines.")
#tell the user how many unique words were analyzed
print("Total unique words analyzed:",unique_words)
# tell user how long the program took to run
print("Analysis took",format(duration, ".3f"),"seconds to complete.")
print()
#keep user in a while loop
while True:
    # ask user to enter a phrase
    phrase = input("Enter a phrase to test: ")
    # if the input is "quit" then end program
    if phrase.lower() == "quit":
        print("Quitting.")
        break
    # if user enters anything else
    else:
        # split the phrase on " " so the program can go through each word in the phrase
        phrase_words = phrase.split(" ")
        # set a counter to 0 for the word averages
        phrase_average_sum = 0
        # set a counter to 0 for the words in the phrase
        word_count = 0
        #for loop to check the words in the phrase
        for word in phrase_words:
            # make the word into lowercases
            word = word.lower()
            #make a for loop to check the characters in the word
            for character in word:
                # check if the charcters are in the alphabet or a number
                # if not
                if character.isalnum() == False:
                    #replace the character with an empty space
                    # this is used to replace any form of punctuation such as "'" or ";" with an empty space to run the word threw the program
                    word = word.replace(character, "")
            #if the word is in the words dictionary
            if word in words:
                # add 1 to the word count
                word_count +=1
                # compute the average score of the the word 
                average = (words[word][0])/(words[word][1])
                # print the number of appearances the word makes and the average score
                print("* '" +word+"' appears", (words[word][1]), "times with an average score of", average)
                # add the average score to the overall sum of the phrase
                phrase_average_sum += average
            else:
                # if the word doesnt appear in the movie review tell the user
                print("* '" +word+ "' does not appear in any movie reviews.")
                
        # if the word count is not 0
        if word_count != 0:
            # compute the average score of the phrase
            phrase_average = (phrase_average_sum/word_count)
            # tell the user the average score of the phrase
            print("The average score for this phrase is:",phrase_average)
            # tell user the phrase average is negative if it is less than 2
            if phrase_average < 2:
                print("This is a NEGATIVE phrase.")
                print()
            # if it is != 2 then tell the user the phrase is positive
            elif phrase_average >= 2:
                print("This is a POSITIVE phrase.")
                print()
        # if word count is 0
        # tell the user there arent enough words to determine a sentiment 
        elif word_count == 0:
            print("Not enough words to determine sentiment.")
            print()
openfile.close()

