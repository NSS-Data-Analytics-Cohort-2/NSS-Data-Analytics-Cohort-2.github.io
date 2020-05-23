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
                        "proImg": "../assets/img/{}1.jpg".format(row['First'].lower()),
                        "funImg": "../assets/img/{}2.jpg".format(row['First'].lower())}
        cohort_json['cohort'].append(student_dict)
    return cohort_json


def make_cohort_json(df_path):
    df = prepare_df(df_path)
    cohort_json = make_cohort_dict(df)
    with open("cohort.json", "w") as outfile:
        json.dump(cohort_json, outfile)
    print("cohort.json created!")


def convert_to_jpg(img_path):
    '''
    Converts image to JPEG and saves new file with .jpg extension
    '''
    img = Image.open(img_path)
    new_path = '.'.join(img_path.split(".")[:-1]) + ".jpg" # join with '.' in case multiple . in path
    img.save(new_path, "JPEG")


def calc_min_img_ratio(img_dir):
    min_ratio = 10000 #just make a really large number to start with
    for img_path in os.listdir(img_dir):
        img = Image.open(img_dir+img_path)
        s = img.size
        if s[0]/s[1] < min_ratio:
            min_ratio = s[0]/s[1]
    return min_ratio


def crop_image(img_path, ratio, desired_width = 1024, desired_height = 153):
    img = Image.open(img_path)
    width, height = img.size

    new_height_half = (width/ratio)/2

    cropped = img.crop((0, new_height_half, width, height - new_height_half))
    cropped.save(img_path, "JPEG")
