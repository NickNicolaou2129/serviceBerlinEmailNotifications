# serviceBerlinEmailNotifications
Python script to automatically email you when a Berlin Anmeldung appointment becomes available.

PREREQUISITES:

•	You must have Firefox installed on your computer.

•	You must have a Python IDE installed on your computer; you then need to open the python script using the IDE. 

•	You must have Python 2.7 installed on your computer and used as an interpreter in the environment of your IDE.

•	You must have a Gmail address to send the notification emails from. With "Allow less secure apps" turned ON in the settings. Google "Turn on less secure apps in Gmail account".

•	You must download Geckodriver.exe on your computer.

INSTRUCTIONS:

After you have completed the above prerequisites, follow the instruction in the code comments.

•	Open your IDE, click “File”, “Open project”, then select the “ServiceBerlin” project.

•	Open the “ServiceBEMonitor.py” file within the project.

•	Install the necessary dependencies at the top of the code.

•	Enter the path of where you downloaded the Geckodriver.exe, my path is already there as an example [Line 8].

•	Enter your Gmail address that you created to send the emails from [Line 24].

•	Enter your email address that receives the emails [Line 25].

•	Enter your sender Gmail address again, then the password for it [Line 30].

•	Click “Run”, then “Run ServiceBEMonitor.py” to run the script. You must leave the code running with your computer left on.

•	A good tip, if the website stops your connection as it has detected a robot, close the browser, increase the wait time [Line 16] and use a VPN to change your IP address. Then try again.
