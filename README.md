![Badge](https://img.shields.io/static/v1?label=Django&message=framework&color=blue&style=for-the-badge&logo=DJANGO)
![Badge](https://img.shields.io/static/v1?label=python&message=language&color=red&style=for-the-badge&logo=PYTHON)
![Badge](https://img.shields.io/static/v1?label=docker&message=virtualization&color=green&style=for-the-badge&logo=DOCKER)
![Badge](https://img.shields.io/static/v1?label=MIT&message=LICENSE&color=yellow&style=for-the-badge)


# Estágio Hoje

> Backend de template para as aplicações do projeto estágio hoje da diciplina PCS3553 - Laboratório de Engenharia de Software II

## 🚀 How to execute

- Run with docker:

```sh
chmod +x run.sh
./run.sh
```

- Run without docker:
```sh
chmod +x manage.py
python3 manage.py migrate
./manage.py runserver
```

Acess:
```
http://localhost:8000
```

## 📦 Dependencies

### 🐋 Docker Compose

```sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

To verify that the installation was successful, you can run:

```sh
docker-compose --version
```