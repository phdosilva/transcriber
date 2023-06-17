### Referências

FastApi - Respondendo com HTML: https://www.youtube.com/watch?v=ntOYtLoRgEQ&ab_channel=PSenna

Subindo um servidor FasAPI num EC2:
https://www.youtube.com/watch?v=SgSnz7kW-Ko&ab_channel=pixegami

Using FastAPI to deploy Machine Learning models: https://engineering.rappi.com/using-fastapi-to-deploy-machine-learning-models-cd5ed7219ea

Why and How to make a Requirements.txt: https://boscacci.medium.com/why-and-how-to-make-a-requirements-txt-f329c685181e

Limit File Upload Size in NGINX: https://docs.rackspace.com/support/how-to/limit-file-upload-size-in-nginx/#:~:text=Edit%20the%20upload%20file%20size%20value%201%20Edit,systemd%20systemctl%20restart%20nginx%20sysvinit%20service%20nginx%20restart

Build an AI-driven SaaS Application: FULLSTACK Tutorial with Python, React, and AWS: https://www.youtube.com/watch?v=yxyyYMWu1ZA&ab_channel=pixegami

# First start EC2
```
sudo apt-get update 
```

```
sudo apt-get install -y python3-pip nginx
```

```
sudo vim /etc/nginx/sites-enabled/fastapi_nginx
```

```
server {
    listen 80;
    server_name <EC2_IP_ADRESS>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
Then, save the file.


Next, edit nginx max body size with:
```
vim /etc/nginx/nginx.conf
```
```
    http {
        ...
        client_max_body_size 100M;
    }
```

Restart the nginx server
```
sudo service nginx restart
```

If you see the following error:
```
Job for nginx.service failed because the control process exited with error code.
See "systemctl status nginx.service" and "journalctl -xeu nginx.service" for details.
```
You problaby did something wrong in nginx configurations 


# Setup a Virtual Environment to run Python
[ref](https://engineering.rappi.com/using-fastapi-to-deploy-machine-learning-models-cd5ed7219ea)

to get requirements in your project
```
pip freeze > requirements.txt
```

In EC2, do the setup:
```
pip install virtualenv
```

In project dir do:
```
virtualenv venv
virtualenv -p path_to_python venv
source venv/bin/activate
```

to install all the requirements:
```
$ pip install -r requirements.txt
```

if your process is killed, probably works:
```
$ pip install -r requirements.txt --no-cache-dir
```

and to check:
```
$ pip freeze
```

### If its needed

to endup your venv:
```
deactivate
```

To kill a port proccess:
```
sudo kill -9 `sudo lsof -t -i:8000`
```

# References to further implementations
https://stackoverflow.com/questions/73442335/how-to-upload-a-large-file-%E2%89%A53gb-to-fastapi-backend

