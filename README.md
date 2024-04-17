## **LAB 12**

## **SUBMISSION INSTRUCTIONS**

- [ ] 0. Submit your GitHub repository link.

## **QUESTION**

- [ ] 1. Create a repository named python.

- [ ] 2. Within the repository, create a new Python file called television.py where you will write code for the Television class. This class should have the variables and methods below (don’t add any extra methods to the class):

	- [ ] a. Class variables (To be declared in the class, outside any methods):

		- [ ] i. MIN_VOLUME: This is meant to serve as a constant. Its default value should be 0.

		- [ ] ii. MAX_VOLUME: This is meant to serve as a constant. Its default value should be 2.

		- [ ] iii. MIN_CHANNEL: This is meant to serve as a constant. Its default value should be 0.

		- [ ] iv. MAX_CHANNEL: This is meant to serve as a constant. Its default value should be 3.

		* Where applicable, use these constant variable names rather than hard coding values in your class methods.

	- [ ] b. Instance variables (To be declared in the __ init __ method):

		- [ ] i. status: This should be treated as a Boolean variable whose initial value is False.

		- [ ] ii. muted: This should be treated as a Boolean variable whose initial value is False.

		- [ ] iii. volume: This should be treated as an integer variable whose initial value is the minimum volume.

		- [ ] iv. channel: This should be treated as an integer variable whose initial value is the minimum channel.

		* All the instance variables should be private.
      
	- [ ] c. Methods:

		- [ ] i. def__ init__(self): This should be used to set the default instance variables.

		- [ ] ii. def power(self): This should be used to turn the tv on and off by changing the value of the status variable.

		- [ ] iii. def mute(self): This should be used to mute and unmute the tv when it’s on by changing the value of the muted variable.

		- [ ] iv. def channel_up(self): This should be used to increase the tv channel value when the tv is on. If the tv is on the maximum channel and this method is called, it should set the tv channel to the minimum channel (just like a regular tv remote, when you reach the maximum channel and keep pressing the channel up button, you are taken back to the starting/minimum channel).

		- [ ] v. def channel_down(self): This should be used to decrease the tv channel value when the tv is on. If the tv is on the minimum channel and this method is called, it should set the tv channel to the maximum channel.

		- [ ] vi. def volume_up(self): This should be used to increase the tv volume when the tv is on. If the tv is on the maximum volume and this method is called, the volume should just remain at the maximum (just like a regular tv remote, when you reach the maximum volume and keep pressing the volume up button, nothing happens, it just remains on the maximum volume).

		- [ ] vii. def volume_down(self): This should be used to decrease the tv volume when the tv is on. If the tv is on the minimum volume and this method is called, the volume should just remain at the minimum.

			* Please note: If any of the volume methods were called when the tv was muted, that would automatically unmute the tv and adjust the tv volume accordingly.

		- [ ] viii. def__str__ (self): This should be used to send the values of the tv object in the format Power =[status], Channel =[channel], Volume =[volume]. The items placed in brackets would be holding the current values of those tv variables. Refer to the comments in main.py on what the output would look like.

- [ ] 3. Test if the code in the Television class works as expected by downloading main.py to the same location television.py is located and then run main.py. The output you get should correspond to that in the comments found in main.py. If you get different values, it means that you need to work on the logic of the methods in the Television class.

- [ ] 4. Commit only television.py to your Git repository’s main/master branch.

- [ ] 5. Push your repository to your GitHub account.

- [ ] 6. Create anew branch named test on your local Git repository (make sure it’s set as the checkout branch — meaning any new changes are going to be saved to it moving forward).

- [ ] 7. Add docstrings and type hinting to the methods in television.py.

- [ ] 8. Create anew python file called test_television.py. Write unit tests for the _init__, power, mute, channel_up, channel_down, volume_up, andvolume_down methods using the external pytest library (please follow the standards for naming unit test functions).

- [ ] 9. Commit the changes to your test branch (At this point the test branch should only contain television.py and test_television.py. Don’t add any extra files or folders — meaning if more files other than television.py and test_television.py appear at the time of committing, make sure to uncheck them that way they are not part of the files saved to your repository). 

- [ ] 10. Push the changes to your GitHub account repository.

- [ ] 11. Submit the link of your public remote repository.

## **Please note:**

- [ ] 12. Don’t merge the 2 branches (we need to check you followed the instructions).

- [ ] 13. Make sure any new changes to your code are pushed to the test branch.

- [ ] 14. Refer to the testing notes and lecture on how to work with the pytest library.

- [ ] 15. Things to test for in the various methods:

	- [ ] a. init:

		- [ ] i. The status, channel, and volume values.

		- [ ] ii. Since you don’t have getter methods, you can use the __str__ method to check the tv values.

	- [ ] b. power:

		- [ ] i. The tv details when the tv is on.

		- [ ] ii. The tv details when the tv is off.

	- [ ] c. mute:

		- [ ] i. The tv details when the tv is on, volume increased once, and then tv muted.

		- [ ] ii. The tv details when the tv is on and unmuted.

		- [ ] iii. The tv details when the tv is off and muted.

		- [ ] iv. The tv details when the tv is off and unmuted.

	- [ ] d. channel_up:

		- [ ] i. The tv details when the tv is off and the channel has been increased.

		- [ ] ii. The tv details when the tv is on and the channel has been increased.

		- [ ] iii. The tv details when the tv is on and one has increased the channel past the maximum value.

	- [ ] e. channel_down:

		- [ ] i. The tv details when the tv is off and the channel has been decreased.

		- [ ] ii. The tv details when the tv is on and one has decreased the channel past the minimum value.

	- [ ] f. volume_up:

		- [ ] i. The tv details when the tv is off and the volume has been increased.

		- [ ] ii. The tv details when the tv is on and the volume has been increased.

		- [ ] iii. The tv details when the tv is on, muted, and the volume has been increased.

		- [ ] iv. The tv details when the tv is on and one has increased the volume past the maximum value.

	- [ ] g. volume_down:

		- [ ] i. The tv details when the tv is off and the volume has been decreased.

		- [ ] ii. The tv details when the tv is on and the volume has been decreased (increase the volume to the maximum before decreasing to see the decreasing effect).

		- [ ] iii. The tv details when the tv is on, muted, and the volume has been decreased.

		- [ ] iv. The tv details when the tv is on and one has decreased the volume past the minimum value.

* The GitHub repository link can be found here:

    Go to file | Add file | **<> Code**

    Local | Codespaces (New)

    Clone | (?)

    HTTPS | SSH | GitHub CLI

    **https://github.com/username/python.git**

    Use Git or checkout with SVN using the web URL

    Open with GitHub Desktop