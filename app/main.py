import os
import requests
import openai

# 環境変数からAPIキーを取得
openai.api_key = os.getenv("OPENAI_API_KEY")

# 天気データ取得用のパラメータ
latitude = 35.6895
longitude = 139.6917
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=Asia/Tokyo"

def get_weather_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve data")
        return None

def generate_comment(weather_summary):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a weather comment based on this summary: {weather_summary}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

def main():
    # 天気データを取得
    weather_data = get_weather_data(url)

    if weather_data:
        # データを整形して表示
        daily_data = weather_data['daily']
        weather_summary = []
        
        for date, temp_max, temp_min, precipitation in zip(
            daily_data['time'],
            daily_data['temperature_2m_max'],
            daily_data['temperature_2m_min'],
            daily_data['precipitation_sum']
        ):
            summary = f"Date: {date}, Max Temp: {temp_max}°C, Min Temp: {temp_min}°C, Precipitation: {precipitation}mm"
            weather_summary.append(summary)
        
        # 天気データをコンソールに出力
        for summary in weather_summary:
            print(summary)
        
        # 最初の1日のデータを使ってGPTコメントを生成
        if weather_summary:
            comment = generate_comment(weather_summary[0])
            print("\nAIからのコメント:", comment)

if __name__ == "__main__":
    main()