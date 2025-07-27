import time
import pygame

pygame.init()
pygame.mixer.init()

ask = input("Enter how long should the timer run:")
if ask.isdigit():
    ask = int(ask)
else:
    raise Exception("Invalid Input!")

print("")

for i in range(ask, 0, -1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print(f"{hours:02}:{minutes:02}:{seconds:02}")

    time.sleep(1)

print("\nCountdown is over!!")


def play_sound():
    try:
        # 2. CORRECT THE PATH TO YOUR ACTUAL MP3 FILE
        # Example: Assuming you have an MP3 file named 'alarm.mp3'
        # in the same directory as your Python_Apps/Timer directory, or
        # anywhere else. Make sure the path is correct.
        mp3_file_path = "/home/user/Python_Apps/Timer/timer_end.mp3"  #! <--- **CHANGE THIS TO YOUR REAL MP3 FILE PATH**

        pygame.mixer.music.load(mp3_file_path)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(3)  # Plays 3 times

        while pygame.mixer.music.get_busy():
            # This line keeps the program running while the music plays.
            # 5 FPS is enough for audio playback without consuming much CPU.
            pygame.time.Clock().tick(5)

        print("\nSound playback finished.")

    except pygame.error as error:
        print(f"Error playing sound: {error}")
    finally:
        # Optional: Uninitialize mixer if this is the only place it's used
        # pygame.mixer.quit()
        pass  # If you have other Pygame parts, don't quit here


play_sound()
