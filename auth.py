import streamlit as st

def user_authentication():
    """Simple authentication flow."""
    if 'user' not in st.session_state:
        st.session_state.user = None

    if st.session_state.user is None:
        # Simple login UI
        user = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if user and password:
                st.session_state.user = user
                st.success(f"Welcome {user}")
                return True
            else:
                st.error("Please provide a username and password.")
    else:
        st.write(f"Logged in as: {st.session_state.user}")
        if st.button("Logout"):
            st.session_state.user = None
            st.success("Logged out")
    return False
