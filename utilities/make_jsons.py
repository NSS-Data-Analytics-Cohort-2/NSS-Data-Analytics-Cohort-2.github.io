from PIL import Image
import os
import pandas as pd
import json


def prepare_df(df_path):
    df = pd.read_csv(df_path)
    if "First" not in df.columns:
        df[["First", "Last"]] = df['Name'].str.replace('  ', ' ').str.split(' ', expand = True)
    return df


def clean_string(s):
    return s.replace('“', '"').replace('”', '"').replace("’", "'").replace("—", "-")


def make_cohort_dict(class_info):
    '''
    function to make cohort.json.
    arg class_info: pandas DataFrame, df including minimally the columns:
        First, Last, Tagline, Bio, Github, LinkedIn, and Capstone
    '''
    cohort_json = {"cohort": []}
    for ind, row in class_info.iterrows():
        student_dict = {"id": ind,
                        "firstName": row['First'],
                        "lastName": row['Last'],
                        "reelThemIn": "<p>"+clean_string(str(row['Tagline']))+"</p>",
                        "bio": "<p>"+clean_string(str(row['Bio']))+"</p>",
                        "github": row['Github'],
                        "linkedIn": row['LinkedIn'],
                        "portfolio": str(row['Capstone (link)']),
                        "proImg": "../assets/img/{}1.jpeg".format(row['First'].lower()),
                        "funImg": "../assets/img/{}2.jpeg".format(row['First'].lower())}
        cohort_json['cohort'].append(student_dict)
    return cohort_json


def make_cohort_json(df_path):
    df = prepare_df(df_path)
    cohort_json = make_cohort_dict(df)
    with open("cohort.json", "w") as outfile:
        json.dump(cohort_json, outfile)
    print("cohort.json created!")
