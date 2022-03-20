# # with open("weather-data.csv") as data_file:
# #     data = data_file.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather-data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# # print(temperature)
#
# import pandas
#
# data = pandas.read_csv("weather-data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # # print(temp_list)
# # print(data["temp"].max())
# # print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)
import pandas
data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

squirrel_color = data["Primary Fur Color"].to_list()
# print(squirrel_color)
num_of_gray_squirrels = squirrel_color.count("Gray")
# print(num_of_grey_squirrels)
num_of_cinnamon_squirrels = squirrel_color.count("Cinnamon")
num_of_black_squirrels = squirrel_color.count("Black")
squirrel_color_dict = {
    "Colors": ["Black", "Cinnamon", "Gray"],
    "Num of squirrels": [num_of_black_squirrels, num_of_cinnamon_squirrels, num_of_gray_squirrels]
}
squirrel_color_dataframe = pandas.DataFrame(squirrel_color_dict)
# print(squirrel_color_dataframe)
squirrel_color_dataframe.to_csv("squirrel_count.csv")
