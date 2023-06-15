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