import streamlit as st

# Title
st.title("Unit Converter")

# Conversion Types
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Function to convert length
def convert_length(value, from_unit, to_unit):
    length_units = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701}
    return value * (length_units[to_unit] / length_units[from_unit])

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    weight_units = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    return value * (weight_units[to_unit] / weight_units[from_unit])

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # Same unit conversion

# User Input
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
elif conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)

# Convert Button
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    else:
        result = convert_temperature(value, from_unit, to_unit)
    
    st.success(f"Converted Value: {result:.2f} {to_unit}")
