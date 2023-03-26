import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_city():
    """
    Asks user to specify a city.

    Returns:
        (str) city - name of the city to analyze
    """
    while True:
        city=str(input('Enter the city name (chicago, new york city or washington) \n')).lower()
        if city not in CITY_DATA.keys():
            print('Please enter city name again')
        else:
            break
    return city

def get_month():
    """
    Asks user to specify a month.

    Returns:
        (str) month - the month to analyze
    """
    months=['all','january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month=str(input('Enter the month (all, january, february, march, april, may, june) \n')).lower()
        if month not in months:
            print('Please enter month again')
        else:
            break
    return month

def get_day():
    """
    Asks user to specify a day.

    Returns:
        (str) day - the day to analyze
    """
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day=str(input('Enter the day of week (all, monday, tuesday, wednesday, thursday, friday, saturday sunday) \n')).lower()
        if day not in days:
            print('Please enter day again')
        else:
            break
    return day
    
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
  
    print('-'*40)
    return get_city(), get_month(), get_day()


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
    # convert datetime then extract month and day     
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.strftime('%B').str.lower()
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower()

    
    # filter by month
    if month != 'all':
        df = df[df['month'] == month]

    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    favourite_month = df['month'].mode()[0]
    print('the most common month is:', favourite_month)

    # display the most common day of week
    favourite_day_of_week = df['day_of_week'].mode()[0]
    print('the most common day of week is:', favourite_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    favourite_start_hour = df['hour'].mode()[0]
    print('the most common start hour is:', favourite_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display the most commonly used start station
    favourite_start_station = df['Start Station'].mode()[0]
    print('the most commonly used start station:', favourite_start_station)


    # display the most commonly used end station
    favourite_end_station = df['End Station'].mode()[0]
    print('the most commonly used end station:', favourite_end_station)


    # display the most frequent combination of start station and end station trip
    df['station_combination'] = df['Start Station']+' -> '+df['End Station']
    favourite_station_combination = df['station_combination'].mode()[0]
    print('the most commonly used combination of start station and end station trip:', favourite_station_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time:', total_travel_time)


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types', df['User Type'].value_counts())


    # exclude washington
    if 'Gender' in df:
        # Display counts of gender
        print('counts of gender', df['Gender'].value_counts())
    else:
        print('Gender data is not available for this city.')
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        print('the earliest year of birth:', df['Birth Year'].min())
        
        print('the most recent year of birth:', df['Birth Year'].max())
        
        print('the most common year of birth:', df['Birth Year'].mode()[0])
    else:
        print('Birth Year data is not available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print('Thanks for using our program!')

if __name__ == "__main__":
	main()
