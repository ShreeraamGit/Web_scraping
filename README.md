# Web_scraping

This repostry contains the files related to Analysis/Data Visualization Report: Bike Ride Trends and Biker Types of Ford GoBike System for April, 2019

####Dataset

This document explores the Ford GoBike's trip data for public containing bike rides from Fall 2017. Each trip is anonymized and includes: • Trip Duration (seconds) • Start Time and Date • End Time and Date • Start Station ID • Start Station Name • Start Station Latitude • Start Station Longitude • End Station ID • End Station Name • End Station Latitude • End Station Longitude • Bike ID • User Type (Subscriber or Customer – “Subscriber” = Member or “Customer” = Casual).

1.Installation

The code should run with no issues using Python versions 3.*

2.Project Motivation

For this project i wanted to answer the business questions like,

The time utilised by the users.
Time of the day most users prefer to use the services.
Day of the week most users prefer to use the services.
Month of the week most users prefer to use the services.
3.File Descriptions

This repostry has the Jupyter notebook where you can refer call codes for Analysis.

Summary of Findings:

we can say that the time utilised by the users is fairly right skewed.we have right skew issue which should be solved by using logarthimic scale.bike durations range from less than 1 minute to 1400+ minutes with median at around 9 min and mean at around 12 min. We have to do some data transformation to make data visualization and data interpretation easiler.

After transformation we can say definetly that both the customers and the subscribers use the service for average time is between 3 - 30 mins from the above histogram.

From the above the analysis we can come to know that the company has more than 78% Subscribers and around 22% customers.

From the analysis we have a surprising details that although the company has only 22% customers they are the users who tend to use the service of the company for longer time when compared to the subscribers. There are less subscribers who tend to use the service for longer time is less.To be precise we can say that the Average time of the subsribers Fall in the range between (1 -50 mins) while the customers tend to use the service for longer time (i.e) the average time fall between ( 1- 350 mins).

We can say now confidently that the most preferred time for the user to use the service provded by the company is Morning (i.e) 05.00 hrs to 8.00 hrs.Followed by Mid-day (i.e) from 15.00 hrs to 18.00hrs.The least preferred is the Evenings people never use the service the most during 18.00 hrs to 23.00 hrs.

As we already know that the months October and September are the most preferred months for the users but every month they tend to use the services for longer times on Saturdays and Sundays.

From the Distplot we can see that the Saturday and Sunday the users tend to use the services between 10:00 hrs - 20:00 hrs.And in weekdays the users tend to use the service more between 6:00 hrs - 10:00 hrs & 15:00 hrs - 19:00 hrs.

5.Licensing, Authors, and Acknowledgements.

This data set used for training is provided by System Data bay Wheels
