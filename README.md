# Electricity-Demand-Analysis-in-USA from 2019-2025

The data was sourced via a public API from the EIA website, covering U.S. power consumption between 2019 and 2025 From PJM Region ,Data contains 56,663 rows and Two columns Datatime and PJM_MW (Electricity Demand) as output 

through this website u can get Dataset 
![Screenshot (1610)](https://github.com/user-attachments/assets/e4a9ca26-df1c-4ac3-94ad-56fe465e28cf)


# Actual Electricity Demand in USA Over Time(2019-2025)

![newplot (18)](https://github.com/user-attachments/assets/bb45d065-a39c-4ea9-893e-54391fd3e705) 


## Preprocessing steps followed :

1- Removing outliers specific in oct 2021 using IQR.
2- Convert Data column into Datatime so i can Create Calender Features such as Hour,month,day,weekday,season to perform EDA and split data into train and test especially in Prophet Model .
3- removing Missing Data.
4- Using Plotly and Seaborn,Matplotlib for Data visualization. 
5-Perform EDA on each Feature to show how impactful is it for gaining insights and uncover hidden patterns .


![image](https://github.com/user-attachments/assets/9e36c09d-ee3a-40af-96e6-2a85b9778bb8)


![image](https://github.com/user-attachments/assets/df54ed1e-3375-4454-b639-493da1700cfa)


![image](https://github.com/user-attachments/assets/6f66f9c7-9cfd-4ed2-acf3-464b54bfe0b5)


![image](https://github.com/user-attachments/assets/4d333cb7-580b-4952-a1b7-da37796d1dc8)


![image](https://github.com/user-attachments/assets/aa61a8a3-e14e-4fd3-b70c-a379db9b1d30)


![image](https://github.com/user-attachments/assets/bf97d59a-4efe-4131-b36b-f75ab08f8b5c)


![newplot](https://github.com/user-attachments/assets/093afe0f-002b-43c2-8db5-209b936967b1)

