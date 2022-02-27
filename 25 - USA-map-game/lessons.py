import pandas as pd

# data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
#
# # avg_temp = sum(temp_list) / len(temp_list)
#
# # print(data[data.temp == data.temp.max()])
#
# monday_temp = int(data.temp[data.day == "Monday"])
# monday_f = (monday_temp * (9/5)) + 32
# print(monday_f)

squirrel_csv = pd.read_csv("Squirrel_Data.csv")

# print(squirrel_csv.keys())
# squirrel_df['Count'][squirrel_df['Fur-color'] == "gray"] =
# squirrel_csv[squirrel_csv["Primary Fur Color"] == "grey"].count()

fur_color = squirrel_csv["Primary Fur Color"]

gray = fur_color[fur_color == "Gray"].count()
red = fur_color[fur_color == "Cinnamon"].count()
black = fur_color[fur_color == "Black"].count()

df = {
    'Fur-color': ["gray", "red", "black"],
    'Count': [gray, red, black]
}

# df['Count'][df['Fur-color'] == "gray"] = fur_color[fur_color == "Gray"].count()
# df['Count'][df['Fur-color'] == "red"] = fur_color[fur_color == "Cinnamon"].count()
# df['Count'][df['Fur-color'] == "black"] = fur_color[fur_color == "Black"].count()

squirrel_df = pd.DataFrame(df)
print(squirrel_df)
squirrel_df.to_csv("Squirrel Fur Count.csv")
