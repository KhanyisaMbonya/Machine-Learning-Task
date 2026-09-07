# Machine-Learning-Task

## Description

This project demonstrates a simple example of machine learning using
Python.

The example uses a small dataset containing study hours and student marks.
A simple linear regression model is created from this data to learn the
relationship between the number of hours studied and the resulting mark.

The project also demonstrates basic web scraping using the Requests and
BeautifulSoup libraries.

## What the Program Does

The program performs the following steps:

1. Sends a request to a webpage using Requests.
2. Uses BeautifulSoup to read the webpage HTML.
3. Extracts the webpage title.
4. Creates a small training dataset containing study hours and marks.
5. Calculates a simple linear regression model.
6. Uses the trained model to predict a student's mark.
7. Displays the prediction.

## Machine Learning Explanation

The machine learning part of the program uses a simple form of linear
regression.

The training data contains two variables:

- Study hours
- Student marks

For example:

| Study Hours | Mark |
|-------------|------|
| 1 | 45 |
| 2 | 50 |
| 3 | 58 |
| 4 | 65 |
| 5 | 72 |

The model looks at these examples and calculates the relationship between
study hours and marks.

The relationship can be represented by:

y = mx + b

Where:

- y is the predicted mark
- x is the number of study hours
- m is the slope
- b is the intercept

After training, the model can be used to make a prediction for new data.

For example, the program predicts the expected mark for a student who
studies for 6 hours.

## Web Scraping Explanation

The project also demonstrates the use of Requests and BeautifulSoup.

Requests is used to retrieve the HTML content of a webpage.

BeautifulSoup then processes the HTML so that information such as the
webpage title can be extracted.

This demonstrates how external data can be retrieved and processed before
being used by a program.

## Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- Linear Regression
- GitHub

## Requirements

The following software is required:

- Python 3
- pip
- Internet connection

## Installation

Clone the repository:

    git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

    cd simple-ml-example

Create a virtual environment:

    python -m venv .venv

Activate the virtual environment.

### Windows

    .venv\Scripts\activate

### macOS/Linux

    source .venv/bin/activate

Install the required packages:

    pip install -r requirements.txt

## Running the Program

Run:

    python main.py

The program will retrieve the webpage title and then train the simple
machine learning model.

It will finally display a predicted mark.

Example:

    Simple Machine Learning Example
    --------------------------------
    Webpage title: Example Domain
    Study hours: 6
    Predicted mark: 78.20%

The exact prediction depends on the training data used in the program.

## Project Structure

    simple-ml-example/
    |
    |-- main.py
    |-- README.md
    |-- requirements.txt
    |-- .gitignore

## Author

Khanyisa Mbonya
