import os
from dotenv import load_dotenv
import requests

load_dotenv("example.env")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = os.environ.get("PIXELA_USER")
PIXELA_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}


def create_user():
    pixela_user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USER,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    create_user_response = requests.post(url=PIXELA_ENDPOINT, json=pixela_user_params)
    print(create_user_response.text)


# create_user()
def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs"

    reading_graphs_params = {
        "id": "graph1",
        "name": "Reader",
        "unit": "Pages",
        "type": "int",
        "color": "shibafu"
    }

    print(graph_endpoint)

    create_graph_response = requests.post(url=graph_endpoint,
                                          json=reading_graphs_params,
                                          headers=PIXELA_HEADERS)

    print(create_graph_response.text)


def add_pixel():
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/graph1"
    pixel_params = {
        "date": "20220102",
        "quantity": "8"
    }
    add_pixel_to_graph = requests.post(url=pixel_endpoint,
                                       json=pixel_params,
                                       headers=PIXELA_HEADERS)


# add_pixel()


def delete_pixel():
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/graph1/20220102"
    pixel_to_delete = requests.delete(url=pixel_endpoint,
                                      headers=PIXELA_HEADERS)


def update_pixel():
    pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USER}/graphs/graph1/20220102"
    pixel_params = {
        "quantity": "4"
    }

    pixel_to_delete = requests.put(url=pixel_endpoint,
                                   json=pixel_params,
                                   headers=PIXELA_HEADERS)


#  update_pixel()
delete_pixel()
