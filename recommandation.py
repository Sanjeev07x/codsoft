
movies = {
    'The Dark Knight': 'Action',
    'Inception': 'Sci-Fi',
    'The Godfather': 'Crime',
    'Forrest Gump': 'Drama',
    'The Matrix': 'Sci-Fi',
    'Titanic': 'Romance',
    'The Avengers': 'Action',
    'Pulp Fiction': 'Crime',
    'The Shawshank Redemption': 'Drama',
    'The Lion King': 'Animation',
    'Gladiator': 'Action',
    'Jurassic Park': 'Adventure',
    'Avatar': 'Sci-Fi',
    'The Notebook': 'Romance',
    'Toy Story': 'Animation',
    'Star Wars: A New Hope': 'Sci-Fi',
    'The Lord of the Rings: The Fellowship of the Ring': 'Adventure',
    'Fight Club': 'Drama',
    'The Silence of the Lambs': 'Crime',
    'Schindler\'s List': 'Drama',
    'The Prestige': 'Mystery',
    'Shutter Island': 'Thriller',
    'The Social Network': 'Drama',
    'Deadpool': 'Action',
    'Guardians of the Galaxy': 'Action',
    'Interstellar': 'Sci-Fi',
    'Mad Max: Fury Road': 'Action',
    'The Revenant': 'Adventure',
    'The Departed': 'Crime',
    'The Big Lebowski': 'Comedy',
    'The Grand Budapest Hotel': 'Comedy',
    'The Dark Knight Rises': 'Action',
    'La La Land': 'Romance',
    'Zootopia': 'Animation',
    'Finding Nemo': 'Animation',
    'The Hunger Games': 'Adventure',
    'Wonder Woman': 'Action',
    'Spider-Man: Into the Spider-Verse': 'Animation',
    'The Incredibles': 'Animation',
    'Goodfellas': 'Crime',
    'American Beauty': 'Drama',
    'The Truman Show': 'Sci-Fi',
    'Whiplash': 'Drama',
    'The Exorcist': 'Horror',
    'The Shining': 'Horror',
    'Get Out': 'Horror',
    'Jaws': 'Thriller',
    'The Conjuring': 'Horror',
    'A Quiet Place': 'Horror',
    'The Witch': 'Horror',
    'The Matrix Reloaded': 'Sci-Fi',
    'The Godfather: Part II': 'Crime',
    'Pulp Fiction': 'Crime',
    'The Untouchables': 'Crime'
}

# Function to display the available genres
def display_available_genres(movies):
    genres = set(movies.values())
    print("Available genres: ", ", ".join(genres))

# Function to get recommendations based on user input
def get_recommendations(user_genre, movies):
    recommendations = [movie for movie, genre in movies.items() if genre == user_genre]
    return recommendations

# Main function to interact with the user
def movie_recommendation_system():
    print("Welcome to the Movie Recommendation System!")
    
    while True:
        # Display the available genres
        display_available_genres(movies)
        
        # Ask user for their preferred genre
        user_genre = input("Enter your preferred genre: ").capitalize()
        
        # Check if the genre exists
        if user_genre not in set(movies.values()):
            print(f"Sorry, we don't have movies in the {user_genre} genre.")
        else:
            # Get and display recommendations
            recommendations = get_recommendations(user_genre, movies)
            
            if recommendations:
                print(f"\nWe recommend the following {user_genre} movies:")
                for movie in recommendations:
                    print(f"- {movie}")
            else:
                print(f"No movies found in the {user_genre} genre.")
        
        # Ask the user if they want to continue
        continue_choice = input("\nWould you like to get recommendations again? (yes/no): ").lower()
        
        if continue_choice != 'yes':
            print("Thank you for using the Movie Recommendation System! Goodbye!")
            break

# Run the movie recommendation system
movie_recommendation_system()
