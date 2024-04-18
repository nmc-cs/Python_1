import pickle
import os
import Tweet

running = True
tweets = []

fileName = "tweets.dat"

if os.path.isfile(fileName):
     with open("tweets.dat", "rb") as fileIn:
          tweets = pickle.load(fileIn)

while(running):
     print('Twitter Menu\n'\
           '1. Create a Tweet \n'\
           '2. View Recent Tweets \n'\
           '3. Search Tweets\n' \
           '4. Quit \n')
     choice = input('What would you like to do? ')
     try:
          value = int(choice)
          if value == 1:
               name = str(input('What is your name? '))
               tweeting = True

               while(tweeting):
                    message = str(input('What would you like to tweet? '))
                    if len(message) < 140:
                         tweet = Tweet.Tweets(name, message)
                         tweets.append(tweet)
                         print(name +", your tweet has been saved.")
                         tweeting = False
                    else:
                         print("Tweets can only be 140 characters!")

          elif value == 2:
               if len(tweets)==0:
                    print("There are no tweets saved")
               else:
                    for i in range(len(tweets)):
                         print(tweets[i].getauthor())
                         print(tweets[i].gettext())
                         print(tweets[i].getage())
          elif value == 3:
               if len(tweets) == 0:
                    print("There are no tweets saved")
               else:
                    found = False
                    searchkey = str(input('What would you like to search for? '))
                    for i in range(len(tweets)-1, 0, -1):
                         if searchkey in tweets[i].gettext():
                               print(tweets[i].getauthor())
                               print(tweets[i].gettext())
                               print(tweets[i].getage())
                               found = True
                    if found == False:
                         print("No tweets contained "+searchkey)

          elif value == 4:
               if len(tweets) > 0:
                    outfile = open('tweets.dat', 'wb')
                    pickle.dump(tweets, outfile)
                    outfile.close()
                    break
     except ValueError:
          print('Please check your input values.')
