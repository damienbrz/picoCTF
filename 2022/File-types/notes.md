# For

# Flag: picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_79b01c26}


Check the file type
```
file Flag.pdf
Flag.pdf: shell archive text
```
Running
```
bash Flag.pdf
# Create a `flag` file
file flag      
flag: current ar archive
ar x flag
file flag
flag: cpio archive
mv flag oldflag
# Had to rename it has cpio extract a file called flag
cpio -idv < oldflag
file flag
flag: bzip2 compressed data, block size = 900k
bzip2 -d flag
bzip2: Can't guess original name for flag -- using flag.out
file flag.out 
flag.out: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:39 2022, from Unix, original size modulo 2^32 328
mv flag.out flag.out.gz
file flag.out 
flag.out: lzip compressed data, version: 1
lunzip -d flag.out 
file flag.out.out 
flag.out.out: LZ4 compressed data (v1.4+)
mv flag.out.out flag.out.lz4 
lz4 -d flag.out.lz4         
Decoding file flag.out 
flag.out.lz4         : decoded 266 bytes
file flag.out    
flag.out: LZMA compressed data, non-streamed, size 254
mv flag.out flag.out.xz  
lzma -d flag.out.xz
file flag.out
flag.out: lzop compressed data - version 1.040, LZO1X-1, os: Unix\
mv flag.out flag.lzo   
lzop -d flag.lzo
file flag    
flag: lzip compressed data, version: 1
lzip -d flag
file flag.out 
flag.out: XZ compressed data, checksum CRC64
 mv flag.out flag.xz
 xz -d flag.xz
file flag   
flag: ASCII text
cat flag           
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37396230316332367d0a 

This a hex representatino of the flag
```
