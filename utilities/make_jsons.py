
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
