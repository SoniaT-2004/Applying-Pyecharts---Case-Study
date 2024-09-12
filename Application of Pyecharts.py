import json

# open U.S. data file
f_us = open('US.txt','r',encoding='utf-8')
US = f_us.read()
# open Japan data file
f_jp = open('JP.txt','r',encoding='utf-8')
JP = f_jp.read()
# open Indian data file
f_in = open('IN.txt','r',encoding='utf-8')
IN = f_in.read()

def get_trend(country):
    # get rid of inconsistent characters at the start and the end for the country's data
    country_data = country[country.index('(')+1:country.index(')')]
    # convert from json to python language and obtain a dictionary
    country_dict = json.loads(country_data)
    # return the value of the key 'trend'
    return country_dict['data'][0]['trend']

# get the x axis and y axis for each country's graph
'''
first, use array slicing to select data in 2020
x axis is the date (in 2020)
y axis is the number of people tested positive on each date (in 2020)
'''
us_data_trend = get_trend(US)
us_xaxis = us_data_trend['updateDate'][:314]
us_yaxis = us_data_trend['list'][0]['data'][:314]

jp_data_trend = get_trend(JP)
jp_xaxis = jp_data_trend['updateDate'][:315]
jp_yaxis = jp_data_trend['list'][0]['data'][:315]

in_data_trend = get_trend(IN)
in_xaxis = in_data_trend['updateDate'][:269]
in_yaxis = in_data_trend['list'][0]['data'][:269]

# plot graph
from pyecharts.charts import Line
line = Line()
# add x_axis data
line.add_xaxis(us_xaxis)
line.add_xaxis(jp_xaxis)
line.add_xaxis(in_xaxis)
# add y_axis data
line.add_yaxis("U.S.", us_yaxis)
line.add_yaxis("Japan", jp_yaxis)
line.add_yaxis("India", in_yaxis)

# import options
from pyecharts import options as opts
line.set_global_opts(
    title_opts = opts.TitleOpts(title="COVID 19 Data - Population Tested Positive Each Day in 2020", pos_left="center", pos_top="0%"),
    legend_opts = opts.LegendOpts(is_show=True, pos_right="right", pos_top="20%"),
    toolbox_opts = opts.ToolboxOpts(is_show=True),
)

# use render
line.render()

# close files
f_us.close()
f_jp.close()
f_in.close()