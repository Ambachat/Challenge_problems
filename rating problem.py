import requests

def getTopRatedFoodOutlets(city):
    BASE_URL = 'https://jsonmock.hackerrank.com/api/food_outlets'

    def get_data(url, params):
        response = requests.get(url, params=params)
        return response.json()

    page = 1
    highest_average_rating = 0.0
    top_outlets = []

    while True:
        params = {'city': city, 'page': page}
        data = get_data(BASE_URL, params)

        if 'data' not in data:
            break

        for outlet in data['data']:
            rating_data = outlet.get('rating', {})  # Get the rating data for the outlet
            average_rating = float(rating_data.get('average', 0.0))  # Get the average rating
            name = outlet['name']

            if average_rating > highest_average_rating:
                highest_average_rating = average_rating
                top_outlets = [name]
            elif average_rating == highest_average_rating:
                top_outlets.append(name)

        if data['total_pages'] <= page:
            break

        page += 1

    return top_outlets

city_name = "Denver"  # Replace with the desired city name
result = getTopRatedFoodOutlets(city_name)
print(result)
