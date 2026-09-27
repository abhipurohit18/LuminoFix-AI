import streamlit as st
from PIL import Image
import random

# Page Configuration
st.set_page_config(page_title="LuminoFix AI", page_icon="💡", layout="centered")

# Header Section
st.title("💡 LuminoFix AI")
st.subheader("Smart Street Light Grievance & Triage System")
st.write("Upload a photo of a broken or faulty street light. Our AI will automatically analyze its severity and route the report to the municipal authority.")

# Sidebar - Simulated Municipal Admin Dashboard
st.sidebar.header("📊 Municipal Dashboard")
st.sidebar.metric(label="Total Complaints Today", value="18")
st.sidebar.metric(label="Resolved", value="12")
st.sidebar.metric(label="Pending", value="6")

# Main Complaint Form
with st.form("complaint_form"):
    st.markdown("### 📝 Report a Fault")
    
    # 1. Image Upload
    uploaded_file = st.file_uploader("Upload a clear photo of the street light", type=["jpg", "jpeg", "png"])
    
    # 2. Location Details
    col1, col2 = st.columns(2)
    with col1:
        area_name = st.text_input("Area / Locality Name", placeholder="e.g., Pratap Nagar, Udaipur")
    with col2:
        landmark = st.text_input("Nearby Landmark", placeholder="e.g., Near Main Square")
        
    # Submit Button
    submit_button = st.form_submit_button("Submit to Authority")

# Processing after submission
if submit_button:
    if uploaded_file is not None and area_name != "":
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Street Light Photo", use_container_width=True)
        
        with st.spinner("AI model is analyzing the photo and location..."):
            # Simulated AI Triage (You can integrate real Gemini API here later)
            severities = [
                ("🔴 High Priority (Exposed live wires / Complete darkness)", "Immediate Action Required"),
                ("🟡 Medium Priority (Intermittent flickering / Low light)", "Scheduled for 24 Hours"),
                ("🟢 Low Priority (Dim lighting)", "Scheduled for 3 Days")
            ]
            selected_severity, action_time = random.choice(severities)
            
            # Simulated Duplicate Check
            is_duplicate = random.choice([True, False])
            
        # Success Message
        st.success("🎉 Complaint registered successfully!")
        
        # AI Triage Report Display
        st.markdown("---")
        st.markdown("### 🤖 AI Analysis & Priority Report")
        st.write(f"- **Location:** {area_name} ({landmark})")
        st.write(f"- **Severity Level:** {selected_severity}")
        st.write(f"- **Estimated Resolution Time:** {action_time}")
        
        if is_duplicate:
            st.warning("⚠️ **Note:** A similar complaint for this pole/area has already been logged. Your report has been merged with the existing ticket to prevent redundancy.")
        else:
            st.info("✨ This is a new complaint. An alert has been dispatched to the concerned municipal ward officer.")
            
    else:
        st.error("⚠️ Please upload a photo and fill in the area name before submitting!")