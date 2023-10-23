import sched
import time

def get_weather(latitude, longitude):
    baseurl = f"http://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10,"
    response = requests.get(base_url)
    data = reponse.json()
    return data

def send_weather_update():
    # Weather to send
    latitude = 40.7128
    longitude = 74.006

    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relativehumidity = weather_data["hourly"]["relativehumidity_2m"][0]
    windspeed =


def main():
    sched.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep()

if __name__ == '__main__':
    main()

