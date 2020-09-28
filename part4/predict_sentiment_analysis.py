from nltk.corpus import stopwords
from string import punctuation
from nltk import SnowballStemmer, FreqDist
from nltk.tokenize import word_tokenize
import json
from nltk import download
import nltk
import pickle
import sys

nltk.data.path.append("/tmp")
nltk.download("punkt", download_dir = "/tmp")
download('stopwords',download_dir = "/tmp")

stemmer = SnowballStemmer("english")
stopwords_eng = stopwords.words('english')

def extract_features(words):
    return [stemmer.stem(w.lower()) for w in words if w not in stopwords_eng and w not in punctuation]

def bag_of_words(words):
    all_words = FreqDist(words)
    word_features = list(all_words)[:2000] #2000 most frequent words
    bag = {}
    for w in word_features:
        bag[w] = w in set(words)
    return bag

#Load Model
model_file = open('sa_classifier.pickle', 'rb')
model = pickle.load(model_file)
model_file.close()

def get_sentiment(review):
    words = word_tokenize(review)
    words = extract_features(words)
    words = bag_of_words(words)
    return model.classify(words)
""" 
print('Loading function')
def lambda_handler(event, context):
    #print('Received event: ' +
        #json.dumps(event, indent=2))
    if 'review' in event["queryStringParameters"]:
        review = event["queryStringParameters"]['review']
        print(f"Got review: {review}")
        try:
            sentiment = get_sentiment(review)
            print(f"Sentiment: {sentiment}")
        except Exception as e:
            print(e)
        
        return { 'statusCode': 200, 'body':  json.dumps({"sentiment" : str(sentiment)}) }
    else:
        print("ERROR: review field not found!")
        return { 'statusCode': 400, 'body': json.dumps(event) } """

# Test code
#if __name__ == '__main__':
#    lambda_handler(sys.argv[1],None)