import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics.pairwise import cosine_similarity
from scipy.spatial.distance import cdist
import spotipy
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyClientCredentials

cid = "223038519aea42c28ef5bf07ebcce55d"
cis = "38a99ad9abe74a00ab4b9cee1f8aa31c"

auth_manager = SpotifyClientCredentials(client_id=cid, client_secret=cis)
sp = spotipy.Spotify(auth_manager = auth_manager)

# Load the dataset globally
tracks = pd.read_csv('web_flask/datas.csv')

# Preprocessing and similarity calculation
def preprocess_tracks(tracks):
    # Features to use for the recommendation system
    selected_features = ['loudness', 'track_popularity', 'danceability', 'genres']

    # Drop rows with missing values in the selected features
    tracks = tracks.dropna(subset=selected_features)

    # Normalize numerical features
    scaler = MinMaxScaler()
    tracks[['danceability', 'valence', 'loudness', 'track_popularity']] = scaler.fit_transform(tracks[['danceability', 'valence', 'loudness', 'track_popularity']])

    # Encode categorical features
    encoder = LabelEncoder()
    tracks['genres'] = encoder.fit_transform(tracks['genres'])
    tracks['artist'] = encoder.fit_transform(tracks['artist'])

    # Define the features for similarity calculation
    features_for_similarity = ['loudness', 'track_popularity', 'danceability', 'genres'] 
    
    feature_matrix = tracks[features_for_similarity].values
    return feature_matrix

# Preprocess tracks and get the feature matrix
feature_matrix = preprocess_tracks(tracks)


def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend_songs(song_name, n=10):
    # Check if the song exists in the dataset
    if song_name not in tracks['track'].values:
        return f"Song '{song_name}' not found in the dataset."

    # Find the index of the song
    song_idx = tracks[tracks['track'] == song_name].index[0]

    # Compute distances from the input song to all other songs
    distances = cdist([feature_matrix[song_idx]], feature_matrix, metric='euclidean')[0]

    # Get the indices of the n closest songs (excluding the input song itself)
    similar_songs_idx = distances.argsort()[1:n+1]

    # Get the names of the most similar songs
    similar_tracks = tracks.iloc[similar_songs_idx][['track', 'artist']].values
    
    # Format the results as a list of dictionaries
    recommendations = []
    for track, artist in similar_tracks:
        album_cover_url = get_song_album_cover_url(track, artist)  # Fetch album cover
        recommendations.append({'track': track, 'artist': artist, 'album_cover_url': album_cover_url})
    
    return recommendations

def search_songs(query):
    filtered_songs = tracks[
        (tracks['track'].str.lower().str.contains(query)) | 
        (tracks['artist'].str.lower().str.contains(query))
    ]

    # Convert the filtered results to a list of dictionaries
    filtered_songs_list = filtered_songs.to_dict('records')

    # Return the filtered results as JSON
    return filtered_songs_list
