# ladong the modules
import pandas as pd
import seaborn as sns
import streamlit as st

import numpy as np
# from PIL import Im

import matplotlib.pyplot as plt

# PAGE CONFIG
st.set_page_config(
    page_title="Stats Magic"
    ,page_icon="✨"
    ,layout="wide"
    #,initial_sidebar_state="expanded"
    )

#st.sidebar.title('Choose the dataset')

# Sampling Reference
st.title("Stats Magic Demo ✨")

#st.header("Sampling Process")
#sampling_process = Image.open('sampling_reference.png')
#st.image(sampling_process, caption = "Sampling Process")



# Import the datasets
titanic = pd.read_csv('https://raw.githubusercontent.com/vkoul/data/main/misc/titanic.csv')
air = pd.read_csv("https://raw.githubusercontent.com/vkoul/data/main/misc/air_miles.csv")

# Air Section
st.header(" Flight Data 🛫")

# air counts
air_rows = air.shape[0]

## Header
# Plot the Population chart 
air_mean = round(air.air_passenger_miles.mean(),2)
air_median = air.air_passenger_miles.median()

# Population chart
def air_popn_chart():
    plt.figure(figsize = (5,5))

    fig, ax = plt.subplots()

    ax = sns.histplot(x = 'air_passenger_miles', data = air, kde = True, bins = 18);
    ax.axvline(x = air_mean, label = "mean", color = "red");
    ax.axvline(x = air_median, label = "median", color = "green")
    ax.set_title(f"The population mean is {air_mean} miles ")
  

    ax.legend()
    
    # display the plot
    st.pyplot(fig)
  

# Selecting the sample
st.subheader(" Select the flight sample details")
air_sample_count = st.slider(label = "How many people collect samples?", min_value = 1, max_value = 500, step = 10,value = 50, key = 1)
air_sample_size = st.slider(label = "How much sample they can collect?", min_value = 1, max_value = air_rows, step = 10,value = 500, key = 2)

# Final text 
st.write(f'We have taken a {air_sample_count} sample each with a sample size of {air_sample_size}')


# sample details 
# plot the sample histogram

def air_sample_chart():
    plt.figure(figsize = (10,8))

    fig, ax = plt.subplots()

    ax = sns.histplot(air_sample_mean_list, kde = True, label = "histogram of sample means")
    ax.axvline(x = sampling_mean, color = "red", label = "sampling mean")
    ax.set_title(f"The sampling mean is {sampling_mean} miles ")
    ax.legend();

    # display the plot
    st.pyplot(fig)
  

## Show charts side by side
col1, col2 = st.columns(2)

with col1:
    st.title('The Population Distribution')
    air_popn_chart()

with col2:
    # Final text 
    st.title('The Sampling Distribution')

    # defining an empty list
    air_sample_mean_list = []

    for sample in range(1,air_sample_count):
            (air_sample_mean_list.append(round(air.air_passenger_miles.sample(air_sample_size, 
                                                                            random_state = sample, replace=True).mean(),3))
            )
            
    # print the mean
    sampling_mean = round(np.mean(air_sample_mean_list),2)
    
    # st.write(f'We have taken a {air_sample_count} sample each with a sample size of {air_sample_size}')
    air_sample_chart()

    ## Error 
    # pop_sample_diff_abs = (air_mean - sampling_mean)
    # pop_sample_diff_perc = (np.array(air_mean) - np.array(sampling_mean)) / np.array(air_mean)
    # st.write(f'The difference from Population mean and Sample mean is {pop_sample_diff_abs: .1f} which is {pop_sample_diff_perc:.2%}')


############# TITANIC DATA ###########################################

# st.write( ":heavy_minus_sign:" * 95)

st.header("Fare data in Titanic 🚢")

## TITANIC Population details
titanic_pop_mean = round(titanic.Fare.mean(),2)
titanic_rows = titanic.shape[0]

# print("The mean fare is {} dollars".format(titanic_pop_mean))

def titanic_popn_chart():
    
    titanic_popn_fig, ax = plt.subplots()

    ax = sns.histplot(x = 'Fare', data = titanic, kde = True);
    ax.axvline(x = titanic_pop_mean, color = "red", label = "Population Mean")
    ax.set_title("The mean population fare is ${}".format(titanic_pop_mean))
    ax.legend()

    # display the plot
    st.pyplot(titanic_popn_fig)

## TITANIC Sample details

# Selecting the sample
st.subheader(" Select the sample details")
age_sample_count = st.slider(label = "How many people collect samples?", min_value = 1, max_value = 500, step = 10,value = 50, key = 3)
age_sample_size = st.slider(label = "How much sample they can collect?", min_value = 1, max_value = titanic_rows, step = 10,value = 500, key = 4)

# define the values
titanic_sample_mean_list = [round(titanic.Fare.sample(age_sample_size, replace=True).mean(),3) for x in range(1, age_sample_count+1)]
titanic_sample_sd_list = [round(titanic.Fare.sample(age_sample_size, replace=True).std(),3) for x in range(1, age_sample_count+1)]
        
titanic_sampling_mean = round(np.mean(titanic_sample_mean_list),2)

# define the chart
def titanic_sample_chart():
    
    titanic_sample_fig, ax = plt.subplots()

    ax = sns.histplot(titanic_sample_mean_list, kde = True, label = "histogram of sample means")
    ax.axvline(x = titanic_sampling_mean, color = "red", label = "sampling mean")
    ax.set_title("The mean sample fare is ${}".format(titanic_sampling_mean))
    ax.legend();

    # display the plot
    st.pyplot(titanic_sample_fig)


# Displaying the charts

## Show charts side by side
titanic_col1, titanic_col2 = st.columns(2)

with titanic_col1:
    st.title('Fare Population Distribution')
    titanic_popn_chart()

with titanic_col2:
    # Final text 
    st.title('Fare Sampling Distribution')
    titanic_sample_chart()

    ## Error 
    # titanic_pop_sample_diff_abs = (titanic_pop_mean - titanic_sampling_mean)
    # titanic_pop_sample_diff_perc = (titanic_pop_mean - titanic_sampling_mean)/titanic_pop_mean

    # st.write(f"The difference from Fare's Population mean and Sample mean is {titanic_pop_sample_diff_abs: .1f} which is {titanic_pop_sample_diff_perc:.2%}")

    
