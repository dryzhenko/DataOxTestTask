import dataclasses
import datetime

import requests
from bs4 import BeautifulSoup, Tag
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")


@dataclasses.dataclass
class Car:
    url: str
    title: str
    price_usd: int
    odometer: int
    username: str
    phone_number: int
    image_url: str
    image_count: int
    car_number: str
    car_vin: str
    datetime_found: datetime


def parse_single_car(car: Tag) -> Car:
    url = car.select_one(".m-link-ticket")["href"]
    title = car.select_one(".blue.bold").text.strip()
    price_usd = int(car.select_one("div.price-ticket")["data-main-price"])
    #скоріш за все так робити не правильно але я не придумав інакше(
    try:
        odometer = int(''.join(filter(str.isdigit, car.select_one("li.item-char.js-race").text.split("тис")[0]))) * 1000
    except Exception:
        odometer = 0
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    username_tag = soup.select_one("div.seller_info_name")
    username = username_tag.get_text(strip=True) if username_tag else None

    #phone number(((

    image_tag = soup.select_one(".carousel-inner img")
    image_url = image_tag["src"] if image_tag else None

    all_images = soup.select(".carousel-inner img")
    image_count = len(all_images) - 1

    vin_tag = soup.select_one("span.label-vin")
    car_vin = vin_tag.get_text(strip=True) if vin_tag else None

    car_number_tag = soup.select_one("span.state-num")
    car_number = car_number_tag.get_text(strip=True)[:10] if car_number_tag else None

    found_at = datetime.datetime.now()

    print(dict(
        url=url,
        title=title,
        price_usd=price_usd,
        odometer=odometer,
        username=username,
        image_url=image_url,
        image_count=image_count,
        car_number=car_number,
        car_vin=car_vin,
        datetime_found=found_at
    ))


def get_home_cars() -> [Car]:
    all_cars = []
    page = 1

    while True:
        url = f"{BASE_URL}?page={page}"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        car_cards = soup.select(".content-bar")
        if not car_cards:
            break

        for car_card in car_cards:
            car = parse_single_car(car_card)
            all_cars.append(car)

        page += 1

    return all_cars


def main():
    get_home_cars()


if __name__ == '__main__':
    main()