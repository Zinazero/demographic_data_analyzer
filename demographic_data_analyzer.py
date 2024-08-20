import pandas as pd # type: ignore


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=0,
                     names=['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male = df[df['sex'] == 'Male']
    average_age_men = round(male['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    total_bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round(((total_bachelors / total_people) * 100), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    education_levels = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(education_levels)]
    total_higher_education = len(higher_education)
    total_higher_ed_rich = len(higher_education[higher_education['salary'] == '>50K'])
    higher_education_rich = round(((total_higher_ed_rich / total_higher_education) * 100), 1)
    
    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(education_levels)]
    total_lower_education = len(lower_education)
    total_lower_ed_rich = len(lower_education[lower_education['salary'] == '>50K'])
    lower_education_rich = round(((total_lower_ed_rich / total_lower_education) * 100), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = len(min_workers)
    num_min_workers_rich = len(min_workers[min_workers['salary'] == '>50K'])
    rich_percentage = round(((num_min_workers_rich / num_min_workers) * 100), 1)

    # What country has the highest percentage of people that earn >50K?
    rich = df[df['salary'] == '>50K']
    grouped = df.groupby('native-country')
    total_counts = grouped.size()
    rich_counts = rich.groupby('native-country').size()
    percentage_rich = (rich_counts / total_counts * 100)
    
    highest_earning_country = percentage_rich.idxmax()
    highest_earning_country_percentage = round(percentage_rich.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    
    rich_IN = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = rich_IN['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

