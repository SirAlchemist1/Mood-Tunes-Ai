import os
from flask import Flask, request, jsonify, send_from_directory
import requests
import random
from datetime import datetime, timedelta

app = Flask(__name__)

# Replace with your Last.fm API key
LASTFM_API_KEY = 'e51d44e35bff0e17a94c2a2b87860d19'
LASTFM_API_URL = 'http://ws.audioscrobbler.com/2.0/'

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('.', path)

@app.route('/generate_playlist', methods=['POST'])
def generate_playlist():
    prompt = request.json.get('prompt')
    try:
        tracks = get_tracks_for_prompt(prompt)
        return jsonify({'playlist': tracks})
    except Exception as e:
        app.logger.error(f"Error generating playlist: {str(e)}", exc_info=True)
        return jsonify({'error': str(e)}), 500

def get_tracks_for_prompt(prompt):
    if prompt.lower() == "new music":
        tracks = get_new_releases()
    else:
        tracks = search_tracks(prompt)
    
    if len(tracks) < 20:
        tracks += get_popular_tracks(20 - len(tracks))
    
    random.shuffle(tracks)
    return tracks[:20]

def search_tracks(query):
    params = {
        'method': 'track.search',
        'track': query,
        'api_key': LASTFM_API_KEY,
        'format': 'json',
        'limit': 50
    }
    response = requests.get(LASTFM_API_URL, params=params)
    data = response.json()
    tracks = data.get('results', {}).get('trackmatches', {}).get('track', [])
    return [format_track(track) for track in tracks if int(track.get('listeners', 0)) > 10000]

def get_new_releases():
    # This is a workaround as Last.fm doesn't have a direct "new releases" API
    # We're using the weekly track chart and assuming these are relatively new/popular
    params = {
        'method': 'chart.gettoptracks',
        'api_key': LASTFM_API_KEY,
        'format': 'json',
        'limit': 50
    }
    response = requests.get(LASTFM_API_URL, params=params)
    data = response.json()
    return [format_track(track) for track in data.get('tracks', {}).get('track', [])]

def get_popular_tracks(limit):
    params = {
        'method': 'chart.gettoptracks',
        'api_key': LASTFM_API_KEY,
        'format': 'json',
        'limit': limit
    }
    response = requests.get(LASTFM_API_URL, params=params)
    data = response.json()
    return [format_track(track) for track in data.get('tracks', {}).get('track', [])]

def format_track(track):
    return {
        'artist': track['artist']['name'] if isinstance(track['artist'], dict) else track['artist'],
        'track': track['name'],
        'url': track['url'],
        'listeners': int(track.get('listeners', 0))
    }

if __name__ == '__main__':
    app.run(debug=True)