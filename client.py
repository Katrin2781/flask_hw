import requests

# response = requests.post(
#     "http://127.0.0.1:5000/adverts",
#     json={
#         "title_advert": "title 1",
#         "description": "description 1",
#         "user": "user 1",
#     },
# )


# response = requests.get(
#     "http://127.0.0.1:5000/adverts/1",
#
# )
# response = requests.post(
#     "http://127.0.0.1:5000/adverts",
#     json={
#         "title_advert": "title 1",
#         "description": "description 1",
#         "user": "user 1",
#     },
# )

# response = requests.post(
#     "http://127.0.0.1:5000/adverts",
#     json={
#         "title_advert": "title 2",
#         "description": "description 2",
#         "user": "user 2",
#     },
# )

# response = requests.get(
#     "http://127.0.0.1:5000/adverts/3",
#
# )

# response = requests.patch(
#     "http://127.0.0.1:5000/adverts/3",
#     json={
#         "title_advert": "title 3",
#         "description": "description 3",
#         "user": "user 3",
#     },
# )

# response = requests.get(
#     "http://127.0.0.1:5000/adverts/3",
#
# )

response = requests.delete(
    "http://127.0.0.1:5000/adverts/3",

)

response = requests.get(
    "http://127.0.0.1:5000/adverts/3",

)

print(response.status_code)
print(response.json())
