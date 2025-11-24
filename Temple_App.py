import streamlit as st
import google.generativeai as genai
from temple_data import temples
import os

# Page Configuration
st.set_page_config(
    page_title="Tamil Temple Architecture AI",
    page_icon="🛕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .temple-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f1f1f;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #333;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    /* Style for temple images */
    .stImage > img {
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .stImage > img:hover {
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🛕 Temple Explorer")
    
    # API Key Configuration
    # Try to get API key from Streamlit secrets first
    default_api_key = None
    try:
        if hasattr(st, 'secrets') and "GOOGLE_API_KEY" in st.secrets:
            default_api_key = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass
    
    # Determine which API key to use
    api_key = None
    use_own_key = False
    
    if default_api_key:
        st.success("✅ Default API Key Available")
        use_own_key = st.checkbox("Use my own API key instead", value=False, 
                                   help="Check this if you want to use your own Gemini API key")
        
        if use_own_key:
            user_api_key = st.text_input("Enter Your Gemini API Key", type="password", 
                                        help="Get your key from Google AI Studio")
            if user_api_key:
                api_key = user_api_key
                st.success("🔑 Using your custom API key")
            else:
                st.warning("Please enter your API key or uncheck the box to use the default key")
        else:
            api_key = default_api_key
            st.info("🔑 Using default API key")
    else:
        # No default key available, user must provide their own
        api_key = st.text_input("Enter Gemini API Key", type="password", 
                               help="Get your key from Google AI Studio")
        if api_key:
            st.success("🔑 API Key Configured!")
        else:
            st.warning("⚠️ Please enter your Gemini API Key to use AI features")
    
    # Configure the API key if available
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
        genai.configure(api_key=api_key)
    
    st.markdown("---")
    
    # Temple Selection
    selected_temple_name = st.selectbox(
        "Select a Temple",
        options=list(temples.keys())
    )

# Main Content
if selected_temple_name:
    temple = temples[selected_temple_name]
    
    st.markdown(f'<div class="temple-header">{selected_temple_name}</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Display Temple Image
        image_path = temple.get("image_url", "")
        
        if os.path.exists(image_path):
            st.image(image_path, caption=selected_temple_name, use_container_width=True)
        else:
            # Fallback if image is missing
            st.info(f"Image not available locally: {image_path}")
            
        st.markdown(f"**📍 Location:** {temple['location']}")
        
        # Add a visual separator
        st.markdown("---")
        
    with col2:
        st.markdown('<div class="section-header">📖 History</div>', unsafe_allow_html=True)
        st.write(temple['history'])
        
        st.markdown('<div class="section-header">🏗️ Architecture</div>', unsafe_allow_html=True)
        st.write(temple['architecture'])
        
        st.markdown('<div class="section-header">📝 Description</div>', unsafe_allow_html=True)
        st.write(temple['description'])

    st.markdown("---")
    
    # AI Analysis Section
    st.header("🤖 AI Architecture Analysis")
    
    if st.button("Analyze Architecture with AI"):
        if not api_key:
            st.error("Please configure your Gemini API Key in the sidebar first.")
        else:
            try:
                with st.spinner("Consulting the digital archives..."):
                    model = genai.GenerativeModel('gemini-2.5-flash')
                    
                    prompt = f"""
                    Act as an expert historian and architect specializing in Dravidian and Tamil temple architecture.
                    Analyze the {selected_temple_name} located in {temple['location']}.
                    
                    Please provide a detailed analysis covering:
                    1. **Architectural Style**: Specific details about the era and style (e.g., Chola, Pallava, Pandya).
                    2. **Key Sculptures**: Notable sculptures or carvings and their mythological significance.
                    3. **Engineering Marvels**: Any unique construction techniques used (e.g., shadowless vimana, musical pillars).
                    4. **Cultural Impact**: The temple's significance in Tamil culture and history.
                    
                    Format the output in clear Markdown with headings and bullet points in both English and followed by Tamil.
                    """
                    
                    response = model.generate_content(prompt)
                    st.markdown(response.text)
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

else:
    st.info("Please select a temple from the sidebar to begin.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Google Gemini")
