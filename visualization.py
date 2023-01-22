import seaborn as sns
import matplotlib.pyplot as plt


def visualizeActiveDaysInTheWeek(df):
    sns.countplot(x='dayofweek', data=df, order=[
                  "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    plt.show()


def visualizeActiveHoursInTheDay(df):
    sns.countplot(x='hourofday', data=df)
    plt.show()
