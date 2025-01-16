# Jarvis: A Personal Voice Assistant 🤖

Jarvis is a Python-based personal voice assistant that can execute various commands such as opening websites, playing music, fetching news, and more. This project leverages technologies like Speech Recognition, Web Browser automation, and environment variable management to create a user-friendly assistant.

---

## Features ✨

- **🎙️ Speech Recognition**: Listens and processes user commands.
- **🔇 Silent Mode**: Enable/disable silent mode for speech output.
- **🌐 Open Websites**: Open commonly used websites like Google, Facebook, LinkedIn, and YouTube.
- **🎵 Music Playback**: Play songs from a predefined music library using YouTube links.
- **📰 News Updates**: Fetch the latest news headlines using the NewsAPI.

---

## Installation Instructions 🛠️

### Prerequisites
- 🐍 Python 3.8 or higher
- 💻 Virtual Environment (optional but recommended)

### Required Libraries 📦
Install the required libraries using the following command:
```bash
pip install speechrecognition pyttsx3 requests python-dotenv
```

### Setting Up ⚙️
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd jarvis
   ```
3. Create a `.env` file in the root directory and add your NewsAPI key:
   ```env
   NEWSAPI_KEY=your_api_key_here
   ```
4. (Optional) Activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

---

## Usage 🚀

### Run the Assistant
Execute the following command to start Jarvis:
```bash
python jarvis.py
```

### Commands 🗒️
| Command           | Description                                 |
|-------------------|---------------------------------------------|
| `Jarvis`         | Activates the assistant.                   |
| `open google`    | Opens Google in your default browser.       |
| `play <song>`    | Plays the specified song from the library.  |
| `news`           | Reads the top 5 news headlines.            |
| `silent mode`    | Activates silent mode (no voice output).    |
| `wake up`        | Deactivates silent mode.                    |
| `stop`           | Stops the assistant and exits.             |

### Adding More Songs 🎧
Update the `musicLibrary.py` file to add more songs to the library. Use the following structure:
```python
music["song_title"] = "https://www.youtube.com/watch?v=song_url"
```

---

## Project Structure 📂

```plaintext
MEGA_PROJECT/
├── __pycache__/         # Cached Python files
├── .venv/               # Virtual environment (optional)
├── .gitignore           # Ignored files for Git
├── jarvis.py            # Main script for the voice assistant
├── musicLibrary.py      # Music library with YouTube links
```

---

## Known Issues 🐛
- 🌐 Internet connectivity is required for fetching news and opening YouTube links.
- 🔊 Speech recognition may misinterpret commands in noisy environments.

---

## Contributing 🤝

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push to your fork and create a pull request.

---

## License 📜
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Acknowledgments 🙏
- [SpeechRecognition Library](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3 Library](https://pypi.org/project/pyttsx3/)
- [NewsAPI](https://newsapi.org/)
