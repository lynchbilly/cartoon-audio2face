# Magical Cartoon Audio2Face Deployment Guide (Test Branch Edition)

Follow these steps – anyone can do it, even a 10-year-old! 🌟

## 1. Install Python

First, make sure Python is installed (version 3.7 or higher).

- Go to [python.org/downloads](https://www.python.org/downloads/)
- Download and install Python for your computer.
- When installing, check “Add Python to PATH” if asked.

## 2. Install pip (Python package manager)

Most Python downloads include pip automatically. To check, open Command Prompt (Windows) or Terminal (Mac/Linux):

```sh
python --version
pip --version
```

If pip isn’t installed, see [pip installation guide](https://pip.pypa.io/en/stable/installation/).

---

## 3. Open a Terminal

- On Windows: Search for “cmd” and open Command Prompt.
- On Mac: Open “Terminal” from Applications.
- On Linux: Use Ctrl+Alt+T.

---

## 4. Clone the Project

Copy and paste this into your terminal:

```sh
git clone https://github.com/lynchbilly/cartoon-audio2face.git
cd cartoon-audio2face
```

---

## 5. Switch to the Magical Test Branch

```sh
git checkout test
```

---

## 6. Install Dependencies

Install Kivy and everything from requirements.txt:

```sh
pip install kivy
pip install -r requirements.txt
```

---

## 7. Prepare Assets

Make a folder called `assets` inside the project folder (if it isn’t there already).

- Put your favorite cartoon picture in `assets/cartoon_avatar.png`
- (Optional) Add a sound file called `assets/sample_audio.wav`

---

## 8. Run the App

Start the magic:

```sh
python main.py
```

---

## 9. What Happens Next?

- You’ll see your cartoon avatar on the screen.
- Press the “Sync with Audio” button to make it pretend to talk (just for fun – actual animation coming soon).
- Watch the status message change!

---

## 10. Troubleshooting (If It Doesn’t Work)

- Is Python installed? Type `python --version`
- Is Kivy installed? Type `pip show kivy`
- Is your cartoon image in the right spot? It must be `assets/cartoon_avatar.png`
- Still stuck? Ask an adult or check the [README](https://github.com/lynchbilly/cartoon-audio2face/blob/main/README.md) or [GUIDE.md](https://github.com/lynchbilly/cartoon-audio2face/blob/test/GUIDE.md)!  

---

## 11. Going Further (Magical Deployment)

- For mobile (Android): Install [Buildozer](https://github.com/kivy/buildozer) and run:
  ```sh
  pip install buildozer
  buildozer init
  buildozer android debug
  ```
- For iOS: See [Kivy-ios](https://github.com/kivy/kivy-ios) for instructions.

---

## 12. License

MIT (or your choice).

---

✨ You did it! You’re a magical app deployer! ✨
