## **LAB 12**

## **SUBMISSION INSTRUCTIONS**

- [ ] 0. Submit your GitHub repository link.

## **QUESTION**

- [x] 1. Create a repository named python.

- [x] 2. Within the repository, create a new Python file called television.py where you will write code for the Television class. This class should have the variables and methods below (don’t add any extra methods to the class):

	- [x] a. Class variables (To be declared in the class, outside any methods):

		- [x] i. MIN_VOLUME: This is meant to serve as a constant. Its default value should be 0.

		- [x] ii. MAX_VOLUME: This is meant to serve as a constant. Its default value should be 2.

		- [x] iii. MIN_CHANNEL: This is meant to serve as a constant. Its default value should be 0.

		- [x] iv. MAX_CHANNEL: This is meant to serve as a constant. Its default value should be 3.

		* Where applicable, use these constant variable names rather than hard coding values in your class methods.

	- [x] b. Instance variables (To be declared in the __ init __ method):

		- [x] i. status: This should be treated as a Boolean variable whose initial value is False.

		- [x] ii. muted: This should be treated as a Boolean variable whose initial value is False.

		- [x] iii. volume: This should be treated as an integer variable whose initial value is the minimum volume.

		- [x] iv. channel: This should be treated as an integer variable whose initial value is the minimum channel.

		* All the instance variables should be private.
      
	- [x] c. Methods:

		- [x] i. def__ init__(self): This should be used to set the default instance variables.

		- [x] ii. def power(self): This should be used to turn the tv on and off by changing the value of the status variable.

		- [x] iii. def mute(self): This should be used to mute and unmute the tv when it’s on by changing the value of the muted variable.

		- [x] iv. def channel_up(self): This should be used to increase the tv channel value when the tv is on. If the tv is on the maximum channel and this method is called, it should set the tv channel to the minimum channel (just like a regular tv remote, when you reach the maximum channel and keep pressing the channel up button, you are taken back to the starting/minimum channel).

		- [x] v. def channel_down(self): This should be used to decrease the tv channel value when the tv is on. If the tv is on the minimum channel and this method is called, it should set the tv channel to the maximum channel.

		- [x] vi. def volume_up(self): This should be used to increase the tv volume when the tv is on. If the tv is on the maximum volume and this method is called, the volume should just remain at the maximum (just like a regular tv remote, when you reach the maximum volume and keep pressing the volume up button, nothing happens, it just remains on the maximum volume).

		- [x] vii. def volume_down(self): This should be used to decrease the tv volume when the tv is on. If the tv is on the minimum volume and this method is called, the volume should just remain at the minimum.

			* Please note: If any of the volume methods were called when the tv was muted, that would automatically unmute the tv and adjust the tv volume accordingly.

		- [x] viii. def __ str __ (self): This should be used to send the values of the tv object in the format Power = [status], Channel = [channel], Volume = [volume]. The items placed in brackets would be holding the current values of those tv variables. Refer to the comments in main.py on what the output would look like.

- [x] 3. Test if the code in the Television class works as expected by downloading main.py to the same location television.py is located and then run main.py. The output you get should correspond to that in the comments found in main.py. If you get different values, it means that you need to work on the logic of the methods in the Television class.

- [x] 4. Commit only television.py to your Git repository’s main/master branch.

- [x] 5. Push your repository to your GitHub account.

- [x] 6. Create a new branch named test on your local Git repository (make sure it’s set as the checkout branch — meaning any new changes are going to be saved to it moving forward).

- [x] 7. Add docstrings and type hinting to the methods in television.py.

- [x] 8. Create a new python file called test_television.py. Write unit tests for the __ init __, power, mute, channel_up, channel_down, volume_up, and volume_down methods using the external pytest library (please follow the standards for naming unit test functions).

- [x] 9. Commit the changes to your test branch (At this point the test branch should only contain television.py and test_television.py. Don’t add any extra files or folders — meaning if more files other than television.py and test_television.py appear at the time of committing, make sure to uncheck them that way they are not part of the files saved to your repository). 

- [x] 10. Push the changes to your GitHub account repository.

- [x] 11. Submit the link of your public remote repository.

## **Please note:**

- [x] 12. Don’t merge the 2 branches (we need to check you followed the instructions).

- [x] 13. Make sure any new changes to your code are pushed to the test branch.

- [x] 14. Refer to the testing notes and lecture on how to work with the pytest library.

