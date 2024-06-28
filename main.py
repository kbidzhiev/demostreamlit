import streamlit as st
import matplotlib.pyplot as plt
from pyvectorSDK import vectorSDK

# Set the title of the app
st.title('pyvectorSDK Streamlit App')

# Input: Accepting a list of numbers from the user
user_input = st.text_input('Enter a list of numbers (comma-separated):', '1, 2, 3, 4, 5')

# Convert the input string to a list of floats
try:
    vector = vectorSDK([float(i) for i in user_input.split(',')])
except ValueError:
    st.error('Please enter a valid list of numbers.')
    st.stop()

# Button to sort the vector
if st.button('Sort Vector'):
    sorted_vector = vector.sort()
    st.write(f'The sorted vector is: {sorted_vector}')

# Input: Slider to accept a value for p from the user
p_value = st.slider('Select the value of p for norm computation:', min_value=0.1, max_value=10.0, value=2.0, step=0.1)

# Compute and display norm automatically when the slider is manipulated
norm = vector.compute_norm(p_value)
st.write(f'The norm of the vector with p = {p_value} is: {norm}')

# Plotting x = p values, y = norms
p_values = [i / 10.0 for i in range(5, 41)]  # Generate p values from 0.1 to 10.0
norm_values = [vector.compute_norm(p) for p in p_values]  # Compute corresponding norms

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(p_values, norm_values, marker='o')
plt.xlabel('p value')
plt.ylabel('Norm')
plt.title('Norm of the vector for different p values')
plt.grid(True)

# Display the plot
st.pyplot(plt)
