#In refactoring, first change is done
#In refactoring, second change is done
import time
import pandas as pd

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
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities=['chicago','new york city','washington']
    city=input("\nEnter a city - ie: chicago , new york or washington\n")
    while city.lower() not in cities:
        main()
    
     
        

    # TO DO: get user input for month (all, january, february, ... , june)
    months_choice = ['all','january','february','march','april','may','june']
    month=input("\nWhich month will you analyze? -ie: all , january, february,...june\n")
    while month.lower() not in months_choice:
        month=input("\nWhich month will you analyze? -ie: all , january, february,...june\n")
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days_choice=['all','monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']
    day=input("\nWhich day will you analyze? - ie:all , monday, tuesday...,sunday\n")
    
    while day.lower() not in days_choice:
        day=input("\nWhich day will you analyze? - ie:all , monday, tuesday...,sunday\n")

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

    df = pd.read_csv('./'+CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday
    months_value={'january':1, 'february':2, 'march':3, 'april':4, 'may':5,'june':6, 'july':7}
    days_value={'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6 }
    
    if month != 'all':
        df=df[df['month']==months_value[month]]
        
    if day != 'all' :
        df=df[df['day']==days_value[day]]

        
    
    print(df)
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    months={1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july'}
    print('Most Popular Start Month:', months[popular_month])

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    popular_day = df['day'].mode()[0]
    days={0:'monday', 1:'tuesday', 2:'wednesday', 3:'thursday', 4:'friday', 5:'saturday', 6:'sunday'}
    print('Most Popular Start Day:', days[popular_day])

    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station: ', popular_start_station+"\n")

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station: ', popular_end_station+"\n")

    # TO DO: display most frequent combination of start station and end station trip
    all_combinations = df['Start Station']+' - '+df['End Station']
    popular_combination = all_combinations.mode()[0]
    print('Most Popular Combination: ', popular_combination+"\n")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df['Trip Duration']
    total_travel_time=travel_time.sum()
    
    print("\nTotal travel time: %s" %total_travel_time+" seconds\n")

    # TO DO: display mean travel time
    mean_of_travel_time=travel_time.mean()
    
    print("\nMean of travel time: %s" % mean_of_travel_time+" seconds\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types=df['User Type']
    unique_types=user_types.unique()
    length=len(unique_types)
    
    i=0
    while i<length:
            print('Count of '+unique_types[i]+': %s'%user_types[user_types==unique_types[i]].count())
            i+=1

    # TO DO: Display counts of gender
    if 'Gender' in list(df.columns):
        gender=df['Gender']
        print('\nCount of male %s'%gender[gender=='Male'].count())
        print('Count of female %s\n'%gender[gender=='Female'].count())
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Gender' in list(df.columns):
        birth_year=df['Birth Year']
        unique_birth=birth_year.unique()
        sorted_unique_birth=sorted(unique_birth)
        print('Earliest year of birth: %s'%sorted_unique_birth[0])
        print('Most recent year of birth: %s'%sorted_unique_birth[-1])
        print('Most common year of birth: %s'%birth_year.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
        while True:
            try:
                raw_number=int(input('Please enter raw data :'))
                break            
            except:
                print("That's not a valid option!")
           
            
        while raw_number >= len(df) or raw_number <= 0:
                   
            while True:
                try:
                    raw_number=int(input('Please enter invalid raw data between 1-%s : '%len(df)))
                    break
                except:
                    print("That's not a valid option!")
            
        
        df=df.drop(columns=['month','day'])
        print(df.iloc[raw_number+1])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        #Display_data
        display = input('\nWould you like to view an individual data? Enter yes or no.\n')
        
        while display.lower() != 'no':
            if(display.lower()=='yes'):
               
                display_data(df)
               
            display = input('\nWould you like to view an individual data? Enter yes or no.\n')
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
