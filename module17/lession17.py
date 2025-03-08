# import streamlit as st
#
#
# # Function to calculate BMI
# def calculate_bmi(weight, height):
#     # BMI formula: BMI = weight (kg) / (height (m) ^ 2)
#     height_m = height / 100  # Convert height from cm to meters
#     bmi = weight / (height_m ** 2)
#     return bmi
#
#
# # Main function to create the Streamlit app
# def main():
#     # Streamlit input widgets for user data
#     st.title("Personal Info and BMI Calculator")
#
#     name = st.text_input("Enter your first name:")
#     surname = st.text_input("Enter your surname:")
#     age = st.number_input("Enter your age:", min_value=1, max_value=150, step=1)
#     height = st.number_input("Enter your height in cm:", min_value=50, max_value=300, step=1)
#     weight = st.number_input("Enter your weight in kg:", min_value=10, max_value=300, step=1)
#
#     # When the user clicks the 'Calculate' button
#     if st.button("Calculate BMI"):
#         # Ensure that all inputs are provided
#         if name and surname and age and height and weight:
#             # Calculate BMI
#             bmi = calculate_bmi(weight, height)
#
#             # Show the results
#             st.write(f"---")
#             st.write(f"Name: {name} {surname}")
#             st.write(f"Age: {age} years")
#             st.write(f"Height: {height} cm")
#             st.write(f"Weight: {weight} kg")
#             st.write(f"BMI: {bmi:.2f}")
#
#             # BMI classification
#             if bmi < 18.5:
#                 st.write("You are underweight.")
#             elif 18.5 <= bmi < 24.9:
#                 st.write("You have a normal weight.")
#             elif 25 <= bmi < 29.9:
#                 st.write("You are overweight.")
#             else:
#                 st.write("You are obese.")
#         else:
#             st.error("Please fill in all the fields.")
#
#
# if __name__ == "__main__":
#     main()

import streamlit as st


# Function to calculate BMI
def calculate_bmi(weight, height):
    # BMI formula: BMI = weight (kg) / (height (m) ^ 2)
    height_m = height / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi


# Main function to create the Streamlit app
def main():
    # Streamlit input widgets for user data
    st.title("Personal Info and BMI Calculator")

    if 'users' not in st.session_state:
        st.session_state['users'] = []

    # Input fields
    name = st.text_input("Enter your first name:")
    surname = st.text_input("Enter your surname:")
    age = st.number_input("Enter your age:", min_value=1, max_value=150, step=1)
    height = st.number_input("Enter your height in cm:", min_value=50, max_value=300, step=1)
    weight = st.number_input("Enter your weight in kg:", min_value=10, max_value=300, step=1)

    # When the user clicks the 'Add New User' button
    if st.button("Add New User"):
        if name and surname and age and height and weight:
            # Calculate BMI
            bmi = calculate_bmi(weight, height)

            # Add user data to session state
            st.session_state['users'].append({
                'name': name,
                'surname': surname,
                'age': age,
                'height': height,
                'weight': weight,
                'bmi': bmi
            })

            # Display confirmation message
            st.success(f"User {name} {surname} added successfully!")

            # Clear the input fields after adding
            st.experimental_rerun()

    # Show list of users added and their details
    if st.session_state['users']:
        st.write("### Users Added:")
        for user in st.session_state['users']:
            st.write(f"Name: {user['name']} {user['surname']}")
            st.write(f"Age: {user['age']} years")
            st.write(f"Height: {user['height']} cm")
            st.write(f"Weight: {user['weight']} kg")
            st.write(f"BMI: {user['bmi']:.2f}")

            # BMI classification
            if user['bmi'] < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= user['bmi'] < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= user['bmi'] < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")
            st.write("---")


if __name__ == "__main__":
    main()
