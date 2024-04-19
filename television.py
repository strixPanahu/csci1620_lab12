"""
    CSCI 1620 001/851
    Professor Owora
    Week 13 - Lab 12
    16/04/2024

    https://github.com/strixPanahu/python
"""


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Television object with power, channels, volume, and muting.
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """
        Power TV on or off
        :return: None
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Enable or disable TV mute
        :return: None
        """
        if not self.__status:
            pass
        elif self.__muted:
            self.__muted = False
        else:
            self.__muted = True
            self.__volume = 0

    def channel_up(self):
        """
        Cycle channel by one increment
        :return:
        """
        if not self.__status:
            pass
        elif self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self):
        """
        Cycle channel by one decrement
        :return: None
        """
        if not self.__status:
            pass
        elif self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self):
        """
        Increase volume by one unit
        :return: None
        """
        if self.__muted:
            self.mute()

        if self.__status and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        """
        Decrease volume by one unit
        :return: None
        """
        if self.__muted:
            self.mute()

        if self.__status and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Query current power status, channel, and volume.
        :return: String containing instance vars
        """
        return ("Power = " + str(self.__status)
                + ", Channel = " + str(self.__channel)
                + ", Volume = " + str(self.__volume))
