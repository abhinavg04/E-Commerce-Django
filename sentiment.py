import pandas as pd
from account.models import Review
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib as plt
import csv
def createCSV(id):
    review = Review.objects.filter(products_id=id)
    with open('review.csv','w',newline='') as revcsv:
        csvwriter = csv.writer(revcsv)
        csvwriter.writerow(["id","review","date","product_id","user_id"])
        for i in review:
            csvwriter.writerow([i.id,i.review,i.date,i.products.id,i.user.id])


def getSentiment():
    df = pd.read_csv('review.csv')
    analyzer = SentimentIntensityAnalyzer()
    res = {}
    for i, row in df.iterrows():
        text = row['review']
        myid = row['user_id']
    res[myid] = analyzer.polarity_scores(text)
    return res










