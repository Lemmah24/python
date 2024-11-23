class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the Television instance with default values."""
        self.__status = False  # TV is off by default
        self.__muted = False  # TV is unmuted by default
        self.__volume = self.MIN_VOLUME  # Volume starts at the minimum
        self.__channel = self.MIN_CHANNEL  # Channel starts at the minimum

    def power(self) -> None:
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Toggle the mute status of the TV. Muting stores the current volume."""
        if self.__status:  # Only allow mute operation if TV is on
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increase the TV channel, cycling back to the minimum at the maximum."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the TV channel, cycling back to the maximum at the minimum."""
        if self.__status :
            self.__channel = (self.__channel - 1) % (self.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increase the volume, respecting mute and maximum constraints."""
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if volume is adjusted
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume, respecting mute and minimum constraints."""
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if volume is adjusted
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the TV's current status, channel, and volume.
        :return: a string representation of the TV's current state"""

        return f"Power: {'True' if self.__status else 'False'}, Channel: {self.__channel}, Volume: {Television.MIN_VOLUME if self.__muted else self.__volume}"
