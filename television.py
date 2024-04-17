class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if not self.__status:
            pass
        elif self.__muted:
            self.__muted = False
        else:
            self.__muted = True

    def channel_up(self):
        if not self.__status:
            pass
        elif self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL
        else:
            self.__channel += 1

    def channel_down(self):
        if not self.__status:
            pass
        elif self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL
        else:
            self.__channel -= 1

    def volume_up(self):
        if self.__muted:
            self.mute()

        if self.__status and self.__volume < self.MAX_VOLUME:
            self.__volume += 1

    def volume_down(self):
        if self.__muted:
            self.mute()

        if self.__status and self.__volume > self.MIN_VOLUME:
            self.__volume -= 1

    def __str__(self):
        if self.__muted:
            return ("Power = " + str(self.__status)
                    + ", Channel = " + str(self.__channel)
                    + ", Volume = 0")
        else:
            return ("Power = " + str(self.__status)
                    + ", Channel = " + str(self.__channel)
                    + ", Volume = " + str(self.__volume))
