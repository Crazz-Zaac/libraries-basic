CITY_DATA = {'chicago': 'chicago.csv',
            'new york city': 'new_york_city.csv',
            'washington': 'washington.csv'}

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month 
    and day if applicable.
    """
    
    # loading the file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # converting the Start Time column into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extracting month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #filter by month if applicable
    if month != 'all':
        #use the index of the months list to get the corresponding int 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        #filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    if day != 'all':
        #filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


df = load_data('chicago', 'march', 'friday')
print(df)
    