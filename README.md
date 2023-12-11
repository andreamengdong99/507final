# 507final
This project aims to look for a list of Ann Arbor restaurants based on the price, cuisine and transaction input, and sort out the nearest restaurant based on the place id input of the user.

price input: '$', '$$', '$$$', '$$$$'

cuisine input: 'Gluten-Free', 'Coffee & Tea', 'Ice Cream & Frozen Yogurt', 'Soup', 'Steakhouses', 'Music Venues', 'Wine Bars', 'Japanese', 'Tacos', 'Hot Dogs', 'Seafood Markets', 'Tapas/Small Plates', 'Spanish', 'Vietnamese', 'Delis', 'Sushi Bars', 'Food Trucks', 'Meat Shops', 'Middle Eastern', 'Burgers', 'Sandwiches', 'American', 'Venues & Event Spaces', 'Noodles', 'Breweries', 'Ramen', 'Barbeque', 'Chicken Wings', 'Asian Fusion', 'Italian', 'Vegan', 'Indian', 'Desserts', 'Halal', 'Mediterranean', 'Pubs', 'Waffles', 'Cuban', 'Mexican', 'Pizza', 'Wraps', 'Himalayan/Nepalese', 'Vegetarian', 'Brazilian', 'Bars', 'Cocktail Bars', 'Seafood', 'Jazz & Blues', 'Tapas Bars', 'Chinese', 'Korean', 'Hawaiian', 'New American', 'Breakfast & Brunch', 'Salad'

transaction input: 'delivery', 'pickup'

With your input, the program will return a list of restaurant names that meet your requirements. It will then ask you to put in your place ID (you can find your place ID by going to google map API: https://developers.google.com/maps/documentation/places/web-service/place-id?hl=en and put in your location)

With your place ID, the program will generate your exact location through the longitute and latitute of it, and sort out the nearest restaurant to you.

You can get the Yelp API key at https://www.yelp.com/developers/v3/manage_app
You can get the googme map API key at https://developers.google.com/maps/documentation/places/web-service/get-api-key?hl=en

packages: requests, json

