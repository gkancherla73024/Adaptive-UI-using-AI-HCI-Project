
'''
Creates a movie recommendation system using a dataset of Netflix titles.
It classifies the genres of movies, compares the cosine similarity between them and gives individualized movie recommendations depending on the similarity in genres.
The user communicates with a Tkinter-based graphical user interface (GUI) in which the user enters the name of a movie and the system provides a list of recommended movies to the user as a pop-up message box.
'''

# Importing necessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import MultiLabelBinarizer

# Loading the dataset from the specified path
df = pd.read_csv("D:/Datasets/netflix_titles_nov_2019.csv")

# Checking the columns to verify the dataset structure
print(df.columns)

# Selecting relevant columns for movie title, genres, and rating
df = df[['title', 'listed_in', 'rating']]

# Dropping rows with missing values
df = df.dropna()

# Splitting the 'listed_in' column to extract genres (genres are separated by commas)
df['listed_in'] = df['listed_in'].apply(lambda x: x.split(','))

# Binarizing the genres using MultiLabelBinarizer to convert genres into binary format
mlb = MultiLabelBinarizer()
genres_matrix = mlb.fit_transform(df['listed_in'])

# Creating a DataFrame from the binary genre matrix
genres_df = pd.DataFrame(genres_matrix, columns=mlb.classes_)

# Concatenating the genres DataFrame with the original DataFrame to add binary genre columns
df = pd.concat([df, genres_df], axis=1)

# Calculating cosine similarity between movies based on genres
cosine_sim = cosine_similarity(genres_df)


def recommend_movies(user_movie):
    # Finding the index of the movie entered by the user
    movie_index = df[df['title'] == user_movie].index[0]

    # Getting cosine similarity scores for all movies with the selected movie
    sim_scores = list(enumerate(cosine_sim[movie_index]))

    # Sorting the movies based on similarity scores in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Extracting top 5 movie recommendations (excluding the movie itself)
    recommendations = []
    for i in sim_scores[1:6]:
        movie = df['title'].iloc[i[0]]
        recommendations.append(movie)

    return recommendations


def show_recommendations():
    # Getting the movie entered by the user
    user_movie = user_entry.get()

    # Checking if the user movie is in the dataset
    if user_movie in df['title'].values:
        recommendations = recommend_movies(user_movie)
        # Displaying the recommendations in a message box
        messagebox.showinfo("Recommended Movies", "\n".join(recommendations))
    else:
        # Displaying a warning if the movie is not found in the dataset
        messagebox.showwarning("Movie Not Found", "The movie you entered is not in the dataset!")


# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Movie Recommendation System")

# Creating and packing UI components
user_label = tk.Label(root, text="Enter Movie Name:")
user_label.pack()

user_entry = tk.Entry(root)
user_entry.pack()

recommend_button = tk.Button(root, text="Get Recommendations", command=show_recommendations)
recommend_button.pack()

# Starting the GUI event loop
root.mainloop()