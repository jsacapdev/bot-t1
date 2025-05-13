#

|Pipeline|-|
|-|-|
|Evergreen|[![Dependabot Updates](https://github.com/jsacapdev/ccxt/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/jsacapdev/ccxt/actions/workflows/dependabot/dependabot-updates)|
|Build and Push Container|[![Python CI](https://github.com/jsacapdev/ccxt/actions/workflows/ci.yml/badge.svg)](https://github.com/jsacapdev/ccxt/actions/workflows/ci.yml)|

## Activate environment

``` bash
conda

conda create --name bot-t1 python=3.13

conda activate bot-t1

pip install -r requirements.txt
```

## Local container creation

``` bash
docker build -t bot-t1 .

docker run -d bot-t1

docker run -d -e BINANCE_API_KEY="your_api_key" -e BINANCE_SECRET_KEY="your_secret_key" bot-t1
```

## Remote container pull

``` bash
docker pull ghcr.io/jsacapdev/bot-t1:main

docker run -d -e BINANCE_API_KEY="your_api_key" -e BINANCE_SECRET_KEY="your_secret_key" ghcr.io/jsacapdev/bot-t1:main
```

## Logs

``` bash
docker logs -f 
docker logs -t 
```
