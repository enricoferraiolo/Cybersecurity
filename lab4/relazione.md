# Detect the intruder

> It has been detected that an intruder has visited a webpage with an html extension. Analyze the traffic and find the flag, that has this format CCIT{flag} from the s3cret.pcapng file.

We used Wireshark to analyze the traffic in the s3cret.pcapng file. We first filtered the packets with a simple filter (http contains "CCIT"), not finding anything. 

We then proceeded to search for any http packet that contains ".http" in the URI. We found a packet that contained the following information:

```
GET /it/sedi/bologna/informazioni.html HTTP/1.1
```

We then followed the HTTP stream to find the corresponding response, revealing the flag:

```
Frame 8041: 537 bytes on wire (4296 bits), 537 bytes captured (4296 bits) on interface eth0, id 0
Ethernet II, Src: 52:54:00:12:35:02 (52:54:00:12:35:02), Dst: PCSSystemtec_bc:84:f5 (08:00:27:bc:84:f5)
Internet Protocol Version 4, Src: 10.0.2.3, Dst: 10.0.2.15
Transmission Control Protocol, Src Port: 80, Dst Port: 46780, Seq: 1, Ack: 417, Len: 483
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
        Response Version: HTTP/1.1
        Status Code: 200
        [Status Code Description: OK]
        Response Phrase: OK
    Date: Wed, 01 May 2024 18:09:06 GMT\r\n
    Server: Apache/2.4.59 (Ubuntu)\r\n
    Last-Modified: Wed, 01 May 2024 18:08:12 GMT\r\n
    ETag: "90-617685eabe3a8-gzip"\r\n
    Accept-Ranges: bytes\r\n
    Vary: Accept-Encoding\r\n
    Content-Encoding: gzip\r\n
    Content-Length: 147\r\n
        [Content length: 147]
    Keep-Alive: timeout=5, max=100\r\n
    Connection: Keep-Alive\r\n
    Content-Type: text/html\r\n
    \r\n
    [HTTP response 1/1]
    [Time since request: 0.000494362 seconds]
    [Request in frame: 8039]
    [Request URI: http://10.0.2.3/it/sedi/bologna/informazioni.html]
    Content-encoded entity body (gzip): 147 bytes -> 144 bytes
    File Data: 144 bytes
Line-based text data: text/html (6 lines)
    Gentile utente,\n
    ti ringraziamo per aver visualizzato questa pagina.\n
    \n
    Il tuo codice è CCIT{asdkjhasd92837ekasjhdias8q98aksduh912}\n
    \n
    Buon lavoro.\n
```

So the flag is `asdkjhasd92837ekasjhdias8q98aksduh912`.

# Web vulnerability