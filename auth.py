import streamlit as st

def user_authentication():
    """Handles user login and logout with Streamlit session_state."""
    
    # Initialize session state if not already set
    if 'user' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user is None:
        # Show login screen
        user = st.text_input("Username", key="username")
        password = st.text_input("Password", type="password", key="password")
        
        if st.button("Login"):
            if user and password:
                # Assuming the login is successful (in real-world use, verify credentials)
                st.session_state.user = user
                st.success(f"Welcome, {user}")
                return True
            else:
                st.error("Please provide both username and password.")
    else:
        # Show logged-in status and logout option
        st.write(f"Logged in as: {st.session_state.user}")
        
        if st.button("Logout"):
            # Clear session state for the 'user' variable on logout
            st.session_state.user = None
            st.success("Logged out successfully!")
            return False
    
    return False
