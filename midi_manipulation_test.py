import midi_manipulation
import numpy as np

songs = np.zeros((0, 156))


def test_noteStateMatrixToMidi():
    assert midi_manipulation.noteStateMatrixToMidi(songs) is None
