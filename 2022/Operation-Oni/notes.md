# For

# Flag: picoCTF{k3y_5l3u7h_d6e19567}

Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download disk image
    Remote machine: ssh -i key_file -p 51609 ctf-player@saturn.picoctf.net


fdisk -l disk.img  
Disk disk.img: 230 MiB, 241172480 bytes, 471040 sectors
Units: sectors of 1 * 512 = 512 bytes                  
Sector size (logical/physical): 512 bytes / 512 bytes                                                                 
I/O size (minimum/optimal): 512 bytes / 512 bytes                                                                     
Disklabel type: dos                                       
Disk identifier: 0x0b0051d0                                                                                           
                                                           
Device     Boot  Start    End Sectors  Size Id Type   
disk.img1  *      2048 206847  204800  100M 83 Linux  
disk.img2       206848 471039  264192  129M 83 Linux

### The -P flag we used actually tells losetup to have the kernel scan the partition table, so we can skip along to mounting the partition we want.
sudo losetup -f -P disk.img

ll /dev/loop*               
brw-rw---- 1 root disk   7,   0 Mar 16 21:28 /dev/loop0
brw-rw---- 1 root disk   7,   1 Mar 16 21:28 /dev/loop1
brw-rw---- 1 root disk 259,   0 Mar 16 21:28 /dev/loop1p1
brw-rw---- 1 root disk 259,   1 Mar 16 21:28 /dev/loop1p2

sudo mount /dev/loop1p2 /mnt/oni

sudo cat root/.ssh/id_ed25519
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
QyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLAAAAJgxpYKDMaWC
gwAAAAtzc2gtZWQyNTUxOQAAACBgrXe4bKNhOzkCLWOmk4zDMimW9RVZngX51Y8h3BmKLA
AAAECItu0F8DIjWxTp+KeMDvX1lQwYtUvP2SfSVOfMOChxYGCtd7hso2E7OQItY6aTjMMy
KZb1FVmeBfnVjyHcGYosAAAADnJvb3RAbG9jYWxob3N0AQIDBAUGBw==
-----END OPENSSH PRIVATE KEY-----


sudo ssh -i id_ed25519  -p 61587 ctf-player@saturn.picoctf.net     
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1017-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.
Last login: Wed Mar 16 12:40:48 2022 from 127.0.0.1
ctf-player@challenge:~$ ls -la
total 4
drwxr-xr-x 1 ctf-player ctf-player 20 Mar 16 12:40 .
drwxr-xr-x 1 root       root       24 Mar 15 06:59 ..
drwx------ 2 ctf-player ctf-player 34 Mar 16 12:40 .cache
drwxr-xr-x 2 ctf-player ctf-player 29 Mar 15 06:59 .ssh
-rw-r--r-- 1 root       root       28 Mar 15 06:59 flag.txt
ctf-player@challenge:~$ cat flag.txt
picoCTF{k3y_5l3u7h_d6e19567}