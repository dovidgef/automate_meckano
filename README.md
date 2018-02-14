## Automate Meckano Checkin & Task Switching
#### General Setup
* `git clone https://github.com/dovidgef/automate_meckano.git`
* `pip install -r requirements.txt`

##### Ubuntu Setup
* Give script full permissions `sudo chmod 777 automate_meckano.py`
* Customize checkin.desktop and checkout.desktop with correct path to script
* Copy files to desktop and give them executable permissions
* Enjoy

#### Instructions
* Run `python automate_meckano.py` to checking and switch to default Project/Task(Set in meckano.json)
* Run `python automate_meckano.py logout` to checkout from Meckano and from Project/Task
* Run `python automate_meckano.py TaskName` to switch to different Project/Task