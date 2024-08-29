import pygame

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

if __name__ == "__main__":
    play_music('sample_music.mp3')
