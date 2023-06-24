# SkyScribe

![SkyScribe Logo](logo.png)

##  `Look Up to the Sky, Command the Forecast!`

## Description

SkyScribe is a powerful weather tool that allows you to effortlessly access and control weather forecasts. With SkyScribe, you can uncover the secrets of the sky and stay ahead of changing weather conditions. This command-line utility tool, created using Python, provides a user-friendly interface to interact with weather data.

### Features

- **Single City Forecast**: Retrieve the weather report for a single city by passing the city name as a parameter.
- **Multiple City Forecast**: Fetch weather reports for multiple cities by providing multiple city names as parameters to the command.
- **Logging**: SkyScribe incorporates a logging module to maintain a log file (`weather.log`) that captures any encountered errors during the execution.
- **User-Friendly Output**: The tool generates well-formatted and easy-to-read weather reports, ensuring a seamless user experience.
- **Error Handling**: The code is equipped with robust error handling mechanisms to gracefully handle invalid parameters or API-related issues.
- **Command-Line Interface**: SkyScribe is designed as a command-line tool, providing a streamlined and efficient workflow for weather forecasting.

## Hackathon Project: Weather Forecasting Tool (Python)

SkyScribe was created as part of a hackathon project with the goal of developing a weather forecasting tool that demonstrates the capabilities of Python programming, API integration, data parsing, and error handling. The project leverages the OpenWeatherMap API to fetch weather data for the specified cities and utilizes Python to parse and present the information to the user.

### API: OpenWeatherMap

SkyScribe integrates the OpenWeatherMap API to retrieve weather data. OpenWeatherMap is a widely used weather data provider that offers a comprehensive set of APIs to access current weather conditions, forecasts, and historical weather data. By leveraging this API, SkyScribe ensures accurate and up-to-date weather information for the specified cities.

### GitHub Copilot

During the hackathon project, the team utilized GitHub Copilot, an AI-powered code completion tool, to assist with various aspects of the development process. GitHub Copilot proved to be instrumental in suggesting API usage patterns, providing guidance on data parsing techniques, and offering error handling suggestions. Its intelligent code suggestions and autocomplete capabilities helped streamline the development workflow and improve overall productivity.

## Installation

To get started with SkyScribe, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/SkyScribe.git
   ```

2. Install the required packages by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

3. Open the project folder in Microsoft Visual Studio Code (VS Code) or your preferred code editor.

4. Execute the main file `skyscribe.py` to start the program.

### Setup Instructions

To set up the SkyScribe project on your local machine, follow these steps:

 **Step 1: Install the Distribution Package**
 The generated distribution package can be distributed and installed on different machines. Users can install your package using pip with the following command:
 ```shell
   pip install /path/to/SkyScribe/dist/SkyScribe-1.0.tar.gz
   ```

   Make sure to replace `/path/to/SkyScribe/dist/SkyScribe-1.0.tar.gz` with the actual path to your distribution package file.

**Step 2: Install from PyPI**
   We have uploaded the package to PyPI (Python Package Index) to make it available for installation using pip from anywhere. Now users can install your package directly from

 PyPI using the following command:
   ```shell
   pip install SkyScribe
   ```
   Note: It's generally recommended to use a virtual environment (`myenv`) to isolate project dependencies and avoid conflicts.

#### Package Creation Process

To create the distribution package, follow these steps:

**Step 1: Create a setup.py File**
   In the root directory of your project (SkyScribe), create a file called `setup.py`. This file will contain the necessary information for packaging and distributing your project.
   Open `setup.py` in a text editor and add the following code:
   ```python
   from setuptools import setup, find_packages
   setup(
       name='SkyScribe',
       version='1.0',
       packages=find_packages(),
       entry_points={
           'console_scripts': [
               'skyscribe = skyscribe:cli',
           ],
       },
   )
   ```

   This code imports the `setup` function from the `setuptools` package and defines the package name, version, and entry point for the console script.

**Step 2: Build the Distribution Package**

   There are two ways to create a distributable package for your project:

   - **Way 1: Using setup.py**

     To create the distribution package using `setup.py`, open a terminal/command prompt and navigate to the root directory of your project (SkyScribe). Run the following command:

     ```shell
     python setup.py sdist bdist_wheel
     ```

     This command builds the distribution package in the `dist` directory. The package will be created in both source and wheel formats.

   - **Way 2: Using PyPI**

     To upload the package to PyPI, follow these steps:

     1. Create an account on PyPI (https://pypi.org/).
     2. Install the `twine` package:

        ```shell
        pip install twine
        ```

     3. Generate the distribution package again:

        ```shell
        python setup.py sdist bdist_wheel
        ```

     4. Upload the package to PyPI:

        ```shell
        twine upload dist/*
        ```

   Now your package will be available for installation using `pip install SkyScribe` from anywhere.

These instructions should help you set up the SkyScribe project on your local machine. If you have any further questions or need assistance, feel free to ask.

## Usage

To use SkyScribe as a command-line tool, follow the instructions below:
- To get help and see available commands, run:

  ```bash
  skyscribe <command> --help
  ```
  Example: `skyscribe city --help`

- For a single city forecast, run the following command:

  ```bash
  skyscribe <command> "CityName" 
  ```
  Example: `skyscribe city Jalgaon`

  Replace `"City Name"` with the name of the city you want to retrieve the weather forecast for.

- For multiple city forecasts, run the following command:

  ```bash
  skyscribe <command> "City Name 1" "City Name 2" "City Name 3"
  ```
  Example: `skyscribe cities Jalgaon Pune Mumbai`

  Replace `"City Name 1"`, `"City Name 2"`, etc., with the names of the cities you want to retrieve the weather forecasts for.

The tool will display the weather forecasts for the specified cities in the command-line interface.

## Contributing

Contributions to SkyScribe are welcome! If you find any issues or have suggestions for improvements, please submit them through the GitHub repository. You can also contribute by opening pull requests with bug fixes, feature enhancements, or code optimizations.

Before contributing, please ensure that you have read the [Contribution Guidelines](CONTRIBUTING.md) for this project.

## License

SkyScribe is licensed under the [MIT License](LICENSE).

## Contact

For any questions, concerns, or feedback, please reach out

 to the project

 team at skyscribe@example.com.

---

Thank you for your interest in SkyScribe! We hope you find it useful for all your weather forecasting needs.
```