# AI Travel Expense Optimizer

A Streamlit-based application that helps users optimize travel expenses based on their budget and preferences. The app suggests destinations, accommodations, and activities while ensuring the total cost remains within budget. Future updates will include dynamic data integration for flights and hotels, an interactive map, and inflation-based budget adjustments.

## Features

- Input travel preferences: budget, type of trip (luxury, adventure, local culture), and trip duration.
- Get destination recommendations with estimated costs.
- Dynamic budget adjustment based on user preferences and trip length.

### Upcoming in Version 2
- Dynamic data for flights and hotels using APIs.
- Interactive map to explore destinations.
- Weights on previous trip costs, travel dates, and destination for more accurate recommendations.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AI_Travel_Expense_Optimizer.git
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the app:
   ```bash
   streamlit run travel_expense_optimizer.py
4. Access the deployed app:
   You can try out the app live here: [AI Travel Expense Optimizer] (https://costsavvytravels.streamlit.app/)

## Technologies Used
- Python: Core programming language for building the app.
- Streamlit: Used for building the web application interface.
- Pandas, NumPy: Data manipulation and calculations.
- Folium: For interactive maps (upcoming).
- API Integration: Flight and hotel data (upcoming).

## Future Improvements
- Integrating real-time flight and hotel price data from APIs like Skyscanner and Booking.com.
- Interactive map for destination exploration.
- Inflation-adjusted budgeting for more accurate trip planning.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page(https://github.com/biplobgon/AI_Travel_Expense_Optimizer/issues) or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

### **2. Repository Structure**
```vbnet
AI_Travel_Expense_Optimizer/ ├── .gitignore # Add unnecessary files to ignore, like .DS_Store or environment files ├── travel_expense_optimizer.py # The main Streamlit app script ├── README.md # A detailed description of the project ├── requirements.txt # Dependencies for the project ├── LICENSE # License file for your project (MIT, Apache, etc.) └── assets/ # Store images, screenshots, or media for README


