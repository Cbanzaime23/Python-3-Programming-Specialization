import requests
import json
#
# page = requests.get("https://api.datamuse.com/words?rel_rhy=coleen")
# print(type(page))
# print(page.text[:150]) # print the first 150 characters
# print(page.url) # print the url that was fetched
# print("------")
# x = page.json() # turn page.text into a python object
# print(type(x))
# print("---first item in the list---")
# print(x[0])
# print("---the whole list, pretty printed---")
# print(json.dumps(x, indent=3)) # pretty print the results


def get_means_like(word):
    baseurl = "https://api.datamuse.com/words"
    params_diction = {} # Set up an empty dictionary for query parameters
    params_diction["ml"] = word
    params_diction["max"] = "3" # get at most 3 results
    resp = requests.get(baseurl, params=params_diction)
    # return the top three words
    word_ds = resp.json()
    return [d['word'] for d in word_ds]
    return resp.json() # Return a python object (a list of dictionaries in this case)

#print(get_rhymes("funny"))

paragraph = "I'm grateful that God is guiding me in all the challenges that I'm facing"

translated = ""

for word in paragraph.split():
    translated_word = get_means_like(word)
    if translated_word == []:
        #print(word)
        translated = translated + " " + word
    else:
        #print(translated_word[1])
        translated = translated + " " + translated_word[2]

print("Old Word:",paragraph )
print("Translated:", translated)
