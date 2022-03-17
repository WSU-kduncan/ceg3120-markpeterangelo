# Part 2
## 1. 
* At the top of `/etc/hosts` there is ip address and then the hostname it leads to. this allows/sets your system has a hostname that is in no way connected to the hostname of the ip you are connecting to, 
* while in the `.ssh/config` file you need to direct the key to it, and set hostname and users


## 2. 
* Use the private IP, username (ubuntu), and the private key called ceg3120-aws-vm.pem to ssh into the proxy.

 
```
ssh Web-Server-1

ssh Web-Server-2
```

## 3.
* google the config file and change it as you need for your proxy, and verify it with `haproxy -f /etc/haproxy/haproxy.cfg -c` and once its correct do `sudo systemctl restart haproxy` to have the proxy up and running

* /etc/haproxy/haproxy

* There were default config file, however I deleted all of them and replaced them with my own

* `sudo systemctl restart haproxy`

* https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/ https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/

* https://discourse.haproxy.org/t/question-about-restarting-the-service/4134

## 4.
* The files modified were /var/www/html/index.html was modified. i moved the 2 .html files to the default html diretory, 

* The configurations were set to default apache2.

* in `/var/www/html` ; They are stored because you need to store the index.html is the default for homepage.

* `sudo systemctl restart apache2`


![Server1](https://user-images.githubusercontent.com/70331126/158909006-c3817fa9-4a98-419d-b625-2bf3efb8c72b.png)

![Server2](https://user-images.githubusercontent.com/70331126/158909015-3e8c4a47-ae66-4190-aa84-e9395b54bce9.png)
