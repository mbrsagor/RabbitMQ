# RabbitMQ
> RabbitMQ is the most widely deployed open source message broker.

###### You have to must install below in your system.

### Prerequisites
- Python
- Django
- RabbitMQ-server

#### Setup:

The following steps will walk you thru installation on a Mac. I think linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed django apps on Windows, you should have little problem getting up and running.

```bash
git clone https://github.com/mbrsagor/RabbitMQ.git
cd RabbitMQ
virtualenv venv --python=python3.8
pip install -r requirements.txt
```

###### Then create ``.env`` file and paste code from `sample.env` file and add validate information.

-------------------------------------------
```bash
|--> .sample.env
|--> .env
```

#### Run:
```bash
./manage.py makemigrations && manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

##### Run RabbitMQ:
```
rabbitmq-server start
celery -A RabbitMQ worker -l info
```
