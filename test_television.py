from television import Television
from pytest import *


def test_pass_init():
    tv = Television()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_power_on():
    tv = Television()
    tv.power()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"


def test_pass_power_off():
    tv = Television()
    tv.power()
    tv.power()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_mute_on():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"


def test_pass_mute_off():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    tv.volume_up()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"


def test_pass_mute_on_no_power():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.power()
    tv.mute()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"


def test_pass_mute_off_no_power():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.power()
    tv.mute()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_channel_up_no_power():
    tv = Television()
    tv.channel_up()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()

    assert tv.__str__() == "Power = True, Channel = 1, Volume = 0"


def test_pass_channel_up_max():
    tv = Television()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_channel_down_no_power():
    tv = Television()
    tv.channel_down()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_channel_down_min():
    tv = Television()
    tv.power()
    tv.channel_down()

    assert tv.__str__() == "Power = True, Channel = 3, Volume = 0"


def test_pass_volume_up_no_power():
    tv = Television()
    tv.volume_up()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 0"


def test_pass_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"


def test_pass_volume_up_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"


def test_pass_volume_up_max():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_up()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 2"


def test_pass_volume_down_no_power():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.power()
    tv.volume_down()

    assert tv.__str__() == "Power = False, Channel = 0, Volume = 1"


def test_pass_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 1"


def test_pass_volume_down_mute():
    tv = Television()
    tv.power()
    tv.mute()
    tv.volume_down()

    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"


def test_pass_volume_down_min():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_down()
    tv.volume_down()
    assert tv.__str__() == "Power = True, Channel = 0, Volume = 0"
