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

    def __init__(self) -> None:
        """
        Television object with power, channels, volume, and muting.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Power TV on or off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Enable or disable TV mute
        """
        if not self.__status:
            pass
        elif self.__muted:
            self.__muted = False
        else:
            self.__muted = True
            self.__volume = 0

    def channel_up(self) -> None:
        """
        Cycle channel by one increment
        """
        if not self.__status:
            pass
        elif self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Cycle channel by one decrement
        """
        if not self.__status:
            pass
        elif self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase volume by one unit
        """
        if self.__muted:
            self.mute()

        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease volume by one unit
        """
        if self.__muted:
            self.mute()

        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        Query current power status, channel, and volume.
        :return: String containing instance vars
        """
        return ("Power = " + str(self.__status)
                + ", Channel = " + str(self.__channel)
                + ", Volume = " + str(self.__volume))
