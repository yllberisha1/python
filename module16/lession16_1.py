import streamlit as st

def calculate (num1, num2, operation):
   if operation == "Addition":
       result = num1 + num2
   elif operation == "Subtraction":
       result = num1 - num2
   elif operation == "Multiply":
       result = num1 * num2
   elif operation == "Division":
       try:
           result = num1 / num2
       except ZeroDivisionError:
           result = "Cannot divide by zero"
   return result

def main():
    st.title("Simple calculator")
    num1 = st.number_input("Enter the first number", step=1)
    num2 = st.number_input("Enter the second number",step=2)
    operation = st.radio("Select operation", ['Addition', 'Subtraction', 'Multiply', 'Division'])

    result = calculate(num1, num2, operation)

    st.write(f"Result of the {operation} of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()

