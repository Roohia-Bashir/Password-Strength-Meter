import streamlit as st
import re

# Set page title and icon
st.set_page_config(
    page_title="Password Strength Meter",
    page_icon="🔐",
    layout="centered"
)

# Common passwords to check against
COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "admin", "welcome", 
    "password123", "abc123", "letmein", "monkey", "1234567890"
]

# Function to check password strength
def check_password_strength(password):
    """Check how strong a password is and return feedback"""
    # If no password, return empty result
    if not password:
        return {
            "score": 0,
            "strength": "None",
            "color": "gray",
            "feedback": []
        }
    
    score = 0
    feedback = []
    
    # Check 1: Length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
        feedback.append("❌ Make your password longer (12+ characters is best)")

    # Check 2: Uppercase and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 25
    else:
        feedback.append("❌ Use both UPPERCASE and lowercase letters")
    
    # Check 3: Numbers
    if re.search(r"\d", password):
        score += 25
    else:
        feedback.append("❌ Add at least one number (0-9)")
    
    # Check 4: Special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 25
    else:
        feedback.append("❌ Add at least one special character (!@#$%^&*)")
    
    # Check 5: Common password
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback = ["❌ This is a commonly used password and is easily guessable"]
    
    # Determine strength category
    if score >= 80:
        strength = "Strong"
        color = "green"
    elif score >= 50:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Weak"
        color = "red"
    
    return {
        "score": score,
        "strength": strength,
        "color": color,
        "feedback": feedback
    }

# Main app title
st.title("🔐 Password Strength Meter")
st.markdown("Check how strong your password is and learn how to make it better.")

# Password input
password = st.text_input("Enter your password:", type="password")

# Check and display password strength if a password is provided
if password:
    result = check_password_strength(password)
    
    # Display strength meter
    st.subheader("Password Strength")
    st.progress(result["score"] / 100)
    
    # Display strength rating with color
    st.markdown(f"<h3 style='color: {result['color']};'>{result['strength']}</h3>", unsafe_allow_html=True)
    
    # Display feedback
    if result["feedback"]:
        st.subheader("How to improve your password:")
        for item in result["feedback"]:
            st.markdown(item)
    elif result["strength"] == "Strong":
        st.success("✅ Great job! Your password is strong.")

# Footer
st.markdown("---")
st.markdown("Password security is important! 🛡️")

