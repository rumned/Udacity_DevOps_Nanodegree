## Docker commands used to build the application
docker built -t techtrends

## Docker commands used to run the application
docker run -d -p 7111:3111 techtrends


## Docker commands used to get the application logs
docker logs e609bca5a868

## Logs from the container running the TechTrends application
* Serving Flask app 'app' (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
20:11:38,893 werkzeug INFO  * Running on http://192.168.1.8:3111/ (Press CTRL+C to quit)
20:11:49,480 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:49] "GET / HTTP/1.1" 200 -
20:11:49,622 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:49] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:11:49,704 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:49] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
20:11:51,263 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:51] "GET /create HTTP/1.1" 200 -
20:11:51,276 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:51] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:11:58,638 root DEBUG Article "testingpost" created!
20:11:58,638 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:58] "[32mPOST /create HTTP/1.1[0m" 302 -
20:11:58,643 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:58] "GET / HTTP/1.1" 200 -
20:11:58,885 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:11:58] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:01,45 root DEBUG Article "testingpost" retrieved!
20:12:01,47 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:01] "GET /9 HTTP/1.1" 200 -
20:12:01,59 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:01] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:02,771 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:02] "GET / HTTP/1.1" 200 -
20:12:03,68 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:03] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:04,264 root DEBUG Article "2020 CNCF Annual Report" retrieved!
20:12:04,265 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:04] "GET /1 HTTP/1.1" 200 -
20:12:04,280 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:04] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:05,884 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:05] "GET / HTTP/1.1" 200 -
20:12:06,184 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:06] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:07,69 root DEBUG Article "KubeCon + CloudNativeCon 2021" retrieved!
20:12:07,70 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:07] "GET /2 HTTP/1.1" 200 -
20:12:07,82 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:07] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:12:07,648 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:07] "GET / HTTP/1.1" 200 -
20:12:07,948 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:12:07] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -
20:13:53,499 root DEBUG About page rendered!
20:13:53,501 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:13:53] "GET /about HTTP/1.1" 200 -
20:13:53,513 werkzeug INFO 127.0.0.1 - - [28/Aug/2023 20:13:53] "[36mGET /static/css/main.css HTTP/1.1[0m" 304 -