- [x] 15. Things to test for in the various methods:

	- [x] a. init:

		- [x] i. The status, channel, and volume values.

		- [x] ii. Since you don’t have getter methods, you can use the __str__ method to check the tv values.

	- [x] b. power:

		- [x] i. The tv details when the tv is on.

		- [x] ii. The tv details when the tv is off.

	- [x] c. mute:

		- [x] i. The tv details when the tv is on, volume increased once, and then tv muted.

		- [x] ii. The tv details when the tv is on and unmuted.

		- [x] iii. The tv details when the tv is off and muted.

		- [x] iv. The tv details when the tv is off and unmuted.

	- [x] d. channel_up:

		- [x] i. The tv details when the tv is off and the channel has been increased.

		- [x] ii. The tv details when the tv is on and the channel has been increased.

		- [x] iii. The tv details when the tv is on and one has increased the channel past the maximum value.

	- [x] e. channel_down:

		- [x] i. The tv details when the tv is off and the channel has been decreased.

		- [x] ii. The tv details when the tv is on and one has decreased the channel past the minimum value.

	- [x] f. volume_up:

		- [x] i. The tv details when the tv is off and the volume has been increased.

		- [x] ii. The tv details when the tv is on and the volume has been increased.

		- [x] iii. The tv details when the tv is on, muted, and the volume has been increased.

		- [x] iv. The tv details when the tv is on and one has increased the volume past the maximum value.

	- [x] g. volume_down:

		- [x] i. The tv details when the tv is off and the volume has been decreased.

		- [x] ii. The tv details when the tv is on and the volume has been decreased (increase the volume to the maximum before decreasing to see the decreasing effect).

		- [x] iii. The tv details when the tv is on, muted, and the volume has been decreased.

		- [x] iv. The tv details when the tv is on and one has decreased the volume past the minimum value.

## **FEEDBACK**

[x] 16. television.py 

	[x] a. init 

		[x] i. Missing type hinting (should return None) 

	[x] b. power 

		[x] i. Missing type hinting (should return None) 

		[x] ii. Incorrect docstrings (need only function description – don’t include param or return) 

	[x] c. mute 

		[x] i. Logic error in method (should only mute if tv is on) 

		[x] ii. Missing type hinting (should return None) 

		[x] iii. Incorrect docstrings (need only function description – don’t include param or return) 

	[x] d. channel_up 

		[x] i. Missing type hinting (should return None) 

		[x] ii. Incorrect docstrings (need only function description – don’t include param or return) 

	[x] e. channel_down 

		[x] i. Missing type hinting (should return None) 

		[x] ii. Incorrect docstrings (need only function description – don’t include param or return) 

	[x] f. volume_up 

		[x] i. Missing type hinting (should return None) 

		[x] ii. Incorrect docstrings (need only function description – don’t include param or return) 

volume_down 

[x] -0.5pts: Missing type hinting (should return None) 

[x] -0.5pts: Incorrect docstrings (need only function description – don’t include param or return) 

str 

[x] -1pt: Logic error (output when volume is muted) 

[x] -1pt: Your output statements should follow the same format as the ones provided in the main.py file comments Advice: It’s better to use Television.MIN_CHANNEL rather than self.MIN_CHANNEL (refer to the discussion video minute 12:41 on the implication of using self vs the class name when it comes to class variables). 

test_television.py 

[x] -12pts: Use pytest library not unit test library (refer to the Testing notes and lecture. Lecture minute 33:18 to 43:20, Notes - slide 9 and 10) test_mute: 

[x] -1pt: Unit test fails 

test_volume_up: 

[x] -1pt: Unit test fails

	"C:/Program Files/JetBrains/PyCharm Community Edition 2023.3.2/plugins/python-ce/helpers/pycharm _jb_pytest_runner.py" --target test_television.py::TestTelevision 
	Testing started at 8:50 PM ...
	Launching pytest with arguments py test_television.py::TestTelevision --no-header --no-summary -q in C:	\PycharmProjects\csci1620_lab12

	============================= test session starts =============================
	collecting ... collected 20 items

	test_television.py::TestTelevision::test_pass_init PASSED                [  5%]
	test_television.py::TestTelevision::test_pass_power_on PASSED            [ 10%]
	test_television.py::TestTelevision::test_pass_power_off PASSED           [ 15%]
	test_television.py::TestTelevision::test_pass_mute_on PASSED             [ 20%]
	test_television.py::TestTelevision::test_pass_mute_off PASSED            [ 25%]
	test_television.py::TestTelevision::test_pass_mute_on_no_power PASSED    [ 30%]
	test_television.py::TestTelevision::test_pass_mute_off_no_power PASSED   [ 35%]
	test_television.py::TestTelevision::test_pass_channel_up_no_power PASSED [ 40%]
	test_television.py::TestTelevision::test_pass_channel_up PASSED          [ 45%]
	test_television.py::TestTelevision::test_pass_channel_up_max PASSED      [ 50%]
	test_television.py::TestTelevision::test_pass_channel_down_no_power PASSED [ 55%]
	test_television.py::TestTelevision::test_pass_channel_down_min PASSED    [ 60%]
	test_television.py::TestTelevision::test_pass_volume_up_no_power PASSED  [ 65%]
	test_television.py::TestTelevision::test_pass_volume_up PASSED           [ 70%]
	test_television.py::TestTelevision::test_pass_volume_up_mute PASSED      [ 75%]
	test_television.py::TestTelevision::test_pass_volume_up_max PASSED       [ 80%]
	test_television.py::TestTelevision::test_pass_volume_down_no_power PASSED [ 85%]
	test_television.py::TestTelevision::test_pass_volume_down PASSED         [ 90%]
	test_television.py::TestTelevision::test_pass_volume_down_mute PASSED    [ 95%]
	test_television.py::TestTelevision::test_pass_volume_down_min PASSED     [100%]

	============================= 20 passed in 0.05s ==============================

	Process finished with exit code 0
