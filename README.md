# Parking Tickets Analysis Dashboard

This project provides an interactive dashboard for analyzing parking tickets data from Toronto for the years 2017-2020. The dashboard allows users to explore various insights and trends in the data, including yearly trends, fine amounts, location-based analysis, and more.

## Features

- Yearly Trend of Parking Tickets
- Total Fine Amount by Year
- Monthly Trend of Parking Tickets
- Top 10 Locations with Most Tickets
- Distribution of Infraction Types
- Total Fine Amount by Infraction Type
- Scatter Plot: Fine Amount vs. Ticket Count by Location
- Heat Map: Ticket Count by Location and Year
- Heat Map: Fine Amount by Location and Year
- Infraction Code Distribution Over the Years

## Installation

To run this project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gemmap520/parking_ticket_dashboard.git
    cd parking_ticket_dashboard
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Streamlit app:**

    ```bash
    streamlit run dashboard.py
    ```

## Usage

Once you have the app running, you can use the sidebar to select different filters and graphs to display. The available filters include:

- Year range
- Locations
- Infraction types

You can also choose which graphs to display, including trends, distributions, scatter plots, and heat maps.

## Data

The data used in this project is the Toronto parking tickets data for the years 2017-2020. The dataset includes the following columns:

- `Year`: The year the ticket was issued
- `Infraction_Code`: The code for the type of infraction
- `Infraction_Description`: The description of the infraction
- `Location`: The location where the ticket was issued
- `Total_Fine_Amount`: The total fine amount for the ticket
- `Ticket_Count`: The count of tickets issued

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License.

## Contact

For any questions or inquiries, please contact:

- Name: Gemma Park
- Email: gemmap520@gmail.com

## Acknowledgments

Special thanks to the Toronto Open Data initiative for providing the parking tickets dataset.

