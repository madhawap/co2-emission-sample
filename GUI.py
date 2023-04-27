import tkinter as tk
import requests
import json

api_key = ""
url = "https://beta3.api.climatiq.io/estimate"


def display_co2_emission():
    # Extract the co2e_total value from the response data
    json_data = call_endpoint(activity_id_var.get(), filter_var.get(), int(input_var.get()))
    data = json.loads(json_data)
    # co2e_total = data['constituent_gases']['co2e_total']
    co2e_total = data['co2e']

    # Display the co2e_total value below the button
    label3.config(text=f"CO2e: {co2e_total} kg", fg="blue")


def call_endpoint(activity, filtering_para, value=500):
    headers = {
        "Authorization": "Bearer " + api_key,
        "Content-Type": "application/json"
    }
    data = {
        "emission_factor": {
            "activity_id": activity
        },
        "parameters": {
            filtering_para: value,
            "money_unit": "usd"
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    return response.text


# Create the GUI
root = tk.Tk()
root.geometry("600x350")
root.title("Emission Finder")

# Create the variables to store the selected values from the drop-down menus
activity_id_var = tk.StringVar()
filter_var = tk.StringVar()

# Define the options for the drop-down menus
activity_id = ["restaurants_accommodation-type_hotel_restaurant_services",
               "agriculture_forestry_support-type_agriculture_forestry_support",
               "fuel_type_natural_gas-fuel_use_residential_construction_commercial_institutional_agriculture"]
filtering_parameters = ["time", "volume", "money"]

# Sample query
header_label = tk.Label(root, text="How much CO2e has emitted spending $1,000 on Forestry type agriculture")
header_label.pack()

# Create the labels and dropdowns on GUI
label1 = tk.Label(root, text="Select an emission factor:")
label1.pack(pady=10)
activity_id_dropdown = tk.OptionMenu(root, activity_id_var, *activity_id)
activity_id_dropdown.pack()

label2 = tk.Label(root, text="Select a filter:")
label2.pack(pady=10)
filter_para_dropdown = tk.OptionMenu(root, filter_var, *filtering_parameters)
filter_para_dropdown.pack()

# Create the text input field
input_var = tk.StringVar()
input_label = tk.Label(root, text="Enter some text:")
input_label.pack(pady=10)
input_entry = tk.Entry(root, textvariable=input_var)
input_entry.pack()

# Create a button to trigger the endpoint
button = tk.Button(root, text="Get CO2 Emission", command=display_co2_emission)
button.pack(pady=10)

# Create a label to display the co2e value
label3 = tk.Label(root, text="", font=("Helvetica", 14))
label3.pack(pady=10)

# Run the main loop
root.mainloop()
