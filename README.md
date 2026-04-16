### Movie Recommendation System Based on Genre Similarity

**Table of Content**

-Overview
-Getting Started
-Dependencies
-Usage
-Code Structure

**Overview**

This is a Python-based movie recommendation system based on content. The system suggests the movies according to the similarity of the genre of an entered movie name. The system compares the similarities of the genres of movies in terms of their cosine and recommends movies with similar genres with the movie the user is interested in. The user approaches the system by using a Tkinter-based graphical user interface (GUI), with which they can use a movie title and get recommendations in a pop-up message box.
Table of Contents

**Getting Started**

i. To execute this project locally, do the following steps:

ii. Clone the repository to your local machine:
git clone <repository_url>

iii. Change into the project directory:
cd movie-recommendation-system

iV. Make sure to install the necessary dependencies. You can install them using pip:
pip install -r requirements.txt

v. Get the Dataset: The dataset needed in the project is the netflix_titles_nov_2019.csv file. Make sure that the dataset is at D:/Datasets/netflix_titles_nov_2019.csv or change the path in the code to the new one.


**Dependencies**

The Python libraries to run this project are the following:

i. pandas: For data manipulation and handling.

ii. scikit-learn: To compute the similarity between movie genres in terms of cosine.

iii. tkinter: To create the graphical user interface (GUI).

iv. MultiLabelBinarizer: To convert movie genres to binary.

v. In order to install the dependencies, the following command can be used:
pip install pandas scikit-learn tkinter.


**Usage**

i. Execute the Python script to receive movie recommendations in accordance with the similarity in genres:
python movie_recommendation.py

ii. Type in a movie title on the Tkinter GUI. For example:
Enter movie name: Livius.

iii. See the suggestions in a pop-up message box. The system will give a list of the movies that have similar genres. For example:
Suggested Films:- Ultramarine Magmell, Sword Art Online, Naruto.

iv. Movie Not Found: When the movie entered by the user is not in the dataset the system will show a warning pop-up that the movie is not found.


**Code Structure**

The following are some of the key files that are contained in the project:

i. movie recommendation.py: The code that provides the logic of the movie recommendation system, genre processing, and Tkinter GUI.

ii. netflix - titles - nov 2019.csv: The table of Netflix movie titles, genres and ratings used by the recommendation system.

ii. README.txt: This is a file that gives instructions on how to set up the project, its usage and a brief description of the project.
