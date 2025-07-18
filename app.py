import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from story import generate_story_from_captions
#from translate import EnglishToMalayalam
from translate import translate_story
from PIL import Image
import time
import pyperclip

# Streamlit Page Configuration
st.set_page_config(page_title="📖 PICTONARRATE", layout="wide")

# Title and Description
st.title("📖 PICTONARRATE: Series of Images to Story in Malayalam")
st.write("This application extracts **captions from images**, generates a **story in English**, and translates it into **Malayalam**.")

# Initialize BLIP model for image captioning
@st.cache_resource
def load_blip_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip_model()

# Function to generate captions using BLIP
def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)

# Upload Multiple Images
uploaded_files = st.file_uploader("Upload Images", type=["jpg", "png", "jpeg", "webp"], accept_multiple_files=True)

if uploaded_files:
    # Display Images in a Single Row
    st.subheader("📷 Uploaded Images")
    cols = st.columns(len(uploaded_files))
    filenames = []
    captions = []

    progress_bar = st.progress(0)  # Initialize progress bar
    step = 1 / (len(uploaded_files) + 2)  # Adjust step based on tasks

    for i, file in enumerate(uploaded_files):
        image = Image.open(file).convert("RGB")
        filenames.append(file.name)
        cols[i].image(image, width=150, use_column_width=False)

        # Generate Caption with Progress Indicator
        with st.spinner(f"Generating caption for Image {i+1}..."):
            caption = generate_caption(image)
            captions.append(caption)
            time.sleep(1)  # Simulate processing time
        progress_bar.progress(int((i+1) * step * 100))  # Update progress

    # Combine Captions
    combined_caption = ". ".join(captions)

    # Generate Story in English with Progress Indicator
    with st.spinner("Generating story in English..."):
        story = generate_story_from_captions(combined_caption)
        english_story = story[0].replace("<sep>", "").strip()
        time.sleep(2)  # Simulate processing time
    progress_bar.progress(int((len(uploaded_files) + 1) * step * 100))

    # Display Captions
    st.subheader("📖 Extracted Captions")
    for i, caption in enumerate(captions):
        st.write(f"**Image {i+1}:** {caption}")

    # Display & Allow Editing of the Generated English Story
    st.subheader("📖 Generated Story (English)")
    edited_story = st.text_area("Edit the generated story before translation:", value=english_story, height=200)

    # Copy & Download Buttons for English Story
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📋 Copy English Story"):
            pyperclip.copy(edited_story)
            st.success("English story copied to clipboard!")

    with col2:
        st.download_button("📥 Download English Story (TXT)", edited_story, "english_story.txt", "text/plain")

    # Translate to Malayalam Only After User Edits & Clicks Button
    if st.button("🌍 Translate to Malayalam"):
        with st.spinner("Translating to Malayalam..."):
            #malayalam_story = EnglishToMalayalam.translate_story(edited_story)
            malayalam_story = translate_story(edited_story)
            # time.sleep(2)  # Simulate processing time
        progress_bar.progress(100)

        # Display Malayalam Story
        st.subheader("📖 Generated Story (Malayalam)")
        st.info(malayalam_story)

        # Copy & Download Buttons for Malayalam Story
        col3, col4 = st.columns(2)
        with col3:
            if st.button("📋 Copy Malayalam Story"):
                pyperclip.copy(malayalam_story)
                st.success("Malayalam story copied to clipboard!")

        with col4:
            st.download_button("📥 Download Malayalam Story (TXT)", malayalam_story, "malayalam_story.txt", "text/plain")

    # Success Message
    st.success("🎉 Processing completed successfully!")
