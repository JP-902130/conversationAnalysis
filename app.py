import visualization
import numpy as np
from selenium import webdriver
import getDummyDataAndStoreInExcel
from random import randint
import pandas as pd
import sys
import statistics
from datetime import datetime
import sentimentAnalysis

import os
from dotenv import load_dotenv, find_dotenv

sys.setrecursionlimit(1500)


def main():
    load_dotenv(find_dotenv())
    print(os.environ.get("PRIVATE_KEY"))

    df = getDummyDataAndStoreInExcel.getWholeDF(1000)
    df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
    # visualization.visualizeActiveHoursInTheDay(df)
    print(sentimentAnalysis.happyIndex("fuck!"))


main()
