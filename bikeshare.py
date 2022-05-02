import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def load_data(): 
    user_city_input = input('Hello and welcome! You have data for Chicago, New York City and Washington at your disposal. Please enter the name of the city you want to view: ')
    user_city_input = user_city_input.lower()
    while user_city_input not in city_data: 
        user_city_input = input('Please enter a correct spelling of the city you want data on. Thank you. ').lower()

    """
    ************************************************
        LOAD dATA
    ************************************************
    """

    df = pd.read_csv(city_data[user_city_input])

    df['Start Time'] = pd.to_datetime(df['Start Time'])     
    df['Year'] = df['Start Time'].dt.year
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()    
    df['Hour'] = df['Start Time'].dt.hour
    df.drop('Unnamed: 0', inplace = True, axis = 1)
    

    """
    ************************************************
        FILTER INPUT
    ************************************************
    """
    filter_input = input('Would you like to view {} data by month, day, all or none?: \n'.format(user_city_input)).lower()
    filter_response = ['none', 'day', 'month', 'all']
    possible_raw_data_resonse = ['y', 'n']
    possible_start_over_resonse = ['y', 'n']
    month_response = df['Month'].unique()
    day_response = df['Day'].unique()
    while filter_input not in filter_response: 
        filter_input = input('Please enter a valid response from the options above. Thank you. ').lower()

    """
    ************************************************
        NO FILTER
    ************************************************
    """

    if filter_input == 'none': 
        def none(df):
            def time_stats(df): 
                print('Okay then! Lets explore {} city data!\n.'.format(user_city_input))
                print('AS IT PARTAINS TO THE TIMES OF TRAVEL')
            #       ***Computing for Hour
                def common_hour(df):
                    print('***Computing the most common hour of day in a 24hr clock...')
                    start_time = time.time()
                    common_hour = df['Hour'].mode()[0]
                    common_hour_count = df['Hour'].value_counts().max()
                    print('The most common hour of the day in {} is: {}.00\nWith a total count of {} in the start time\n'.format(user_city_input, common_hour, common_hour_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                common_hour(df)
            #      ***Computing for Day
                def common_day(df):
                    print('***Computing the most common day of the week in {}...'.format(user_city_input))
                    start_time = time.time()
                    common_weekday = df['Day'].mode()[0]
                    common_weekday_count = df['Day'].value_counts().max()
                    print('The most common day of the week in {} is: {}\nWith a total count of {}\n'.format(user_city_input, common_weekday, common_weekday_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                common_day(df)
                #       ***Computing for Month
                def common_month(df):
                    print('***Computing the most common month in {}...'.format(user_city_input))
                    start_time = time.time()
                    common_month = df['Month'].mode()[0]
                    common_month_count = df['Month'].value_counts()[0]
                    print('The most common month in {} is: {}\nWith a total count of {}\n'.format(user_city_input, common_month, common_month_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                common_month(df)
            time_stats(df)

            def station_stats(df): 
            #         ***Computing for Start Stations
                print('\nAS IT PARTAINS TO STATIONS AND TRIPS')
                #       ***Computing common Start Stations
                def common_start_station(df):
                    print('***Computing the most common start station...')
                    start_time = time.time()
                    common_start_station = df['Start Station'].mode()[0]
                    common_start_station_count = df['Start Station'].value_counts().max()
                    print('The most common start station in {} is: {}\nWith a total count of {}\n'.format(user_city_input, common_start_station, common_start_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                common_start_station(df)
                #       ***Computing common End Stations
                def common_end_station(df):
                    print('***Computing the most common end station...')
                    start_time = time.time()
                    common_end_station = df['End Station'].mode()[0]
                    common_end_station_count = df['End Station'].value_counts().max()
                    common_end_station_count
                    print('The most common end station in {} is: {}\nWith a total count of {}\n'.format(user_city_input, common_end_station, common_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                common_end_station(df)
                #       ***Computing common Start and End Stations
                def start_and_end_station(df):
                    print('***Computing the most common trip from start to end. That is the most frequent combination of start and end stations...\n')
                    start_time = time.time()
                    most_common_startandend_station = df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
                    start_and_end_count = df.groupby(['Start Station'])['End Station'].value_counts().max()
                    print('The most common start and end stations in {} are:\n{}\nWith a total of {} trips'.format(user_city_input, most_common_startandend_station, start_and_end_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                start_and_end_station(df)
            station_stats(df)

        #       ***Computing for Travel Time
            def trip_duration(df): 
                print('AS IT PARTAINS TO TRIP DURATIONS')
                print('***Computing the total travel time...')
                start_time = time.time()
                total_travel_time = df['Trip Duration'].sum()
                total_travel_time_average = int(df['Trip Duration'].mean())
                print('The total travel time in {} is: {} hours\nWith an average of {}\n hours'.format(user_city_input, total_travel_time, total_travel_time_average))
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            trip_duration(df)

        #         ***Computing User Info  
            def number_of_users(df): 

                print('AS IT PARTAINS TO USER INFORMATION')
                print('***Computing the total number for each type of user...')
                start_time = time.time()
                user_type_count = df['User Type'].value_counts()
                print(user_type_count)
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            number_of_users(df)
            #       ***Computing gender and birth year for only new york city and chicago
            #       ***For Gender
            def gender_number(df):
                for column in df: 
                    if 'Gender' in df: 
                        print('\n***Computing the total number for each gender...')
                        start_time = time.time()
                        gender_type_count = df['Gender'].value_counts()
                        print('{}\n'.format(gender_type_count))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            gender_number(df)

            #       ***For Birth Year
            #       ***Most frequent birth year
            def frequent_birth_year(df):
                for column in df:
                    if 'Birth Year' in df: 
                        print('***Computing the most frequent birth year and the most recent birthyear')
                        print('For the most frequent birth year..')
                        start_time = time.time()
                        most_frequent_birthyear = int(df['Birth Year'].mode())
                        print('The most frequent bith year in {} is: {}\n'.format(user_city_input, most_frequent_birthyear))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break 
                    else: 
                        pass
            frequent_birth_year(df)
            #       ***Most recent birth year
            def recent_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the most recent birth year..')
                        start_time = time.time()
                        most_recent_birthyear = int(df['Birth Year'].max())
                        print('The most recent birth year in {} is {}\n'.format(user_city_input, most_recent_birthyear))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            recent_birth_year(df)
            
#      ***Earliest birth year
            def earliest_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the earliest birth year..')
                        start_time = time.time()
                        earliest_birthyear = int(df['Birth Year'].min())
                        print('The earliest birth year in {} is {}\n'.format(user_city_input, earliest_birthyear))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            earliest_birth_year(df)
            
#             Starting the program again 
            def explore_over_again():
                raw_data = input('Would you like to see some raw data? Please respond with a "y" or "no": ').lower()
                while raw_data not in possible_raw_data_resonse: 
                    raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                count = 0
                while raw_data == 'y': 
                    count += 5
                    show_raw_data = df.head(count)
                    show_raw_data
                    print(show_raw_data)
                    if count == len(df.index): 
                            print('There is no more data to show')
                    else: 
                        raw_data = input('Do you want to see some more?: y or n: ').lower()
                        while raw_data not in possible_raw_data_resonse: 
                            raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                start_over = input('Do you want to explore bikeshare data again? y or n: ').lower()
                while start_over not in possible_start_over_resonse: 
                    start_over = input('Please enter a correct response from above. Thank you. ').lower()
                if start_over == 'y': 
                    load_data()
                else: 
                    print('Thank you for exploring the bikeshare data.\n')
            explore_over_again()
        none(df)
    """
    ************************************************
        FILTER BY CITY AND MONTH
    ************************************************
    """ 
    if filter_input == 'month':
        def get_month_data(df):
            user_month = input('what month would you want to view?: ')
            user_month = user_month.capitalize()
            while user_month not in month_response: 
                user_month = input('Please enter a correct spelling of the month you want data on. Thank you. ').capitalize()
                
    #           Load month data
            month = df.groupby(['Month'])
            month_data = month.get_group(user_month)

            print('Okay then! Lets explore the data with your chosen filters!\n.')
            
            print('AS IT PARTAINS TO THE TIMES OF TRAVEL')
            print('Okay then! Lets explore the data with your chosen filters!\n.')
            print('AS IT PARTAINS TO THE TIMES OF TRAVEL')
    #       ***Computing for Hour
            def month_time_stats(df): 
                def month_common_hour(df):
                    print('***Computing the most common hour of day in a 24hr clock...')
                    start_time = time.time() 
                    month_hour= df['Month'] == user_month
                    common_month_hour = df.loc[month_hour]['Hour'].value_counts().idxmax()
        #             Calculating hour count per month
                    month_hour_count= df['Month'] == user_month
                    common_month_hour_count = df.loc[month_hour_count]['Hour'].value_counts().max()
                    print('The most common hour in {} is: {}.00\nWith a total count of {} hours in the start time\n'.format(user_month, common_month_hour, common_month_hour_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                month_common_hour(df)

        #      ***Computing for Day
                def month_common_day(df):
                    print('***Computing the most common day of the week...')
                    start_time = time.time()
                    month_day= df['Month'] == user_month
                    month_common_day = df.loc[month_day]['Day'].value_counts().idxmax()
        #             Calculating day count per month
                    month_day_count= df['Month'] == user_month
                    month_common_day_count = df.loc[month_day_count]['Day'].value_counts().max()
                    print('The most common day of the week in {} is: {}\nWith a total count of {}\n'.format(user_month, month_common_day, month_common_day_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                month_common_day(df)
            month_time_stats(df)
        

    #         ***Computing for Start Stations
            def month_station_stats(df): 
                print('\nAS IT PARTAINS TO STATIONS AND TRIPS')
                #       ***Computing common Start Station
                def month_common_start_station(df):
                    print('***Computing the most common start station...')
                    start_time = time.time()
                    month_start_station= df['Month'] == user_month
                    month_common_start_station = df.loc[month_start_station]['Start Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    month_start_station_count= df['Month'] == user_month
                    month_common_start_station_count = df.loc[month_start_station_count]['Start Station'].value_counts().max()
                    print('The most common start station in {} is: {}\nWith a total count of {}\n'.format(user_month, month_common_start_station, month_common_start_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                month_common_start_station(df)
        #       ***Computing common End Stations
                def month_common_end_station(df):
                    print('***Computing the most common end station...')
                    start_time = time.time()
                    month_end_station= df['Month'] == user_month
                    month_common_end_station = df.loc[month_end_station]['End Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    month_end_station_count= df['Month'] == user_month
                    month_common_end_station_count = df.loc[month_end_station_count]['End Station'].value_counts().max()            
                    print('The most common end station in {} is: {}\nWith a total count of {}\n'.format(user_month, month_common_end_station, month_common_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                month_common_end_station(df)

        #       ***Computing for Start and End Stations
                def month_start_and_end_station(df):
                    print('***Computing the most common trip from start to end. That is the most frequent combination of start and end stations...\n')
                    start_time = time.time()
                    start_end_station= df['Month'] == user_month
                    month_common_start_end_station = df.loc[start_end_station][['Start Station', 'End Station']].value_counts().idxmax()
        #             Calculating start and end station count per month
                    start_end_station= df['Month'] == user_month
                    month_common_start_end_station_count = df.loc[start_end_station][['Start Station', 'End Station']].value_counts().max()
                    print('The most common start and end stations in  {} is {}\nWith a total count of {}\n'.format(user_month, month_common_start_end_station, month_common_start_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                month_start_and_end_station(df)
            month_station_stats(df)

            #       ***Computing for Travel Time
            def month_trip_duration(df): 
                print('AS IT PARTAINS TO TRIP DURATIONS')
                print('***Computing the total travel time...')
                start_time = time.time()
                month_travel = df['Month'] == user_month
                month_total_travel_time =  df.groupby([month_travel])['Trip Duration'].sum()[True]
                month_total_travel_time_average = int(df.groupby([month_travel])['Trip Duration'].mean()[True])
                print('The total travel time is {}\nWith an average of {}'.format(month_total_travel_time, month_total_travel_time_average))
        #             print('The total travel time in {} is: {} hours\nWith an average of {} hours'.format(user_month, month_total_travel_time, month_total_travel_time_average))
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            month_trip_duration(df)

        #         ***Computing User Info  
            def month_number_of_users(df): 
                print('AS IT PARTAINS TO USER INFORMATION')
                print('***Computing the total number for each type of user...')
                start_time = time.time()
                month_user = df['Month'] == user_month
                month_user_info =  df.groupby([month_user])['User Type'].value_counts()[True]
                print(month_user_info)
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            month_number_of_users(df)

        #       ***Computing gender and birth year for only new york city and chicago
        #       ***For Gender
            def month_gender_number(df):
                for column in df: 
                    if 'Gender' in df: 
                        print('***Computing the total number for each gender...')
                        start_time = time.time()
                        month_gender_num = df['Month'] == user_month
                        gender_type_count = df.groupby([month_gender_num])['Gender'].value_counts()[True]
                        print('{}\n'.format(gender_type_count))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            month_gender_number(df)

        #       ***For Birth Year
        #       ***Most frequent birth year
            def month_frequent_birth_year(df):
                for column in df:
                    if 'Birth Year' in df: 
                        print('***Computing the most frequent birth year and the most recent birthyear')
                        print('For the most frequent birth year..')
                        start_time = time.time()
                        month_birth_year = df['Month'] == user_month
                        month_frequent_birth_year = df.groupby([month_birth_year])['Birth Year'].value_counts().idxmax()[True]
                        month_frequent_birth_year = int(month_frequent_birth_year)
                        month_frequent_birth_year = int(month_frequent_birth_year)
                        print('The most frequent bith year in {} is: {}\n'.format(user_month, month_frequent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break 
                    else: 
                        pass
            month_frequent_birth_year(df)

        #       ***Most recent birth year
            def month_recent_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the most recent birth year..')
                        start_time = time.time()
                        month_birth_year = df['Month'] == user_month
                        month_recent_birth_year = df.groupby([month_birth_year])['Birth Year'].max()[True]
                        month_recent_birth_year = int(month_recent_birth_year)
                        print('The most recent birth year is {}\n'.format(month_recent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            month_recent_birth_year(df)
        #    ***Earliest birth year  
            def month_earliest_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the earliest birth year..')
                        start_time = time.time()
                        month_birth_year = df['Month'] == user_month
                        month_earliest_birth_year = df.groupby([month_birth_year])['Birth Year'].min()[True]
                        month_earliest_birth_year = int(month_earliest_birth_year)
                        print('The earliest birth year is {}\n'.format(month_earliest_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            month_earliest_birth_year(df)
        #             Starting the program again
            def explore_over_again():
                    raw_data = input('Would you like to see some raw data? Please respond with a "y" or "n": ').lower()
                    while raw_data not in possible_raw_data_resonse: 
                        raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    count = 0
                    while raw_data == 'y': 
                        count += 5
                        show_raw_data = month_data.head(count)
                        show_raw_data
                        print(show_raw_data)
                        if count == len(month_data.index): 
                            print('There is no more data to show')
                        else: 
                            raw_data = input('Do you want to see some more?: y or n: ').lower()
                            while raw_data not in possible_raw_data_resonse: 
                                raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    start_over = input('Do you want to explore bikeshare data again? y or n: ').lower()
                    while start_over not in possible_start_over_resonse: 
                            start_over = input('Please enter a correct response from above. Thank you. ').lower()
                    if start_over == 'y': 
                        load_data()
                    else: 
                        print('Thank you for exploring the bikeshare data.\n')
            explore_over_again()
        get_month_data(df)


    """
    ************************************************
        FILTER BY CITY AND DAY
    ************************************************
    """  

    if filter_input == 'day':
        user_day = input('what day would you want to view?: ')
        user_day = user_day.capitalize()
        while user_day not in day_response: 
            user_month = input('Please enter a correct spelling of the day you want data on. Thank you. ').capitalize()

    #   Retrieving data by month 
        def get_day_data(df): 
            day = df.groupby(['Day'])
            day_data = day.get_group(user_day)

            print('Okay then! Lets explore the data with your chosen filters!\n.')
            print('AS IT PARTAINS TO THE TIMES OF TRAVEL')
    #       ***Computing for Hour
            def day_time_stats(df): 
                def day_common_hour(df):
                    print('***Computing the most common hour of day in a 24hr clock...')
                    start_time = time.time() 
                    day_hour= df['Day'] == user_day
                    common_day_hour = df.loc[day_hour]['Hour'].value_counts().idxmax()
        #             Calculating hour count per month
                    day_hour_count= df['Day'] == user_day
                    common_day_hour_count = df.loc[day_hour_count]['Hour'].value_counts().max()
                    print('The most common hour in {} is: {}.00\nWith a total count of {} hours in the start time\n'.format(user_day, common_day_hour, common_day_hour_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                day_common_hour(df)

        #      ***Computing for Day
                def day_common_month(df):
                    print('***Computing the most common month')
                    start_time = time.time()
                    day_month= df['Day'] == user_day
                    day_common_month = df.loc[day_month]['Month'].value_counts().idxmax()
        #             Calculating day count per month
                    day_month_count= df['Day'] == user_day
                    day_common_month_count = df.loc[day_month_count]['Month'].value_counts().max()
                    print('The most common month on {} is: {}\nWith a total count of {}\n'.format(user_day, day_common_month, day_common_month_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                day_common_month(df)
            day_time_stats(df)
        

        #         ***Computing for Start Stations
            def day_station_stats(df): 
                print('\nAS IT PARTAINS TO STATIONS AND TRIPS')
                #       ***Computing common Start Station
                def day_common_start_station(df):
                    print('***Computing the most common start station...')
                    start_time = time.time()
                    day_start_station= df['Day'] == user_day
                    day_common_start_station = df.loc[day_start_station]['Start Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    day_start_station_count= df['Day'] == user_day
                    day_common_start_station_count = df.loc[day_start_station_count]['Start Station'].value_counts().max()
                    print('The most common start station on {} is: {}\nWith a total count of {}\n'.format(user_day, day_common_start_station, day_common_start_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                day_common_start_station(df)
        #       ***Computing common End Stations
                def day_common_end_station(df):
                    print('***Computing the most common start station...')
                    start_time = time.time()
                    day_end_station= df['Day'] == user_day
                    day_common_end_station = df.loc[day_end_station]['End Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    day_end_station_count= df['Day'] == user_day
                    day_common_end_station_count = df.loc[day_end_station_count]['End Station'].value_counts().max()
                    print('The most common end station on {} is: {}\nWith a total count of {}\n'.format(user_day, day_common_end_station, day_common_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                day_common_end_station(df)

        #       ***Computing for Start and End Stations
                def day_start_and_end_station(df):
                    print('***Computing the most common trip from start to end. That is the most frequent combination of start and end stations...\n')
                    start_time = time.time()
                    start_end_station_day= df['Day'] == user_day
                    day_common_start_end_station = df.loc[start_end_station_day][['Start Station', 'End Station']].value_counts().idxmax()
        #             Calculating start and end station count per month
                    start_end_station_day= df['Day'] == user_day
                    day_common_start_end_station_count = df.loc[start_end_station_day][['Start Station', 'End Station']].value_counts().max()
                    print('The most common start and end stations on  {} is {}\nWith a total count of {}\n'.format(user_day, day_common_start_end_station, day_common_start_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                day_start_and_end_station(df)
            day_station_stats(df)

            #       ***Computing for Travel Time
            def day_trip_duration(df): 
                print('AS IT PARTAINS TO TRIP DURATIONS')
                print('***Computing the total travel time...')
                start_time = time.time()
                day_travel = df['Day'] == user_day
                day_total_travel_time =  df.groupby([day_travel])['Trip Duration'].sum()[True]
                day_total_travel_time_average = int(df.groupby([day_travel])['Trip Duration'].mean()[True])
                print('The total travel time is {}\nWith an average of {}'.format(day_total_travel_time, day_total_travel_time_average))
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            day_trip_duration(df)

        #         ***Computing User Info  
            def day_number_of_users(df): 
                print('AS IT PARTAINS TO USER INFORMATION')
                print('***Computing the total number for each type of user...')
                start_time = time.time()
                day_user = df['Day'] == user_day
                day_user_info =  df.groupby([day_user])['User Type'].value_counts()[True]
                print(day_user_info)
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            day_number_of_users(df)

        #       ***Computing gender and birth year for only new york city and chicago
        #       ***For Gender
            def day_gender_number(df):
                for column in df: 
                    if 'Gender' in df: 
                        print('***Computing the total number for each gender...')
                        start_time = time.time()
                        day_gender_type = df['Day'] == user_day
                        gender_type_count = df.groupby([day_gender_type])['Gender'].value_counts()[True]
                        print('{}\n'.format(gender_type_count))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            day_gender_number(df)

        #       ***For Birth Year
        #       ***Most frequent birth year
            def day_frequent_birth_year(df):
                for column in df:
                    if 'Birth Year' in df: 
                        print('***Computing the most frequent birth year and the most recent birthyear')
                        print('For the most frequent birth year..')
                        start_time = time.time()
                        day_birth_year = df['Day'] == user_day
                        day_frequent_birth_year = df.groupby([day_birth_year])['Birth Year'].value_counts().idxmax()[True]
                        day_frequent_birth_year = int(day_frequent_birth_year)
                        print('The most frequent birth year on {} is: {}\n'.format(user_day, day_frequent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break 
                    else: 
                        pass
            day_frequent_birth_year(df)

        #       ***Most recent birth year
            def day_recent_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the most recent birth year..')
                        start_time = time.time()
                        day_birth_year = df['Day'] == user_day
                        day_recent_birth_year = int(df.groupby([day_birth_year])['Birth Year'].max()[True])
                        print('The most recent birth year is {}\n'.format(day_recent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            day_recent_birth_year(df)
        #        ***Earliest birth year
            def day_earliest_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the earliest birth year..')
                        start_time = time.time()
                        day_birth_year = df['Day'] == user_day
                        day_earliest_birth_year = int(df.groupby([day_birth_year])['Birth Year'].min()[True])
                        print('The earliest birth year is {}\n'.format(day_earliest_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            day_earliest_birth_year(df)
        #        ***Starting the program again
            def explore_over_again():
                    raw_data = input('Would you like to see some raw data? Please respond with a "y" or "no": ').lower()
                    while raw_data not in possible_raw_data_resonse: 
                        raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    count = 0
                    while raw_data == 'y': 
                        count += 5
                        show_raw_data = day_data.head(count)
                        show_raw_data
                        print(show_raw_data)
                        if count == len(day_data.index): 
                            print('There is no more data to show')
                        else: 
                            raw_data = input('Do you want to see some more?: y or n: ').lower()
                            while raw_data not in possible_raw_data_resonse: 
                                raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    start_over = input('Do you want to explore bikeshare data again? y or n: ').lower()
                    while start_over not in possible_start_over_resonse: 
                        start_over = input('Please enter a correct response from above. Thank you. ').lower()
                    if start_over == 'y': 
                        load_data()
                    else: 
                        print('Thank you for exploring the bikeshare data.\n')
            explore_over_again()
        get_day_data(df)


    """
    ************************************************
        FILTER BY CITY, MONTH, AND DAY
    ************************************************
    """

    if filter_input == 'all':
        user_all_month = input('what month would you want to view?: ').lower()
        user_all_month = user_all_month.capitalize()
        while user_all_month not in month_response: 
            user_all_month = input('Please enter a correct spelling of the month you want data on. Thank you. ').capitalize()
        user_all_day = input('what day would you want to view?: ')
        user_all_day = user_all_day.capitalize()

        while user_all_day not in day_response: 
                user_all_day = input('Please enter a correct spelling of the day you want data on. Thank you. ').capitalize()
        #   Retrieving city data by month and day  
        def get_all_data(df): 
            all_data = df[(df['Month'] == user_all_month ) & (df['Day'] == user_all_day)]
            print('Okay then! Lets explore the data with your chosen filters!\n.')
            print('AS IT PARTAINS TO THE TIMES OF TRAVEL')
    #       ***Computing for Hour
            def all_time_stats(df):
                def all_common_hour(df):
                    print('***Computing the most common hour of day in a 24hr clock...')
                    start_time = time.time() 
                    all_user_day = df['Day'] == user_all_day
                    all_user_month = df['Month'] == user_all_month
                    common_all_hour = df.loc[all_user_month][all_user_day]['Hour'].value_counts().idxmax()
    #             Calculating hour count per month
                    all_user_day = df['Day'] == user_all_day
                    all_user_month = df['Month'] == user_all_month
                    common_all_hour_count = df.loc[all_user_month][all_user_day]['Hour'].value_counts().max()
                    print('The most common hour is {}.00\nWith a total count of {} hours in the start time\n'.format(common_all_hour, common_all_hour_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                all_common_hour(df)
            all_time_stats(df)      

    #        ***Computing for Start Stations
            def all_station_stats(df): 
                print('\nAS IT PARTAINS TO STATIONS AND TRIPS')
                #       ***Computing common Start Station
                def all_common_start_station(df):
                    print('***Computing the most common start station...')
                    start_time = time.time()
                    all_user_day_start_station= df['Day'] == user_all_day
                    all_user_month_start_station = df['Month'] == user_all_month
                    all_common_start_station = df.loc[all_user_month_start_station][all_user_day_start_station]['Start Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    all_user_day_start_station= df['Day'] == user_all_day
                    all_user_month_start_station = df['Month'] == user_all_month
                    all_common_start_station_count = df.loc[all_user_month_start_station][all_user_day_start_station]['Start Station'].value_counts().max()
                    print('The most common start station is: {}\nWith a total count of {}\n'.format(all_common_start_station, all_common_start_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                all_common_start_station(df)

        #       ***Computing common End Stations
                def all_common_end_station(df):
                    print('***Computing the most common end station...')
                    start_time = time.time()
                    all_user_day_end_station = df['Day'] == user_all_day
                    all_user_month_end_station = df['Month'] == user_all_month
                    all_common_end_station = df.loc[all_user_month_end_station][all_user_day_end_station]['End Station'].value_counts().idxmax()
        #             Calculating start station count per month           
                    all_user_day_end_station = df['Day'] == user_all_day
                    all_user_month_end_station = df['Month'] == user_all_month
                    all_common_end_station_count = df.loc[all_user_month_end_station][all_user_day_end_station]['End Station'].value_counts().max()
                    print('The most common End station is: {}\nWith a total count of {}\n'.format(all_common_end_station, all_common_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                all_common_end_station(df)

        #       ***Computing for Start and End Stations
                def all_start_and_end_station(df):
                    print('***Computing the most common trip from start to end. That is the most frequent combination of start and end stations...\n')
                    start_time = time.time()
                    all_user_start_end_station_day = df['Day'] == user_all_day
                    all_user_start_end_station_month = df['Month'] == user_all_month
                    all_common_start_end_station = df.loc[all_user_start_end_station_month][all_user_start_end_station_day][['Start Station', 'End Station']].value_counts().idxmax()
        #             Calculating start and end station count per month
                    all_user_start_end_station_day= df['Day'] == user_all_day
                    all_user_start_end_station_month = df['Month'] == user_all_month
                    all_common_start_end_station_count = df.loc[all_user_start_end_station_month][all_user_start_end_station_day][['Start Station', 'End Station']].value_counts().max()
                    print('The most common start and end stations are {}\nWith a total count of {}\n'.format(all_common_start_end_station, all_common_start_end_station_count))
                    print("This took %s seconds." % (time.time() - start_time))
                    print('-'*40)
                all_start_and_end_station(df)
            all_station_stats(df)

        #       ***Computing for Travel Time
            def day_trip_duration(df): 
                print('AS IT PARTAINS TO TRIP DURATIONS')
                print('***Computing the total travel time...')
                start_time = time.time()
                all_user_trip_duration_day = df['Day'] == user_all_day
                all_user_trip_duration_month = df['Month'] == user_all_month
                all_total_trip_duration =  df.loc[all_user_trip_duration_month][all_user_trip_duration_day]['Trip Duration'].sum()
                all_total_trip_duration_average = int(df.loc[all_user_trip_duration_month][all_user_trip_duration_day]['Trip Duration'].mean())
                print('The total travel time is {}\nWith an average of {}'.format(all_total_trip_duration, all_total_trip_duration_average))
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            day_trip_duration(df)

        #         ***Computing User Info  
            def all_number_of_users(df): 
                print('AS IT PARTAINS TO USER INFORMATION')
                print('***Computing the total number for each type of user...')
                start_time = time.time()
                all_user_number_day = df['Day'] == user_all_day
                all_user_number_month = df['Month'] == user_all_month
                all_user_number_info =  df.loc[all_user_number_month][all_user_number_day]['User Type'].value_counts()
                print(all_user_number_info)
                print("This took %s seconds." % (time.time() - start_time))
                print('-'*40)
            all_number_of_users(df)

        #       ***Computing gender and birth year for only new york city and chicago
        #       ***For Gender
            def all_gender_number(df):
                for column in df: 
                    if 'Gender' in df: 
                        print('***Computing the total number for each gender...')
                        start_time = time.time()
                        all_gender_type_day = df['Day'] == user_all_day
                        all_gender_type_month = df['Month'] == user_all_month
                        all_gender_type_count = df.loc[all_gender_type_month][all_gender_type_day]['Gender'].value_counts()
                        print('{}\n'.format(all_gender_type_count))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            all_gender_number(df)

        #       ***For Birth Year
        #       ***Most frequent birth year
            def all_frequent_birth_year(df):
                for column in df:
                    if 'Birth Year' in df: 
                        print('***Computing the most frequent birth year and the most recent birthyear')
                        print('For the most frequent birth year..')
                        start_time = time.time()
                        all_frequent_birth_year_day = df['Day'] == user_all_day
                        all_frequent_birth_year_month = df['Month'] == user_all_month
                        all_frequent_birth_year = df.loc[all_frequent_birth_year_month][all_frequent_birth_year_day]['Birth Year'].value_counts().idxmax()
                        all_frequent_birth_year = int(all_frequent_birth_year)
                        print('The most frequent birth year is: {}\n'.format(all_frequent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break 
                    else: 
                        pass
            all_frequent_birth_year(df)

            #       ***Most recent birth year
            def all_recent_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the most recent birth year..')
                        start_time = time.time()
                        all_recent_birth_year_day = df['Day'] == user_all_day
                        all_recent_birth_year_month = df['Month'] == user_all_month
                        all_recent_birth_year = int(df.loc[all_recent_birth_year_month][all_recent_birth_year_day]['Birth Year'].max())
                        print('The most recent birth year is {}\n'.format(all_recent_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            all_recent_birth_year(df)
        #        ***Earliest birth year
            def all_earliest_birth_year(df):
                for column in df: 
                    if 'Birth Year' in df:
                        print('For the earliest birth year..')
                        start_time = time.time()
                        all_earliest_birth_year_day = df['Day'] == user_all_day
                        all_earliest_birth_year_month = df['Month'] == user_all_month
                        all_earliest_birth_year = int(df.loc[all_earliest_birth_year_month][all_earliest_birth_year_day]['Birth Year'].min())
                        print('The most earliest year is {}\n'.format(all_earliest_birth_year))
                        print("This took %s seconds." % (time.time() - start_time))
                        print('-'*40)
                        break
                    else: 
                        pass
            all_earliest_birth_year(df)
        #           ***Starting the program again
            def explore_over_again():
                    raw_data = input('Would you like to see some raw data? Please respond with a "y" or "no": ').lower()
                    while raw_data not in possible_raw_data_resonse: 
                        raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    count = 0
                    while raw_data == 'y': 
                        count += 5
                        show_raw_data = all_data.head(count)
                        show_raw_data
                        print(show_raw_data)
                        if count == len(all_data.index): 
                            print('There is no more data to show')
                        else: 
                            raw_data = input('Do you want to see some more?: y or n: ').lower()
                            while raw_data not in possible_raw_data_resonse: 
                                raw_data = input('Please enter a correct response from above. Thank you. ').lower()
                    start_over = input('Do you want to explore bikeshare data again? y or n: ').lower()
                    while start_over not in possible_start_over_resonse: 
                        start_over = input('Please enter a correct response from above. Thank you. ').lower()
                    if start_over == 'y': 
                        load_data()
                    else: 
                        print('Thank you for exploring the bikeshare data.\n')
            explore_over_again()
        get_all_data(df)
load_data()