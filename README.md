# Introduction

This project was developed as a complement to [The Complete Python Developer](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) course I've recently finished. This program takes a file of passwords and queries the pwned passwords API to see if they've been cracked and how many times, after which it prints the information on screen. Since I wanted to learn about jobs and schedulers on Linux I've implemented two different ways of scheduling this program via **systemd** and **cron**.

<br/>

# Requirements

*Python3*, *pip* and *requests* are required, for convenience a requirements.txt file is provided in the config folder, to use it run the following command:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/image-processing/master/images/install.png" alt="Download Instructions">
</p>

<br/>

# Usage

## cron

The simplest way, simply use ```crontab -e``` to edit the cron configurations and insert the following line: ```0 0 * * SUN```.

There is also a ```job.cron``` file inside the config folder that contains the cron string for convenience.

After saving the file the job will automatically run on the specified schedule, no extra configuration required.

<br/>
<br/>

## systemd

A bit more involved process, start by creating a new systemd service in ```/etc/systemd/system/password-checker.service``` with the following configuration, or use the appropriate file in the config folder:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/password-checker/master/images/password-checker-service.png" alt="Systemd Service">
</p>

Afterwards create another file but name it as a timer in ```/etc/systemd/system/password-checker.timer``` with the following configuration, or use the appropriate file as specified above:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/password-checker/master/images/password-checker-timer.png" alt="Systemd Timer">
</p>

Finally reload the daemon and start, enable and check your timer by running these commands:

<p align="center">
    <img width="640" src="https://raw.githubusercontent.com/dumiii/password-checker/master/images/systemd.png" alt="Systemd Timer">
</p>

The job is also configured to run at the time specified by the cronjob string, 

# Credits

[The Complete Python Developer](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/) for the script, [Pwned Passwords API](https://api.pwnedpasswords.com) for the cracked passwords information and credits for the awesome instruction images go to [Carbon](https://carbon.now.sh/).