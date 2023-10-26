import sched
import time

def get_weather(latitude, longitude):
    baseurl = f"http://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10,"
    response = requests.get(base_url)
    data = reponse.json()
    return data

def send_text(body):
    account_sid = "twilio_sid"
    auth_token = "twilio_token"
    from_number = "from_number"
    to_number = "to_number"

    client = Client(account_sid, auth_token)

    message = client.message.create(
        body = body,
        from_ = from_number,
        to_= to_number
    )
    print("SENT")

def send_weather_update():
    # Weather to send
    latitude = 40.7128
    longitude = 74.006

    weather_data = get_weather(latitude, longitude)
    temperature_celsius = weather_data["hourly"]["temperature_2m"][0]
    relative_humidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]

    weather_info = (
        f"temperature: {temperature_celsius:.2f}C\n"
        f"relativehumidity: {relative_humidity}%\n"
    )
    send_text(weather_info)

def main():
    sched.every().day.at("08:00").do(send_weather_update)
    while True:
        schedule.run_pending()
        time.sleep()

if __name__ == '__main__':
    main()

