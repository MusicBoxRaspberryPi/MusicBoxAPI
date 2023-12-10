<h1 align="center" id="title">Music Box API</h1>

<p align="center"><img src="https://socialify.git.ci/MusicBoxRaspberryPi/MusicBoxAPI/image?description=1&amp;font=Inter&amp;language=1&amp;name=1&amp;owner=1&amp;theme=Light" alt="project-image"></p>


## 🛠️ Installation

1. Clone the repository `git clone https://github.com/MusicBoxRaspberryPi/MusicBoxAPI`
2. Rename `.env.dist` to `.env`
3. Edit `.env` to your needs
4. Install dependencies `pip install -r requirements.txt`
5. [Create Spotify App](https://developer.spotify.com/dashboard) with redirect URIs: `http://localhost:8080`
6. Copy **Client ID** and **Client Secret** from _Spotify App -> Settings -> View client secret_ to `.env`
7. Run `python -m app.spotify.service`, webpage should open in your browser and `.cache` file should be created

## 🚀 Usage

- With Docker: `docker compose up`

- Without Docker: `python -m app.main`
