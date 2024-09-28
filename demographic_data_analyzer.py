import pandas as pd

def calculate_demographic_data(print_data=True):
    # Lê os dados do arquivo CSV
    df = pd.read_csv('adult.data.csv')

    # Quantas pessoas de cada raça estão representadas neste conjunto de dados? Isso deve ser uma série do Pandas com os nomes das raças como rótulos do índice.
    race_count = df['race'].value_counts()

    # Qual é a idade média dos homens?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # Qual é a porcentagem de pessoas que têm um diploma de Bacharel?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / df.shape[0] * 100, 1)

    # Qual a porcentagem de pessoas com educação avançada (`Bachelors`, `Masters` ou `Doctorate`) que ganham mais de 50K?
    # Qual a porcentagem de pessoas sem educação avançada que ganham mais de 50K?

    # Com e sem `Bachelors`, `Masters` ou `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df[~((df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'))]

    # Porcentagem com salário >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').sum() / higher_education.shape[0] * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').sum() / lower_education.shape[0] * 100, 1)

    # Qual é o número mínimo de horas que uma pessoa trabalha por semana (feature `hours-per-week`)?
    min_work_hours = df['hours-per-week'].min()

    # Qual a porcentagem de pessoas que trabalham o número mínimo de horas por semana e têm um salário >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').sum() / min_workers.shape[0] * 100, 1)

    # Qual país tem a maior porcentagem de pessoas que ganham >50K?
    country_salaries = round((df[df["salary"] == ">50K"]["native-country"].value_counts() / df["native-country"].value_counts()) * 100, 1).sort_values(ascending=False)
    highest_earning_country = country_salaries.idxmax()
    highest_earning_country_percentage = country_salaries.max()

    # Identificar a ocupação mais popular entre aqueles que ganham >50K na Índia.
    top_IN_occupation = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]["occupation"].value_counts().index[0]

    if print_data:
        print("Número de cada raça:\n", race_count)
        print("Idade média dos homens:", average_age_men)
        print(f"Porcentagem com diplomas de Bacharel: {percentage_bachelors}%")
        print(f"Porcentagem com educação avançada que ganham >50K: {higher_education_rich}%")
        print(f"Porcentagem sem educação avançada que ganham >50K: {lower_education_rich}%")
        print(f"Tempo mínimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre os que trabalham menos horas: {rich_percentage}%")
        print("País com maior porcentagem de ricos:", highest_earning_country)
        print(f"Maior porcentagem de ricos em um país: {highest_earning_country_percentage}%")
        print("Principais ocupações na Índia:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
