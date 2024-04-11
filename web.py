import streamlit as st

def main():
    st.markdown(
        """
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div>
                 <h3 style="margin-left: 8px;">Your Gym </h3>
            </div>
            <div>
                <a href='#'>Home</a> | <a href='#'>About</a> | <a href='#'>Contact Us</a> | <a href='#'>Support</a> | <a href='#'>Sign In</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Gym Admission Form")

    # Get user input for personal details
    st.header("Personal Details")
    name = st.text_input("Name")
    address = st.text_input('Address')
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    personal_training = st.checkbox('Do you want personal training?')

    # Get user input for contact details
    st.header("Contact Details")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    # Get user input for membership type
    st.header("Membership Type")
    membership_type = st.radio("Select Membership Type", options=["Monthly", "Quarterly", "Yearly"])

    # Get user input for fitness goals
    st.header("Fitness Goals")
    fitness_goals = st.text_area("What are your fitness goals?")

    # Get user input for medical conditions
    st.header("Medical Conditions")
    medical_conditions = st.text_area("Do you have any medical conditions? If yes, please specify.")

    # Terms and Conditions
    st.header("Terms and Conditions")
    agree_terms = st.checkbox("I agree to the terms and conditions")

    # Display submit button
    if st.button("Submit"):
        # Save form data to a file or database
        save_data(name, address, age, gender, personal_training, email, phone, membership_type, fitness_goals, medical_conditions)
        st.success("Form submitted successfully!")


def save_data(name, address, age, gender, persnoal_training, email, phone, membership_type, fitness_goals, medical_conditions):
    # Save form data to a file or database
    with open("gym_admission_data.txt", "a") as f:
        f.write(f"Name: {name}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Gender: {gender}\n")
        f.write(f"Persnoal Training: {persnoal_training}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"Membership Type: {membership_type}\n")
        f.write(f"Fitness Goals: {fitness_goals}\n")
        f.write(f"Medical Conditions: {medical_conditions}\n\n")


if __name__ == "__main__":
    main()





