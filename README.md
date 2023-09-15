# EC2
## First start EC2
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
### Referências

FastApi - Respondendo com HTML: https://www.youtube.com/watch?v=ntOYtLoRgEQ&ab_channel=PSenna

[Subindo um servidor FasAPI num EC2](https://www.youtube.com/watch?v=SgSnz7kW-Ko&ab_channel=pixegami)

[Using FastAPI to deploy Machine Learning models](https://engineering.rappi.com/using-fastapi-to-deploy-machine-learning-models-cd5ed7219ea)

[Why and How to make a Requirements.txt](https://boscacci.medium.com/why-and-how-to-make-a-requirements-txt-f329c685181e)

[Limit File Upload Size in NGINX](https://docs.rackspace.com/support/how-to/limit-file-upload-size-in-nginx/#:~:text=Edit%20the%20upload%20file%20size%20value%201%20Edit,systemd%20systemctl%20restart%20nginx%20sysvinit%20service%20nginx%20restart)

[Build an AI-driven SaaS Application: FULLSTACK Tutorial with Python, React, and AWS](https://www.youtube.com/watch?v=yxyyYMWu1ZA&ab_channel=pixegami)

# Deploy on GCP

https://datatonic.com/insights/deploying-machine-learning-models-google-cloud/

[Deploying models in Vertex AI](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/custom/SDK_Custom_Container_Prediction.ipynb)
[What is vertex AI?](https://geekflare.com/google-clouds-vertex-ai/)

#### Other references:

https://towardsdatascience.com/deploy-your-ml-model-as-a-web-service-in-minutes-using-gcps-cloud-run-ee9d433d8787

https://medium.datadriveninvestor.com/deploy-machine-learning-model-in-google-cloud-using-cloud-run-6ced8ba52aac

https://www.amplemarket.com/blog/how-to-deploy-machine-learning-microservice-to-google-cloud-run

https://www.youtube.com/watch?v=vieoHqt7pxo

[Deploy your own “ChatGPT”](https://medium.com/@giacomo.vianello/deploy-your-own-chatgpt-c012e762f6c0)

https://www.google.com/search?q=how+to+deploy+fastapi+in+vertex+ai&oq=how+to+deploy+fastapi+in+vertex+ai&aqs=edge..69i64j69i57.923j0j9&sourceid=chrome&ie=UTF-8

[Serving machine learning models with FastAPI: It’s not all about speed](https://www.amplemarket.com/blog/serving-machine-learning-models-with-fastapi)

[FastAPI documentation about container](https://fastapi.tiangolo.com/deployment/docker/)

# References to further implementations

https://stackoverflow.com/questions/73442335/how-to-upload-a-large-file-%E2%89%A53gb-to-fastapi-backend

https://stackoverflow.com/questions/63169865/how-to-do-multiprocessing-in-fastapi



# Hardware Requirements

As we saw above, Whisper is fairly easy to install. However it requires advanced hardware. A GPU is recommended if you want to use the large version of the model.

If you use the whisper Python lib (see above) you will need around 10GB of RAM and 11GB of VRAM. It means that in practice you will need a 16GB GPU at least. It could be a NVIDIA Tesla T4 for example, or an NVIDIA A10.

On a Tesla T4, you will transcribe 30 seconds of audio in around 6 seconds.
Performance Considerations

If you want to improve the default performance mentioned above, here are several strategies you can explore:

    • Use a higher end GPU. For example you will get a better response time with GPUs using the Ampere platform like A10, A40, or A100.
    • Work on batch inference in order to improve the throughput
    • Leverage XLA compilation with Tensorflow or Jax
    • Export the model to ONNX or TensorRT, and then serve it through the NVIDIA Triton Inference Server
