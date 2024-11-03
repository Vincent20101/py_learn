import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0)
with open("brand.txt", "r", encoding="utf-8") as f:
    brands = f.readlines()
for brand in brands:
    url = "https://www.guazi.com{}i7c-1/".format(brand)
    r.lpush("guazi:start_urls", url)
