#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def scrape_data():
    """Retrieve and extract data from a simple webpage."""

    url = "https://example.com"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title found"

    return title


def train_simple_model():
    """
    Demonstrate a very simple machine learning concept.

    The model learns the relationship between study hours and marks
    using a simple linear regression formula.
    """

    # Training data
    study_hours = [1, 2, 3, 4, 5]
    marks = [45, 50, 58, 65, 72]

    # Calculate averages
    average_hours = sum(study_hours) / len(study_hours)
    average_marks = sum(marks) / len(marks)

    # Calculate slope
    numerator = sum(
        (x - average_hours) * (y - average_marks)
        for x, y in zip(study_hours, marks)
    )

    denominator = sum(
        (x - average_hours) ** 2
        for x in study_hours
    )

    slope = numerator / denominator

    # Calculate intercept
    intercept = average_marks - (slope * average_hours)

    return slope, intercept


def predict(hours, slope, intercept):
    """Predict a student's mark based on study hours."""

    return slope * hours + intercept


def main():
    print("Simple Machine Learning Example")
    print("--------------------------------")

    # Demonstrate web scraping
    try:
        webpage_title = scrape_data()
        print(f"Webpage title: {webpage_title}")
    except requests.RequestException as error:
        print(f"Could not access webpage: {error}")

    # Train the simple model
    slope, intercept = train_simple_model()

    # Make a prediction
    study_hours = 6
    predicted_mark = predict(study_hours, slope, intercept)

    print(f"Study hours: {study_hours}")
    print(f"Predicted mark: {predicted_mark:.2f}%")


if __name__ == "__main__":
    main()
