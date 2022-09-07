from playsound import playsound
import multiprocessing

p = multiprocessing.Process(
    target=playsound,
    args=("Breakout.mp3",)
)
p.start()
input('ENter to stop')
p.terminate()
#playsound('Breakout.mp3', False)