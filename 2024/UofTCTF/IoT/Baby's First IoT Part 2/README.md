# Baby's First IoT Part 2

## Description
See introduction for complete context.

- Part 2 - What company makes the processor for this device? https://fccid.io/Q87-WRT54GV81/Internal-Photos/Internal-Photos-861588. Submit the answer to port 6318.

## Solution
From the image provided, it is obvious that the company that makes the processor for the device is Broadcom

![Broadcom Processor of Linksys Wireless-G Broadband Router](./image1.png)

```shell
printf 'Broadcom\n\0' | nc 35.225.17.48 6318
```

## Flag
`{Processor_Recon}`
