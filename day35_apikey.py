import requests
api_key = "aa2111d932291f0027a0f04e2e040df8"
endpointAPI="https://api.openweathermap.org/data/2.5/onecall"
apiparams = {
"lat":22.499299,
"lon":103.960460,
"exclude":"current,minutely,daily",
"appid":api_key
}
response = requests.get(endpointAPI,params=apiparams)
#nếu không trả về 200 success thì sẽ hiện ra đang lỗi ở đâu
response.raise_for_status()
#lưu dữ liệu thu được save vào biến dưới dạng json
weather_data = response.json()
#print(weather_data["hourly"][1]["weather"][0]["id"])
# vấn đề ở đây là muốn lấy 12h đầu và ta phải tìm cách chia file json ra để for
weather_slice = weather_data["hourly"][:12] # sẽ có một tệp list các dict trong list này
for hour_data in weather_slice:
    print(hour_data["weather"][0]["id"])