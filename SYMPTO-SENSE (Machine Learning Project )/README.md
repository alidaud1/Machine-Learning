# SYMPTO SENSE – Machine Learning Project

## Overview

**SYMPTO SENSE** is a machine learning-based web application designed to assist users in identifying potential health conditions based on their symptoms. By leveraging a CatBoost classifier model, this project analyzes 133 different symptoms to provide immediate insights into possible diseases, helping users make informed decisions about their health.

## Features

- **Symptom Analysis**: Users can input symptoms to receive predictions on potential diseases.
- **Disease Information**: The app provides detailed descriptions of identified diseases, precautions, and medication recommendations to support user understanding and decision-making.
- **User-Friendly Interface**: Built with a Flask interface, ensuring ease of use and accessibility.

## Technology Stack

- **Backend**: Flask
- **Machine Learning**: CatBoost classifier
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: JSON for disease information

## Dataset

The project utilizes a comprehensive dataset consisting of various health conditions and their associated symptoms. 

- **Features**: 
  - `Symptom 1`
  - `Symptom 2`
  - ...
  - `Symptom 133`
  
This dataset was sourced from **Kaggle** and serves as the foundation for training the CatBoost model. Each record in the dataset represents a unique combination of symptoms and the corresponding disease, allowing for accurate predictions.

## Project Structure

The project consists of the following files and folders:

- **model/**: 
  - `model_weights.bin`: Contains the trained CatBoost model weights.
  - `disease_info.json`: A JSON file containing detailed descriptions of diseases, precautions, and medication recommendations.

- **templates/**:
  - `index.html`: The main HTML file for the web app interface.

- **static/**:
  - `style.css`: CSS file for styling the web app.
  - `index.js`: JavaScript file for client-side functionality.
 
## Project Interface

![SYMPTO SENSE Interface](https://github.com/alidaud1/Machine-Learning/blob/main/SYMPTO-SENSE%20(Machine%20Learning%20Project%20)/asset.png?raw=true)

## Installation

To run the SYMPTO SENSE web application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SYMPTO_SENSE.git
