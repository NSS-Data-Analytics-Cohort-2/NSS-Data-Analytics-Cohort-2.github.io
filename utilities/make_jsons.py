from PIL import Image
import os


def make_cohort_json(class_info):
    '''
    function to make cohort.json.
    arg class_info: pandas DataFrame, df including minimally the columns:
        First, Last, Tagline, Bio, Github, LinkedIn, and Capstone
    '''
    cohort_json_2 = {"cohort": []}
    for ind, row in class_info.iterrows():
        student_dict = {"id": ind,
                        "firstName": row['First'],
                        "lastName": row['Last'],
                        "reelThemIn": "<p>"+str(row['Tagline']).replace('“', '"').replace('”', '"')+"</p>",
                        "bio": "<p>"+str(row['Bio']).replace('“', '"').replace('”', '"')+"</p>",
                        "github": row['Github'],
                        "linkedIn": row['LinkedIn'],
                        "portfolio": str(row['Capstone']),
                        "proImg": "../assets/img/{}1.jpg".format(row['First'].lower()),
                        "funImg": "../assets/img/{}2.jpg".format(row['First'].lower())}
        cohort_json_2['cohort'].append(student_dict)


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

    # width_diff = width - desired_width
    # height_diff = height - desired_height
    #
    # if width_diff < 0:
    #     raise Exception ("Image too narrow")
    # else:
    #     remove_left_right = width_diff/2
    #
    # if height_diff < 0:
    #     raise Exception ("Image too short")
    # else:
    #     remove_top_bottom = height_diff/2



    cropped = img.crop((0, new_height_half, width, height - new_height_half))
    cropped.save(img_path, "JPEG")
