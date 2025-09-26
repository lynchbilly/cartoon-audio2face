# Cartoon Audio2Face Mobile App – In-Depth Guide

This project is a cartoon-style mobile app demo built with Python and Kivy. The ultimate goal is to sync cartoon character facial animations to audio, using NVIDIA's Audio2Face technology.

---

## Table of Contents

- Features
- Application Architecture & Code Walkthrough
- Prerequisites
- Installation & Setup (User Guide)
- Using the App
- File Structure & Asset Preparation
- Contributor/Developer Guide
  - Development Environment
  - Code Extension Points & API Integration
  - Testing & Debugging
  - Building for Mobile (Android/iOS)
  - Contributing Guidelines
- Troubleshooting & FAQ
- Resources
- License

---

## Features

- Cartoon avatar display using Kivy UI.
- Button to simulate syncing lips to audio (currently a stub).
- Modular structure for future integration with NVIDIA Audio2Face SDK.
- Designed for desktop and future mobile deployment.

---

## Application Architecture & Code Walkthrough

### Main Application (`main.py`)

- **Kivy UI Components:**
  - Vertical `BoxLayout` with:
    - `Image` widget for avatar (loads from `assets/cartoon_avatar.png`)
    - `Label` for status messages
    - `Button` ("Sync with Audio")
- **Event Handling:**
  - Button press triggers `sync_audio` method.
  - This calls `sync_avatar_with_audio` from `audio2face_stub.py`, passing avatar and audio paths.
  - Status label updates with result; currently, this is a stub response.

#### Code Excerpt:
```python
class CartoonAudio2FaceApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.avatar = Image(source='assets/cartoon_avatar.png')
        self.status = Label(text="Press to sync lips to audio!")
        btn = Button(text='Sync with Audio')
        btn.bind(on_press=self.sync_audio)
        layout.add_widget(self.avatar)
        layout.add_widget(self.status)
        layout.add_widget(btn)
        return layout

    def sync_audio(self, instance):
        self.status.text = sync_avatar_with_audio('assets/cartoon_avatar.png', 'assets/sample_audio.wav')
```

### Stub Logic (`audio2face_stub.py`)

- Function: `sync_avatar_with_audio(avatar_path, audio_path)`
- Currently returns a fixed message: "Cartoon avatar lips synced to audio! (stubbed)"
- **Developer Note:** Replace with actual Audio2Face API logic for real facial animation.

### Dependencies (`requirements.txt`)

- Placeholder comments for future dependencies:
  - Audio2Face SDK/API
  - Advanced animation libraries
  - Build tools (Buildozer, PyInstaller)
- **Developer Note:** Add `kivy` and any actual dependencies needed for your environment.

---

## Prerequisites

- Python 3.7 or newer.
- pip (Python package manager).
- Kivy (`pip install kivy`)
- An image named `cartoon_avatar.png` in the `assets` directory.
- (Optional) Sample audio file: `assets/sample_audio.wav`.

---

## Installation & Setup (User Guide)

1. **Clone the repository**
   ```sh
   git clone https://github.com/lynchbilly/cartoon-audio2face.git
   cd cartoon-audio2face
   ```

2. **(Recommended) Switch to the test branch**
   ```sh
   git checkout test
   ```

3. **Install dependencies**
   ```sh
   pip install kivy
   # Add other dependencies from requirements.txt as needed
   ```

4. **Prepare assets**
   - Place your preferred cartoon avatar image at `assets/cartoon_avatar.png`.
   - (Optional) Add an audio file at `assets/sample_audio.wav` for future features.

5. **Run the app**
   ```sh
   python main.py
   ```

---

## Using the App

- On launch, you’ll see your cartoon avatar.
- Press the "Sync with Audio" button to simulate facial animation syncing (stubbed).
- The status label updates (no real animation yet).

---

## File Structure & Asset Preparation

```
cartoon-audio2face/
├── main.py                # Main Kivy app logic
├── audio2face_stub.py     # Stub for future Audio2Face integration
├── requirements.txt       # Python dependencies and future integration notes
├── assets/
│   ├── cartoon_avatar.png # User-supplied avatar image
│   └── sample_audio.wav   # (Optional) Audio sample
├── README.md              # Project overview
```

---

## Contributor/Developer Guide

### Development Environment

- Fork, clone, and create a feature branch:
  ```sh
  git checkout -b my-feature-branch
  ```
- Install dependencies as above.
- Run and test via `python main.py`.

### Code Extension Points & API Integration

- **audio2face_stub.py**: Replace stub logic with real API integration.
  - Example integration steps:
    1. Load and preprocess audio input.
    2. Send to Audio2Face API or SDK.
    3. Receive facial animation data (typically blendshapes or keyframes).
    4. Apply animation data to the Kivy avatar.
    5. Handle errors and display status in the UI.

- **main.py**: Extend UI (add animation controls, avatar customization, audio recording/upload, etc.).
  - Consider async calls for smooth UI when integrating with external APIs.

- **requirements.txt**: Add all required third-party libraries as you expand features.

### Testing & Debugging

- Test avatar and audio file presence.
- Add unit tests for new functions (animation logic, API wrappers).
- Validate API integration with mock responses before implementing full pipeline.

### Building for Mobile (Android/iOS)

- **Android:** Use [Buildozer](https://github.com/kivy/buildozer)
  - Install buildozer and dependencies.
  - Setup `buildozer.spec` for permissions (audio, file access).
  - Build with `buildozer android debug` or `release`.
- **iOS:** Use [Kivy-ios](https://github.com/kivy/kivy-ios)
  - Follow Kivy-ios setup instructions.
  - Update Xcode project with necessary permissions.

### Contributing Guidelines

- Fork and branch for features/fixes.
- Make atomic, well-commented commits.
- Write or update docstrings for new code.
- Open issues for bugs, feature requests, or questions.
- Review README.md and GUIDE.md for context before contributing.

---

## Troubleshooting & FAQ

- **App won’t launch:** Check Python/Kivy installation and asset locations.
- **Missing avatar:** Ensure `cartoon_avatar.png` exists in `assets/`.
- **Button does nothing:** Confirm stub logic and correct file paths.
- **Dependency errors:** Add missing libraries to requirements.txt and install.
- **Mobile build fails:** Review platform-specific documentation, ensure all dependencies and permissions are set.
- **Audio2Face integration not working:** This feature is not yet implemented; current version uses stub only.

---

## Resources

- [Kivy Documentation](https://kivy.org/doc/stable/)
- [NVIDIA Audio2Face SDK](https://developer.nvidia.com/nvidia-audio2face)
- [Buildozer for Android](https://github.com/kivy/buildozer)
- [Kivy-ios](https://github.com/kivy/kivy-ios)

---

## License

MIT (or your choice).

---

_For more details, see the repository README: https://github.com/lynchbilly/cartoon-audio2face/blob/main/README.md_