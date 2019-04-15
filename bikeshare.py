import time as t
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'nyc': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    print ('Hello! Let\'s explore major US bikeshare data!')
    print ('')
    t.sleep(1)
    while True:
        print ("Which city do you want to explore its bikeshare data?\n")
        answer = input("Chicago, NYC or Washington?\n").lower()
        print ('')
        if answer not in ("chicago", "nyc", "washington"):
            print("\nInvalid answer\n") 
            continue
        else:
            break
        
    print("\nNow how do you want to filter your data?\n")
    
    data_filter = input("Month, day, both, or none?\n")
    
    while True:
        if data_filter not in ("month", "day", "both", "none"):
            print("\nInvalid answer\n")
            continue
        elif data_filter == "month":
            print("Which month do you want to explore? - please type in first three letters of month all in lowercase\n")
            month = input("Jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec or all?\n").lower()
            day = 'all'
            while True:
                if month not in ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "all"):
                    print("\nInvalid answer\n")
                    continue
                else:
                    break
            break
        elif data_filter == "day":
            print("Which day do you want to explore? - please type in first three letters of day all in lowercase\n")
            day = input("Mon, tue, wed, thu, fri, sat, sun or all?\n").lower()
            month = 'all'
            while True:
                if day not in ("mon", "tue", "wed", "thu", "fri", "sat", "sun", "all"):
                    print("\nInvalid answer\n")
                    continue
                else:
                    break
            break
        elif data_filter == "both":
            print("Which month do you want to explore? - please type in first three letters of month all in lowercase\n")
            month = input("Jan, feb, mar, apr, may, jun, july, aug, sep, oct, nov, dec or all?\n").lower()
            while True:
                if month not in ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "all"):
                    print("\nInvalid answer\n")
                    continue
                else:
                    break
            print("Now which day do you want to explore? - please type in first three letters of day all in lowercase\n")
            day = input("Mon, tue, wed, thu, fri, sat, sun or all?\n").lower()
            while True:
                if day not in ("mon", "tue", "wed", "thu", "fri", "sat", "sun", "all"):
                    print("\nInvalid answer\n")
                    continue
                else:
                    break 
                    
        elif data_filter == "none":
            month = 'all'
            day = 'all'

    return city, month, day

def load_data(city, month, day):
    
    df = pd.read_csv(CITY_DATA['chicago'])
    df = pd.read_csv(CITY_DATA['nyc'])
    df = pd.read_csv(CITY_DATA['washington'])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'aug', 'sep', 'oct', 'nov', 'dec']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day]
        
    return df

def time_stats(df):
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['time'] = df['Start Time'].dt.time
    common_time = df['time'].mode()[0]
  
    print('\nCalculating The Most Frequent Times of Travel...\n')
    print('')

    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]

    print('Most Common Month:', common_month)
    print('')
    
    df['week'] = df['Start Time'].dt.week
    common_week = df['week'].mode()[0]

    print('Most Common day of week:', common_week)
    print('')

    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:', common_hour)
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
          
def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    print('')
    start_time = time.time()

    df['Station'] = pd.to_string(df['Station'])

    df['start'] = df['Station'].dt.start
    common_start_station = df['start'].mode()[0]

    print('Most Common Start Station:', common_start_station)
    print('')

    df['end'] = df['Station'].dt.start
    common_end_station = df['end'].mode()[0]

    print('Most Common End Station:', common_end_station)
    print('')

    df['combo'] = df['Start Station'] + ' to ' + df['End Station'] 
    common_station_combo = df['combo'].mode().loc[0]

    print('Most common Combination:', common_station_combo)
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['total'] = df['Start Time'] + df['End Time']
    total_travel_time = df['total'].mode()[0]

    print('Total Travel Time:', total_travel_time)
    print('')

    df['average'] = df['total']
    average = np.mean(df['total']).mode()[0]

    print('Mean/Average Travel Time:', average)
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    df['user_stats'] = pd.to_numeric(df['user_stats'])

    df['user_types'] = df['user_stats'].dt.user_types
    user_types = df['user_types'].value_counts()

    print('Counts of user types:', user_types)
    print('')
    
    df['gender'] = df['user_stats'].dt.gender
    gender = df['gender'].value_counts()

    print('Counts of gender:', gender)
    print('')

    df['earliest_birth_year'] = df['Birth_Year'].dt.earliest_birth_year
    earliest_birth_year = df['Birth_Year'].min()

    print('Earliest Birth Year:', earliest_birth_year)
    print('')

    df['recent_birth_year'] = df['Birth_Year'].dt.recent_birth_year
    recent_birth_year = df['Birth Year'].max()

    print('Recent Birth Year:', recent_birth_year)
    print('')

    df['common_birth_year'] = df['Birth_Year'].dt.common_birth_year
    common_birth_year = df['Birth Year'].mode()[0]

    print('Most Popular Birth Year:', common_birth_year)
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def main():
    city = ""
    month = 0
    day = 0
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
	main()
