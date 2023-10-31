# Super Admin

## Description
Comfort food.

Author: smarty

https://bluehens-web-cookies.chals.io/ 

## Description
This is the user interface for this challenge would looks like.

![Web for challenge](./1.png)

If we checked the cookies for this challenge, we will get `creds` cookies.
This cookies is called JSON Web Token (JWT) and this is authentication cookies.

![creds cookies](./2.png)

We can check the header (contains cryptography algorithm and token type), payload (data), and signature of the `creds` cookies using this [link](https://jwt.io/)

![Decoded value of JWT](./3.png)

From the image above, we know that JWT is encoded using base64 and there's `.` as separator for header, payload, and signature. 
From that image the cryptography algorithm is using HMAC SHA256, the role is `user` and the `iat` value is a timestamp when this JWT token were created.
Even though it's encoded using base64 and we can change the value of these base64 encoded data, but there's signature that check the validity of this JWT.
But it doesn't mean we can't change the value of these base64 encoded data, there's some attack for JWT token forgery.

If we look again for cryptography algorithm for this JWT token, it's use HMAC SHA256 which is algorithm for authentication of hash-message using SHA256.
Since it's using hashing the data can't be decrypted again, the possible attack against hashing is brute-force, dictionary attack, or rainbow table.
In this challenge, I use the [jwt_tool](https://github.com/ticarpi/jwt_tool) to crack the key for signature using dictionary attack and altering the value.
To crack the key for signature using dictionary attack, run this command.

```
python3 jwt_tool.py -C -d /usr/share/wordlists/rockyou.txt eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImlhdCI6MTY5ODc3MTE2N30.nssbt6IpQUjtPQE3gh3C63mU9MOK-C_kR3gYDV6q-9g
```

![Cracked key using jwt_tool](./4.png)

Using `jwt_tool` we got the key or secret to generate the signature which is `password1`.
To alter the value of JWT run this command

```
python3 jwt_tool.py -T -S hs256 -p "password1" eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoidXNlciIsImlhdCI6MTY5ODc3MTE2N30.nssbt6IpQUjtPQE3gh3C63mU9MOK-C_kR3gYDV6q-9g
```

For this menu, choose 0

![Continue to next step](./5.png)

For the next step we will change the value of role from `user` to `admin`. Choose 1 to edit the value of role and insert `admin` as the new role.

![Choose 1 to change the value of role](./6.png)

After that, we need to update the timestamp, which is the `iat` value. Choose 5 to update timestamp and then choose 1 to update the timestamp to current time.

![Choose 5 and then 1 to change the timestamp to current time](./7.png)

After you succesfully change the value, then choose 0.
You will get the altered version of the JWT token, copy paste that token and change the value of `creds` cookies.

![Altered version of JWT](./8.png)

Click the Go to profile button after changing the value of `creds` token to get the flag.

![Flag](./flag.png)

## Flag
`UDCTF{k33p_17_51mp13_57up1d_15_4_l1e}`

