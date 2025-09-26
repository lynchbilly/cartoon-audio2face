import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from audio2face_stub import sync_avatar_with_audio

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
        # Stub: this will later call NVIDIA Audio2Face
        self.status.text = sync_avatar_with_audio('assets/cartoon_avatar.png', 'assets/sample_audio.wav')

if __name__ == '__main__':
    CartoonAudio2FaceApp().run()