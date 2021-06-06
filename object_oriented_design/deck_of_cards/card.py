from abc import ABC, abstractmethod


class Card(ABC):

    def __init__(self, rank, suite):
        self._rank = rank
        self._suite = suite
        self._is_face_down = True

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, val):
        self._rank = val

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, val):
        self._suite = val

    @property
    def is_face_down(self):
        return self._is_face_down

    @is_face_down.setter
    def set_face_down(self):
        self._is_face_down = True

    @is_face_down.setter
    def set_face_up(self):
        self._is_face_down = False

    @abstractmethod
    def value(self):
        pass

    def __str__(self):
        return f"{self._suite} {self.rank}"

