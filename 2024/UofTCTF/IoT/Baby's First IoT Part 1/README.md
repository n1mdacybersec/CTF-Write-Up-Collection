# Baby's First IoT Part 1

## Description
See introduction for complete context.

- Part 1 - Here is an FCC ID, Q87-WRT54GV81, what is the frequency in MHz for Channel 6 for that device? Submit the answer to port 3895.

## Solution
The FCC ID of Q87-WRT54GV81 is FCC ID from Linksys Wireless-G Broadband Router. The search results are from https://fccid.io/.

From the search results, there are [supporting documents](https://fcc.report/FCC-ID/Q87-WRT54GV81) about the device.
We can find out about the frequency usage for Channel 6 in the [RF Exposure Info](https://fcc.report/FCC-ID/Q87-WRT54GV81/861595) and [Test Report](https://fcc.report/FCC-ID/Q87-WRT54GV81/861591) documents.

The correct answer for what is the frequency for Channel 6 for Linksys Wireless-G Broadband Router is 2437 MHz.
When I tried to insert the answer to the netcat connection it's always failed and will return a message "Access denied". So to send the answer to netcat connection we can use this command.

```shell
printf '2437\n\0' | nc 35.225.17.48 3895
```

## Flag
`{FCC_ID_Recon}`

