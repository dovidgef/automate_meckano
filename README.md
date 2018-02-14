## Automate Meckano Checkin & Task Switching
#### General Setup
* `git clone https://github.com/dovidgef/automate_meckano.git`
* `pip install -r requirements.txt`
* In meckano.json replace values with your own username, password and task values.

##### Ubuntu Setup
* Give script full permissions `sudo chmod 777 automate_meckano.py`
* Customize checkin.desktop and checkout.desktop with correct path to script on your system
* Copy files to desktop

#### Windows Setup
* Copy Login To Meckano.lnk and Logout From Meckano.lnk to desktop
* Right click on icons > Click properties
* Customize target to correct path for your system

#### Instructions
* Run `python automate_meckano.py` to checkin and switch to default Project/Task(Set in meckano.json)
* Run `python automate_meckano.py logout` to checkout from Meckano and from Project/Task
* Run `python automate_meckano.py TaskName` to switch to different Project/Task