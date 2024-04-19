from television import Television
import unittest


class TestTelevision(unittest.TestCase):
    def test_pass_init(self):
        self.tv = Television()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_power_on(self):
        self.tv = Television()
        self.tv.power()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 0")

    def test_pass_power_off(self):
        self.tv = Television()
        self.tv.power()
        self.tv.power()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_mute_on(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 0")

    def test_pass_mute_off(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.mute()
        self.tv.volume_up()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 1")

    def test_pass_mute_on_no_power(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.power()
        self.tv.mute()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_pass_mute_off_no_power(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.power()
        self.tv.mute()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_channel_up_no_power(self):
        self.tv = Television()
        self.tv.channel_up()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_channel_up(self):
        self.tv = Television()
        self.tv.power()
        self.tv.channel_up()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 1, Volume = 0")

    def test_pass_channel_up_max(self):
        self.tv = Television()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_channel_down_no_power(self):
        self.tv = Television()
        self.tv.channel_down()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_channel_down_min(self):
        self.tv = Television()
        self.tv.power()
        self.tv.channel_down()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 3, Volume = 0")

    def test_pass_volume_up_no_power(self):
        self.tv = Television()
        self.tv.volume_up()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_pass_volume_up(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 1")

    def test_pass_volume_up_mute(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        self.tv.volume_up()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 1")

    def test_pass_volume_up_max(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 2")

    def test_pass_volume_down_no_power(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.power()
        self.tv.volume_down()

        self.assertEqual(self.tv.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_pass_volume_down(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 1")

    def test_pass_volume_down_mute(self):
        self.tv = Television()
        self.tv.power()
        self.tv.mute()
        self.tv.volume_down()

        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 0")

    def test_pass_volume_down_min(self):
        self.tv = Television()
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_down()
        self.tv.volume_down()
        self.assertEqual(self.tv.__str__(), "Power = True, Channel = 0, Volume = 0")
