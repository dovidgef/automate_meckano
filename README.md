## Automate Meckano Checkin & Task Switching
#### General Setup
* `git clone https://github.com/dovidgef/automate_meckano.git`
* `pip install -r requirements.txt`
* In meckano.json replace values with your own username, password and task values.

##### Ubuntu Setup
###### Desktop Shortcuts
* Customize checkin.desktop and checkout.desktop with correct path to script on your system
* Copy files to desktop
###### Command Line Shortcuts
* Add the following lines to end of your `~/.bashrc` file
```
alias login='~/PycharmProjects/automate_meckano/automate_meckano.py'
alias logout='~/PycharmProjects/automate_meckano/automate_meckano.py logout'
```
* Customize paths to script location on your system
* Run `source ~/.bashrc`
* In any terminal run `login` to checkin to Meckano and to select automatically your default task.
* Run `login Task_Name` to switch task
* Run `logout` to checkout from Mekano and exit from your task


#### Windows Setup
* Copy Login To Meckano.lnk and Logout From Meckano.lnk to desktop
* Right click on icons > Click properties
* Customize target to correct path for your system

##### Turn Off Hibernate
Turn off Hibernate so that the computer goes to sleep instead of hibernating on logout:
* Open cmd with administrator rights
* Run `powercfg.exe /h off`

#### Instructions
* Run `python automate_meckano.py` to checkin and switch to default Project/Task(Set in meckano.json)
* Run `python automate_meckano.py logout` to checkout from Meckano and from Project/Task
* Run `python automate_meckano.py TaskName` to switch to different Project/Task