
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(str):
    new_str = ""
    for char in str:
        if char not in punctuation_chars:
            new_str = new_str + char
    return new_str


positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_pos(sentence):
    postive = 0
    for word in sentence.split():
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            postive = postive + 1

    return postive

def get_neg(sentence):
    neg = 0
    for word in sentence.split():
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            neg = neg + 1

    return neg


tweet_text = ""
retweet_count = ""
reply_count = ""

tweets = []

cnt = 0

with open("project_twitter_data.csv") as pos_f:
    for lin in pos_f:
        #tweet.append(lin)
        #tweet.append(lin.split(","))
        if cnt == 0:
            cnt = cnt + 1
            continue
        tweet = lin.split(",")
        tweet_text = tweet[0].strip()

        #Number of Retweets
        retweet_count = int(tweet[1].strip())

        #Number of Replies
        reply_count = int(tweet[2].strip())

        #Positive Score
        posScore = get_pos(tweet_text)

        #Negative Score
        negScore = get_neg(tweet_text)

        #Net Score
        netScore = int(posScore) - int(negScore)

        tweets.append( str(retweet_count) + "," + str(reply_count) + "," + str(posScore) + "," + str(negScore)+ "," + str(netScore))
    print(tweets)

with open('resulting_data.csv', 'w') as f:
    f.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score" + "\n")
    for item in tweets:
        f.write("%s\n" % item)
