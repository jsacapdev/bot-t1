#

[![Dependabot Updates](https://github.com/jsacapdev/ccxt/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/jsacapdev/ccxt/actions/workflows/dependabot/dependabot-updates)

[![Python CI](https://github.com/jsacapdev/ccxt/actions/workflows/ci.yml/badge.svg)](https://github.com/jsacapdev/ccxt/actions/workflows/ci.yml)

``` bash
conda

conda create --name bot-t1 python=3.13

conda activate bot-t1

pip install -r requirements.txt
```

``` bash
docker build -t bot-t1 .

docker run -d bot-t1

docker run -d -e BINANCE_API_KEY="your_api_key" -e BINANCE_SECRET_KEY="your_secret_key" bot-t1

docker logs -f 
docker logs -t 
```
