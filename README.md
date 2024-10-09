# MoodTunes AI

MoodTunes AI is a web application that generates personalized music playlists based on user input. It uses the Last.fm API to fetch and recommend tracks based on genres, moods, or specific requests like "new music".

## Features

- Generate playlists based on user input (genre, mood, or "new music")
- Display track information including artist, song name, and popularity
- Responsive and visually appealing user interface
- Integration with Last.fm API for music data

## Technologies Used

- Frontend: HTML, CSS, JavaScript
- Backend: Python with Flask
- API: Last.fm API
- Development Environment: Cursor

## How It Works

1. Users enter a genre, mood, or "new music" into the input field.
2. The application sends a request to the Flask backend.
3. The backend queries the Last.fm API based on the user's input.
4. A playlist of 20 tracks is generated and returned to the frontend.
5. The frontend displays the playlist with track details and popularity.

## Development with Cursor

This project was developed using Cursor, an AI-powered code editor. Cursor enhanced the development process in several ways:

1. **Code Completion**: Cursor's AI-powered code completion helped in writing both Python and JavaScript code more efficiently.

2. **Error Detection**: The AI assistant in Cursor helped identify and fix errors in real-time, improving code quality.

3. **Code Explanation**: When working with the Last.fm API and Flask routes, Cursor provided helpful explanations of complex code sections.

4. **Refactoring Suggestions**: Cursor offered suggestions for code refactoring, helping to improve the overall structure and readability of the project.

5. **Documentation Generation**: The AI assisted in generating comments and documentation for functions and classes.

Using Cursor significantly streamlined the development process, allowing for faster iteration and improved code quality in the MoodTunes AI project.

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/MoodTunes-AI.git
   ```

2. Install the required Python packages:
   ```
   pip install flask requests
   ```

3. Get a Last.fm API key from [Last.fm API](https://www.last.fm/api/account/create) and replace `'your_lastfm_api_key_here'` in `app.py` with your actual API key.

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000` to use the application.

## Future Improvements

- Implement user accounts and playlist saving functionality
- Add more music sources and APIs for a wider range of tracks
- Improve playlist generation algorithm for better recommendations
- Implement a feature to play song previews directly in the application

## Contributing

Contributions to MoodTunes AI are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).