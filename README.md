## Sentiment Analysis app is [deployed with wsgi server and hosted behind nginx on port 80](http://54.164.1.34/)
## Install the requirements using 
```
pip3 install -r requirements.py
```
## How this app works?
- The app takes a sentence as input
- The app uses pre trained vaderSentiment model and computes the cosine distance of each words to compute the sentiment.
- It then returns the results in pie chart format. 

## This is the input
<p align='center'>
<img src='../master/input.png'>
</p>

## This is the output
<p align='center'>
<img src='../master/output.png'>
</p>

## Steps to deploy Django app from GitHub to AWS EC2 with wsgi server and hosted behind nginx on port 80

```cd .. 
python manage.py collectstatic
gunicorn --bind 0.0.0.0:8000 sentiment.wsgi:application
```

```
sudo vim /etc/systemd/system/gunicorn.service
```
## Edit the gunicorn.service as follows
```
[Unit]
Description=gunicorn daemon
After=network.target
[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/sentiment
ExecStart=/home/ubuntu/sentiment/venv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/sentiment/sentimentapp.sock sentiment.wsgi:application
[Install]
WantedBy=multi-user.target
```
```
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo vim /etc/nginx/sites-available/sentiment
```
## Edit site config as follows
```
server {
  listen 80;
  server_name 54.221.151.161;
  location = /favicon.ico { access_log off; log_not_found off; }
  location /static/ {
      root /home/ubuntu/sentiment;
  }
  location / {
      include proxy_params;
      proxy_pass http://unix:/home/ubuntu/sentiment/sentimentapp.sock;
}
}
```

```
sudo ln -s /etc/nginx/sites-available/sentiment /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
```
