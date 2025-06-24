# Electricity-Demand-Analysis-in-USA from 2019-2025

The data was sourced via a public API from the EIA website, covering U.S. power consumption between 2019 and 2025 From PJM Region ,Data contains 56,666 rows and Two columns Datatime and PJM_MW (Electricity Demand) as output 

through this website u can get Dataset : https://www.eia.gov/electricity/gridmonitor/dashboard/electric_overview/US48/US48

![Screenshot (1610)](https://github.com/user-attachments/assets/e4a9ca26-df1c-4ac3-94ad-56fe465e28cf)

this is a sample of dataset after setting Datatime column as index :

![Screenshot (1611)](https://github.com/user-attachments/assets/da487bda-8c24-4f6e-b021-fc019d5cecba)


# Actual Electricity Demand in USA Over Time(2019-2025)

![newplot (18)](https://github.com/user-attachments/assets/bb45d065-a39c-4ea9-893e-54391fd3e705) 


## Preprocessing steps followed :

1- Removing outliers specific in oct 2021 using IQR.

2- Converted the date column into a datetime format to enable the creation of calendar-based features such as hour, month, day, weekday, and season for exploratory data analysis (EDA).

3- Removing  Missing Values .

4- Using Plotly and Seaborn , Matplotlib for Data visualization. 

5- Perform EDA on each Feature to show how impactful is it for gaining insights and uncover hidden patterns .


![image](https://github.com/user-attachments/assets/df54ed1e-3375-4454-b639-493da1700cfa)


![newplot](https://github.com/user-attachments/assets/093afe0f-002b-43c2-8db5-209b936967b1)


![image](https://github.com/user-attachments/assets/9e36c09d-ee3a-40af-96e6-2a85b9778bb8)


![image](https://github.com/user-attachments/assets/6f66f9c7-9cfd-4ed2-acf3-464b54bfe0b5)


![image](https://github.com/user-attachments/assets/4d333cb7-580b-4952-a1b7-da37796d1dc8)


![image](https://github.com/user-attachments/assets/aa61a8a3-e14e-4fd3-b70c-a379db9b1d30)


![image](https://github.com/user-attachments/assets/bf97d59a-4efe-4131-b36b-f75ab08f8b5c)


![newplot](https://github.com/user-attachments/assets/093afe0f-002b-43c2-8db5-209b936967b1)


## Models :

1- I used Prophet, developed by Facebook, due to its ability to automatically detect seasonality, handle non-linear trends, and work without requiring the data to be stationary. Prophet accepts data in a specific format, where ds refers to datetime and y represents the target variable — in this case, PJM_MW (Electricity Demand). I manually split the dataset by assigning all records after '2024-07-01' as the test set, and the rest as training data. The model achieved a MAPE of 9% . I also experimented with adding holiday effects to the model, but they did not improve performance — the MAPE remained nearly the same at 9.1%.

![image](https://github.com/user-attachments/assets/13ee44ce-0275-4ecd-8602-a016d9ecf259)

![image](https://github.com/user-attachments/assets/86388242-49e0-414d-b560-bc7d513ae0c0)

2- used XGBoost but its not consider datatime column in either training and testing Data, it depends on calender features such as hour,day,season,year and output PJM_MW (Electricity Demand) only but i also split data based on Datatime index due to preserve temporal order so setting each data comes after '2024-07-01' is considered as testing data else i consider it in training data , it was achieved of MAPE of 7 % as u can see it has been outperforming Prophet . so i have choose it for deployment 


## Deployment Model (using Docker and streamlit Web APP ) on Azure :

## u can check it out :

Live APP : https://electricitydemandapp-ezf8cef9btfsajbc.uaenorth-01.azurewebsites.net/

u can choose any future Date and it will forcast how much Electricity Demand for each hour 

![Screenshot (1612)](https://github.com/user-attachments/assets/16abd2bd-1684-4de2-ab65-f56ff197bf9a) 

u can visuialze Electricity Demand for each hour and finding insight about which hour will be the highest and lowest value 

![Screenshot (1613)](https://github.com/user-attachments/assets/8ac0b7c2-1dd9-4c50-b66e-f86c99db5876)


u can download Data that contains hour with forcasted value 

![Screenshot (1615)](https://github.com/user-attachments/assets/70bd672e-49c5-426b-9478-1ca9053fc25e)



