# For

# Flag: picoCTF{h4un71ng_p457_5113beab}

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download compressed disk image


sudo losetup -f -P disk.flag.img

fdisk -l disk.flag.img  
Disk disk.flag.img: 400 MiB, 419430400 bytes, 819200 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0xb11a86e3

Device         Boot  Start    End Sectors  Size Id Type
disk.flag.img1 *      2048 206847  204800  100M 83 Linux
disk.flag.img2      206848 411647  204800  100M 82 Linux swap / Solaris
disk.flag.img3      411648 819199  407552  199M 83 Linux


sudo ls -lartR . | grep flag
-rw-r--r--  1 root root   64 Oct  7 05:32 flag.txt.enc

sudo find . -name flag.txt.enc -exec ls -lart {} \;
-rw-r--r-- 1 root root 64 Oct  7 05:32 ./root/flag.txt.enc

sudo cat ./root/.ash_history
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt

openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
cat flag.txt
picoCTF{h4un71ng_p457_5113beab}