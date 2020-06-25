# NSS Part Time Data Analytics Cohort 2 - [Website](https://NSS-Data-Analytics-Cohort-2.github.io)

## Development

* Clone down the repo
* You need a local server running to power some of the javascript going on.
We like python3. 
Run this in your terminal, within the directory of this project:
```bash
python3.7 -m http.server
``` 
* Then, make changes as needed. 
You should be able to go to `http://localhost:8000/` in your browser!
As you make changes in the code, refresh your browser to see them committed.

### Updating Profile Content
All user profile info is stored in Google Drive.
See [Taylor Perkins](https://github.com/taylorperkins) or [UrLeaka Newsome](https://github.com/unewsome) for access.

Download that file as csv, and save it [here](data/Website%20-%20Website.csv).

Next, open [this notebook](utilities/Make%20JSONs.ipynb) with [Anaconda Navigator](https://www.anaconda.com/products/individual).
Run it from start to finish!
It primary job is to create [this file](data/cohort.json) which is responsible for powering the website!
The output file should have the following fields per user: 
* **firstName** - (First Name) Name of the student
* **lastName** - (Last Name) Last Name of the student
* **reelThemIn** - (Tagline) Small quote (shown on the first card)
* **bio** - (Bio) Longer info (shown on the modal when the user clicks "More!")
* **github** - (Github) Github URL
* **linkedin** - (LinkedIn) LinkedIn URL
* **job_searching** - (Is Job Searching) True / False determines the "Hire Me!" ribbon
* **portfolio** - (Website Portfolio) Either a personal website, 
* **proImg** - Path to the professional [resized images](assets/img/resized) 
* **funImg** - Path to the funny/unprofessional [resized images](assets/img/resized)
* **resume** - Path to the students [resume](assets/resume)
* **id** - Helps for targeting the modal. The notebook will create this for you

Load the website using the ocmmand above and make sure everything is working properly!

### Updating Pictures
All original pictures are stored in Google Drive.
See [Taylor Perkins](https://github.com/taylorperkins) or [UrLeaka Newsome](https://github.com/unewsome) for access.

Download that folder, and unzip the contents into [this folder](assets/img/original). 
All images should have the following filename pattern: `<firstname><number>.<extension>`.
Examples ::

* taylor1.jpg
* urleaka2.png

Pictures with a **1** in the name will be shown on the main page (professional pictures).
Pictures with a **2** in the name will be shown in the modal when a user clicks "More!" (non-professional / funny).

It is important to make sure that the _orient_ of the pictures are accurate! 
No pictures should be rotated.

Next, open [this notebook](utilities/Resizing%20Images.ipynb) with [Anaconda Navigator](https://www.anaconda.com/products/individual). 
This notebook is responsible for "resizing" all images into an appropriate format (2/3) that works with the card height /width ratio on the website.
It will dump the results [here](assets/img/resized).
If a student does not have a "funny" photo, it will also copy their resized "professional" photo to be used as their "funny" photo.

Then, re-run the [cohort notebook](utilities/Make%20JSONs.ipynb) as listed above!

### Updating Resumes
All original resumes are stored in Google Drive.
See [Taylor Perkins](https://github.com/taylorperkins) or [UrLeaka Newsome](https://github.com/unewsome) for access.

Download the resumes, and stick em [here](assets/resume).
Naming pattern is `<firstname>.pdf`.
Please make sure the name is lowercase!

Then, re-run the [cohort notebook](utilities/Make%20JSONs.ipynb) as listed above!

### Updating JS
Muck around in [here](scripts/main.js).

This is all pretty vanilla js. 
React is  for nerds!
But, if you feel like converting it..
We have faith in you.
