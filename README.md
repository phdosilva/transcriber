Como usuário eu quero enviar uma entrevista para que esta seja transcrita.

Como usuário eu quero selecionar um vídeo de entrevista para ser enviada

https://www.youtube.com/watch?v=ntOYtLoRgEQ&ab_channel=PSenna

Subindo um servidor FasAPI num EC2:
https://www.youtube.com/watch?v=SgSnz7kW-Ko&ab_channel=pixegami

To kill a port proccess:
sudo kill -9 `sudo lsof -t -i:8001`

# Configuring ec2
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
Save this file.

https://docs.rackspace.com/support/how-to/limit-file-upload-size-in-nginx/#:~:text=Edit%20the%20upload%20file%20size%20value%201%20Edit,systemd%20systemctl%20restart%20nginx%20sysvinit%20service%20nginx%20restart
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
You problaby did something wrong in the step above 


# Initialyzing a Venv
ref: https://engineering.rappi.com/using-fastapi-to-deploy-machine-learning-models-cd5ed7219ea

```
$ pip install virtualenv
$ virtualenv venv
$ virtualenv -p path_to_python venv
$ source venv/bin/activate
```

to genereate requirements in your project
```
pip freeze > requirements.txt
```

to install all the requirements:
```
$ pip install -r requirements.txt
```

if your process is killed:
```
$ pip install -r requirements.txt --no-cache-dir
```

and to check:
```
$ pip freeze
```

to endup your venv:
```
deactivate
```

