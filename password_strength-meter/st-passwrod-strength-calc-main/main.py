import streamlit as st
import re
import math

def calculate_entropy(password):
    """Calculate password entropy (bits of strength)"""

    lower_chars = len(re.findall(r'[a-z]', password))
    upper_chars = len(re.findall(r'[A-Z]', password))
    digits = len(re.findall(r'[0-9]', password))
    special_chars = len(re.findall(r'[^a-zA-Z0-9]', password))

    pool_size = 0
    if lower_chars > 0:
        pool_size += 26
    if upper_chars > 0:
        pool_size += 26
    if digits > 0:
        pool_size += 10
    if special_chars > 0:
        pool_size += 33  
    
    if pool_size == 0:
        return 0
    
    password_length = len(password)
    entropy = password_length * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

def evaluate_strength(password):
    """Evaluate password strength based on various factors"""
    score = 0
    feedback = []
    
  
    length = len(password)
    if length >= 12:
        score += 25
        feedback.append("✅ Good length")
    elif length >= 8:
        score += 15
        feedback.append("⚠️ Decent length, but longer is better")
    else:
        score += 5
        feedback.append("❌ Too short - use at least 8 characters")
    
    
    if re.search(r'[a-z]', password):
        score += 10
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
        
    if re.search(r'[A-Z]', password):
        score += 10
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")
        
    if re.search(r'[0-9]', password):
        score += 10
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Missing numbers")
        
    if re.search(r'[^a-zA-Z0-9]', password):
        score += 15
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")
    
  
    if re.search(r'(.)\1\1', password):
        score -= 10
        feedback.append("❌ Contains repeating characters")
    
    if re.search(r'(abcdef|qwerty|password|123456|admin)', password.lower()):
        score -= 15
        feedback.append("❌ Contains common patterns")
    
    entropy = calculate_entropy(password)
    if entropy >= 80:
        score += 30
    elif entropy >= 60:
        score += 20
    elif entropy >= 40:
        score += 10
    
  
    if score >= 80:
        rating = "Very Strong"
        color = "green"
    elif score >= 60:
        rating = "Strong"
        color = "lightgreen"
    elif score >= 40:
        rating = "Moderate"
        color = "orange"
    elif score >= 20:
        rating = "Weak"
        color = "red"
    else:
        rating = "Very Weak"
        color = "darkred"
    
    time_to_crack = estimate_crack_time(entropy)
    
    return {
        "score": score,
        "rating": rating,
        "color": color,
        "entropy": entropy,
        "feedback": feedback,
        "time_to_crack": time_to_crack
    }

def estimate_crack_time(entropy):
    """Estimate time to crack password based on entropy"""

    if entropy <= 0:
        return "Instantly"
    
    guesses = 2 ** entropy
    seconds = guesses / (10 ** 12)
    
    if seconds < 1:
        return "Instantly"
    elif seconds < 60:
        return f"{seconds:.1f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.1f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.1f} hours"
    elif seconds < 2592000:
        return f"{seconds/86400:.1f} days"
    elif seconds < 31536000:
        return f"{seconds/2592000:.1f} months"
    elif seconds < 3153600000:
        return f"{seconds/31536000:.1f} years"
    else:
        return f"{seconds/31536000:.0f} years"

def main():
    st.set_page_config(
        page_title="Password Strength Calculator",
        page_icon="🔒",
        initial_sidebar_state="collapsed",
    )
    
    st.title("🔒 Password Strength Calculator")
    st.markdown("""
    Enter a password to check its strength. 
    This tool analyzes various factors like length, character variety, and entropy.
    """)
    
    password = st.text_input("Enter a password:", type="password")
    
    show_password = st.checkbox("Show password")
    if show_password and password:
        st.code(password)
    
    if password:
        result = evaluate_strength(password)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Strength Score", f"{result['score']}/100")
        with col2:
            st.metric("Rating", result['rating'])
        with col3:
            st.metric("Entropy", f"{result['entropy']:.1f} bits")
        
       
        st.progress(min(result['score']/100, 1.0))
        st.markdown(f"<h3 style='color: {result['color']}'>Password Rating: {result['rating']}</h3>", unsafe_allow_html=True)
        
        st.subheader("Estimated Time to Crack:")
        st.info(f"{result['time_to_crack']}")
        
        st.subheader("Feedback:")
        for item in result['feedback']:
            st.markdown(f"- {item}")
        
        st.subheader("Recommendations:")
        st.markdown("""
        - Use at least 12 characters
        - Include uppercase & lowercase letters, numbers, and special characters
        - Avoid common patterns and repeated characters
        - Consider using a password manager to generate and store strong passwords
        """)
    
    st.markdown("---")
    st.caption("This tool is for educational purposes only. Never enter real passwords you use.")

if __name__ == "__main__":
    main()