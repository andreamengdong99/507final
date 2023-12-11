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

dict = {}
found = False  # 新增标志变量

while not found:
    input1 = input("Choose a price range (or type 'exit' to quit): ")
    if input1.lower() == 'exit':
        break
    price_found = False
    for pricenode in root.children:
        if pricenode.param == input1:
            price_found = True
            input2 = input("Choose a transaction type: ")
            transaction_found = False
            for transactionnode in pricenode.children:
                if transactionnode.param == input2:
                    transaction_found = True
                    input3 = input("Choose a cuisine: ")
                    category_found = False
                    for categoriesnode in transactionnode.children:
                        if categoriesnode.param == input3:
                            category_found = True
                            if categoriesnode.children:
                                for node in categoriesnode.children:
                                    dict[node.param] = [node.lat, node.lng]
                                    found = True
                                    break
                                if found:  # 如果找到了，立即退出所有循环
                                    break
                            else:
                                print("No restaurant found. Please try again")
                    if not category_found and not found:
                        print("No such cuisine found. Please try again")
                        break  # 如果未找到菜系，则退出交易类型循环
                if found:
                    break  # 如果找到了，退出交易类型循环
            if not transaction_found and not found:
                print("No such transaction type found. Please try again")
                break  # 如果未找到交易类型，则退出价格范围循环
        if found:
            break  # 如果找到了，退出价格范围循环
    if not price_found and not found:
        print("No such price range found. Please try again")




print(dict)



place_id = input("Please refer to this page (https://developers.google.com/maps/documentation/places/web-service/place-id?hl=en) to find and put in your place id: ")
url2 = f"https://maps.googleapis.com/maps/api/geocode/json?place_idp={place_id}&key=AIzaSyBzTrJWeimUYu32ysF5_gwsbvm1Bwp5nko"
response2 = requests.get(url2)
ans = response2.json()

min = 0
if ans["results"]:  # Check if results list is not empty
    lat = ans["results"][0]["geometry"]["location"]["lat"]
    lng = ans["results"][0]["geometry"]["location"]["lng"]

    for key in dict.keys():
        key_lat = dict[key][0]
        key_lng = dict[key][1]
        distance = (key_lat - lat) * (key_lat - lat) + (key_lng - lng) * (key_lng - lng)
        if distance < min:
            min = distance
            answer = key
    print(key)
else:
    print("No results found for the provided place ID.")








