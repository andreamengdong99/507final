import requests
import json
url = "https://api.yelp.com/v3/businesses/search?location=Ann%20Arbor&term=restaurants&categories=&sort_by=best_match&limit=50"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer W8SD92yWmFjWB7XhnKiv4gHKCiO8P0ReAuuz068hD8K7BuRiZ_lTxzbui45as_Ih-21SySH2s-4zGPz3PD8JGwGb_Btv--zjlFecH7ak0-g3ivKKJfOS_SHe2PhUZXYx"
}

response = requests.get(url, headers=headers)
data = response.json()
restaurants_list = data["businesses"]


class Node:
    def __init__(self, param, lat = 0, lng = 0):
        self.param = param
        self.children = []
        self.lat = lat
        self.lng = lng

    def add_child(self, child):
        self.children.append(child)



root = Node("all restaurants")
prices = {"$", "$$", "$$$", "$$$$"}
cuisine = set()
transactions = {"delivery", "pickup"}

for r in restaurants_list:
    list = r["categories"]
    for dict in list:
        cuisine.add(dict["title"])

for p in prices:
    child1 = Node(p)
    root.add_child(child1)
    for t in transactions:
        child2 = Node(t)
        child1.add_child(child2)
        for c in cuisine:
            child3 = Node(c)
            child2.add_child(child3)


for r in restaurants_list:
    price = r.get("price", "")
    categories = [category["title"] for category in r.get("categories", [])]
    transactions = r.get("transactions", [])
    name = r["name"]
    lat = r["coordinates"]["latitude"]
    lon = r["coordinates"]["longitude"]
    for price_node in root.children:
        if price_node.param == price:
            for transaction_node in price_node.children:
                if transaction_node.param in transactions:
                    for categories_node in transaction_node.children:
                        if categories_node.param in categories:
                            newNode = Node(name)
                            newNode.lat = lat
                            newNode.lon = lon
                            categories_node.add_child(newNode)

with open('data.json', 'w') as file:
    json.dump(restaurants_list, file, indent=4)