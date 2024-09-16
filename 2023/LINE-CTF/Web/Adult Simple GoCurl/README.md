# Adult Simple GoCurl

## Description
Read the flag (/flag)

## Attachment
[adult-simple-gocurl_9fd03c47bfa6bb6d4687720836633c3d.tar.gz](https://github.com/n1mdacybersec/CTF-Write-Up-Collection/blob/main/2023/LINE-CTF/Web/Adult%20Simple%20GoCurl/Challenge/adult-simple-gocurl_9fd03c47bfa6bb6d4687720836633c3d.tar.gz)

## Solution
The source code of this challenge is pretty similar with [Baby Simple GoCurl](../Baby%20Simple%20GoCurl/README.md), but there's a difference of how the program check the GET method request for `/curl` path.

```go
if strings.Contains(reqUrl, "flag") || strings.Contains(reqUrl, "curl") || strings.Contains(reqUrl, "%") {
	c.JSON(http.StatusBadRequest, gin.H{"message": "Something wrong"})
		return
}
```

From the snippet of code, the request to the server will be checked if its contains `flag`, `curl` or `%`. But, in this program there's no condition to check the originating IP address must be `127.0.0.1`, so we can insert `http://127.0.0.1:8080/` directly to `url` parameter on `/curl` path.

To obtain the flag, I used `X-Forwarded-Prefix` header that can be modified to make the unintented request to exploit the server. I found about this from this [link](https://github.com/gin-gonic/gin/pull/3500).
Because the flag on this challenge are on `/flag` path that can only be accessed by the localhost, but by using the feature of `X-Forwarded-Prefix` header will change the redirect of the request and make its possible to us to see the content of `/flag`. The request that need to be sent to the server to obtain the flag is like this.


```
GET http://34.84.87.77:11001/curl/?url=http://127.0.0.1:8080//&header_key=X-Forwarded-Prefix&header_value=/flag
```

![Request using crafted X-Forwarded Prefix](./solved.png)

## Flag
`LINECTF{b80233bef0ecfa0741f0d91269e203d4}`
