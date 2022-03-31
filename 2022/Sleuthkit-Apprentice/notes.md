# For

# Flag: picoCTF{by73_5urf3r_adac6cb4}

Download this disk image and find the flag. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

    Download compressed disk image


fdisk -l disk.flag.img
Disk disk.flag.img: 300 MiB, 314572800 bytes, 614400 sectors
Units: sectors of 1 * 512 = 512 bytes                  
Sector size (logical/physical): 512 bytes / 512 bytes  
I/O size (minimum/optimal): 512 bytes / 512 bytes       
Disklabel type: dos                                    
Disk identifier: 0x7389e82d                           
                                                           
Device         Boot  Start    End Sectors  Size Id Type
disk.flag.img1 *      2048 206847  204800  100M 83 Linux                                                              
disk.flag.img2      206848 360447  153600   75M 82 Linux swap / Solaris
disk.flag.img3      360448 614399  253952  124M 83 Linux


sudo losetup -f disk.flag.img

ll /dev/loop*       
brw-rw---- 1 root disk   7,   0 Mar 16 21:18 /dev/loop0
brw-rw---- 1 root disk 259,   0 Mar 16 21:18 /dev/loop0p1
brw-rw---- 1 root disk 259,   1 Mar 16 21:18 /dev/loop0p2
brw-rw---- 1 root disk 259,   2 Mar 16 21:18 /dev/loop0p3

sudo mount /dev/loop0p3 /mnt/apprentice
ll /mnt/apprentice                     
total 39
drwxr-xr-x  2 root root  3072 Sep 30 04:06 bin
drwxr-xr-x  2 root root  1024 Sep 30 01:57 boot
drwxr-xr-x  2 root root  1024 Sep 30 01:57 dev
drwxr-xr-x 27 root root  3072 Sep 30 04:06 etc
drwxr-xr-x  2 root root  1024 Sep 30 01:57 home
drwxr-xr-x  9 root root  1024 Sep 30 01:57 lib
drwx------  2 root root 12288 Sep 30 01:57 lost+found
drwxr-xr-x  5 root root  1024 Sep 30 01:57 media
drwxr-xr-x  2 root root  1024 Sep 30 01:57 mnt
drwxr-xr-x  2 root root  1024 Sep 30 01:57 opt
drwxr-xr-x  2 root root  1024 Sep 30 01:57 proc
drwx------  3 root root  1024 Sep 30 04:07 root
drwxr-xr-x  2 root root  1024 Sep 30 01:57 run
drwxr-xr-x  2 root root  5120 Sep 30 01:57 sbin
drwxr-xr-x  2 root root  1024 Sep 30 01:57 srv
drwxr-xr-x  2 root root  1024 Sep 30 04:06 swap
drwxr-xr-x  2 root root  1024 Sep 30 01:57 sys
drwxrwxrwt  4 root root  1024 Sep 30 04:06 tmp
drwxr-xr-x  8 root root  1024 Sep 30 01:57 usr
drwxr-xr-x 11 root root  1024 Sep 30 04:06 var

sudo ls -lartR | grep flag
-rw-r--r-- 1 root root   60 Sep 30 04:08 flag.uni.txt

sudo find . -name flag.uni.txt -exec cat {} \; 
picoCTF{by73_5urf3r_adac6cb4}