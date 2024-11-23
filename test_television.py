# test_television.py

import pytest
from television import Television
class TestTelevision:
    def setup_method(self):
        self.tv=Television()
    def teardown_method(self):
        del self.tv

    def test_initial_state(self):

        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 0"

    def test_power(self):

        self.tv.power()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"
        self.tv.power()
        assert self.tv.__str__()== "Power: FALSE, Channel: 0, Volume: 0"

    def test_mute(self):

        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"
        self.tv.mute()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 1"
        self.tv.power()
        self.tv.mute()
        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 1"
        self.tv.mute()
        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 1"

    def test_channel_up(self):

        self.tv.channel_up()

        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 0"
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power: TRUE, Channel: 1, Volume: 0"
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"


    def test_channel_down(self):

        self.tv.channel_down()  # Wrap-around to MAX_CHANNEL
        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 0"
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power: TRUE, Channel: 3, Volume: 0"

    def test_volume_up(self):

        self.tv.volume_up()
        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 0"
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 1"
        self.tv.mute()
        self.tv.volume_up()# No change at MAX_VOLUME
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 2"
        self.tv.volume_up()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 2"

    def test_volume_down(self):

        self.tv.volume_down()  # Already at MIN_VOLUME
        assert self.tv.__str__() == "Power: FALSE, Channel: 0, Volume: 0"
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 1"
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"
        self.tv.volume_down()
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"

    def test_volume_unmutes(self):

        self.tv.power()
        self.tv.mute()
        self.tv.volume_up()  # Volume change should unmute
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 1"
        self.tv.mute()
        self.tv.volume_down()  # Volume change should unmute
        assert self.tv.__str__() == "Power: TRUE, Channel: 0, Volume: 0"
