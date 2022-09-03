# `httpfs`

TODO

## Usage

Example:

```
$ httpfs https://archive.org/download/league-of-legends-rads-patch-system-2010-2019{/RADS_LZX_Split{a..d}{a..z},-part-2/RADS_LZX_Split{e..h}{a..z},-part-3/RADS_LZX_Split{i{a..z},j{a..j}}}
Got 244 parts.
https://archive.org/download/league-of-legends-rads-patch-system-2010-2019/RADS_LZX_Splitaa 10.0G
...
https://archive.org/download/league-of-legends-rads-patch-system-2010-2019-part-3/RADS_LZX_Splitjj 2.8G
/tmp/tmpm4e040tx
```

In another terminal:

```
$ ls -lh /tmp/tmpm4e040tx
total 2.4T
-r--r--r-- 0 root root 2.4T Jan  1  1970 RADS_LZX_Split

$ wimmount /tmp/tmpm4e040tx/RADS_LZX_Split 14 /mnt/RADS-live

$ ls -l /mnt/RADS-live
total 0
drwxrwxrwx 1 vladimir vladimir 0 Mar 17  2021 live

$ ls -l /mnt/RADS-live/live/projects/league_client/releases/0.0.0.240/files
total 57386
-rwxrwxrwx 1 vladimir vladimir   198248 Mar 10  2020 BugSplatRc.dll
-rwxrwxrwx 1 vladimir vladimir   713320 Mar 10  2020 chrome_elf.dll
-rwxrwxrwx 1 vladimir vladimir  1237608 Mar 10  2020 ffmpeg.dll
-rwxrwxrwx 1 vladimir vladimir    24680 Mar 10  2020 jpatch.exe
-rwxrwxrwx 1 vladimir vladimir 23552616 Mar 10  2020 LeagueClient.exe
-rwxrwxrwx 1 vladimir vladimir  3538536 Mar 10  2020 LeagueClientUx.exe
-rwxrwxrwx 1 vladimir vladimir   812136 Mar 10  2020 LeagueClientUxRender.exe
-rwxrwxrwx 1 vladimir vladimir 93511784 Jul 30  2020 libcef.dll
-rwxrwxrwx 1 vladimir vladimir   117864 Mar 10  2020 libEGL.dll
-rwxrwxrwx 1 vladimir vladimir  4730984 Mar 10  2020 libGLESv2.dll
-rwxrwxrwx 1 vladimir vladimir  2433536 Mar 10  2020 rc-win.uni

$ head -c 128 /mnt/RADS-live/live/projects/league_client/releases/0.0.0.240/files/LeagueClient.exe | xxd
00000000: 4d5a 9000 0300 0000 0400 0000 ffff 0000  MZ..............
00000010: b800 0000 0000 0000 4000 0000 0000 0000  ........@.......
00000020: 0000 0000 0000 0000 0000 0000 0000 0000  ................
00000030: 0000 0000 0000 0000 0000 0000 b001 0000  ................
00000040: 0e1f ba0e 00b4 09cd 21b8 014c cd21 5468  ........!..L.!Th
00000050: 6973 2070 726f 6772 616d 2063 616e 6e6f  is program canno
00000060: 7420 6265 2072 756e 2069 6e20 444f 5320  t be run in DOS 
00000070: 6d6f 6465 2e0d 0d0a 2400 0000 0000 0000  mode....$.......
```

## Install

```
pip3 install httpfs-py
```
