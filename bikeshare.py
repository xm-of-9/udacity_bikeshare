# some references used:
# https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/
# https://www.datacamp.com/community/tutorials/pandas-read-csv
# https://www.w3schools.com/python/python_try_except.asp

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\nHello! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    while True:
      city = input("Please select one of the following cities: Chicago, New York City or Washington.").lower()
      if city not in ('chicago', 'new york city', 'washington'):
        print("Invalid entry.")
        continue
      else:
        break

    # get user input for month (all, january, february, ... , june)

    while True:
      month = input("Please select one of the following months: January, February, March, April, May or June. Select 'all' for aggregated data.").lower()
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Invalid entry.")
        continue
      else:
        break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      day = input("Please select one of the following days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday. Select 'all' for aggregated data.").lower()
      if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print("Invalid entry.")
        continue
      else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]
    print('Most Common Month:', popular_month)


    # display the most common day of week

    popular_day = df['day_of_week'].mode()[0]
    print('Most Common day:', popular_day)


    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most commonly used start station:', Start_Station)


    # display most commonly used end station

    End_Station = df['End Station'].value_counts().idxmax()
    print('Most commonly used end station:', End_Station)


    # display most frequent combination of start station and end station trip

    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('Most Commonly used combination:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total travel time:', Total_Travel_Time/86400, " Days")

    # display mean travel time

    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean travel time:', Mean_Travel_Time/60, " Minutes")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('User Types:', user_types)

    # Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print('Gender Types:', gender_types)
    except KeyError:
      print("No data available for this month.")

    # Display earliest, most recent, and most common year of birth

    try:
      Earliest_Year = df['Birth Year'].min()
      print('Earliest Year:', Earliest_Year)
    except KeyError:
      print("No data available for this month.")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print('Most Recent Year:', Most_Recent_Year)
    except KeyError:
      print("No data available for this month.")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print('Most Common Year:', Most_Common_Year)
    except KeyError:
      print("No data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    display_data = input('Display five lines of raw data? Select yes or no.').lower()
    print()
    if display_data=='yes':
        display_data=True
    elif display_data=='no':
        display_data=False
   
    if display_data:
        while 1:
            for i in range(5):
                print(df.iloc[i])
                print()
            display_data = input('Display additional fives lines of raw data? Select yes or no.').lower()
            if display_data=='yes':
                continue
            elif display_data=='no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
   
         
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()