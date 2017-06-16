import mido
import time
import random


output = mido.open_output()

for x in range(0, 1000):
    note = random.randint(0, 120)
    note_2 = random.randint(0, 120)
    vel = random.randint(10, 100)
    vel_2 = random.randint(10, 100)
    output.send(mido.Message('note_on', note=note, velocity=vel, channel=1))
    print(note, vel)
    time.sleep(4)
    output.send(
        mido.Message(
            'note_on',
            note=note_2,
            velocity=vel_2,
            channel=2
        ))
    print(note_2, vel_2)
    time.sleep(4)
    output.send(mido.Message('note_off', note=note, velocity=vel, channel=1))
    time.sleep(1)
    output.send(
        mido.Message(
            'note_off',
            note=note_2,
            velocity=vel_2,
            channel=2
        ))
    time.sleep(1)
