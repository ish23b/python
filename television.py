class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Method to initialize an object in the class
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn on and off the power
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        """
        Method to mute the volume
        """
        if self.__status:
            if self.__muted == False:
                self.__muted = True
            else:
                self.__muted = False
    def channel_up(self) -> None:
        """
        Method to increase the tv channel.
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to turn up the volume a single level and,
        if muted, to unmute and then turn up volume a single level
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to turn down the volume a single level and,
        if muted, to unmute and then turn down volume a single level
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to display the tv status, channel, and volume.
        :return: display of tv status, channel, and volume.
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
