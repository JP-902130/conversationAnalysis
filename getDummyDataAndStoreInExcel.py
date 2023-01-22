"""
Common dummy data generation scripts
"""

from random import randint
from datetime import datetime as dt
from datetime import timedelta
from randomtimestamp import randomtimestamp
import numpy as np
import pandas as pd
import random


def getHeartBeats(numRows):
    data = np.random.normal(80, 10, numRows)
    return data


def getTimeStamps(numRows):
    times = []
    for i in range(numRows):
        times.append(randomtimestamp(2021, 2022))
    times = sorted(times)

    return times


def getPeople(numRows):
    res = []
    for i in range(numRows):
        if randint(0, 1) == 0:
            res.append("Alice")
        else:
            res.append("Bob")
    return res


def getWholeDF(numRows):
    mapNumToDay = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    timeStampData = getTimeStamps(numRows)
    heartBeatData = getHeartBeats(numRows)
    peopleData = getPeople(numRows)
    dict = {'TimeStamp': timeStampData,
            'heartBeatData': heartBeatData,
            'Person': peopleData
            }
    df = pd.DataFrame(dict)
    df['dayofweek'] = df.apply(
        lambda row: mapNumToDay[row['TimeStamp'].dayofweek], axis=1)
    df['hourofday'] = df.apply(lambda row: row['TimeStamp'].hour, axis=1)
    return df
