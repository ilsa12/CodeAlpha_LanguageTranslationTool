import streamlit as st
from deep_translator import GoogleTranslator
import pyttsx3
import pyperclip

# Text-to-speech engine
tts_engine = pyttsx3.init()

# Streamlit UI
st.title("🌐 Language Translation Tool")

text = st.text_area("Enter text to translate:")

languages = [
    "english", "urdu", "german", "spanish", "french",
    "chinese", "arabic", "hindi", "russian", "japanese"
]

src_lang = st.selectbox("Select source language", languages)
tgt_lang = st.selectbox("Select target language", languages)

if st.button("Translate"):
    if text:
        try:
            translated = GoogleTranslator(source=src_lang, target=tgt_lang).translate(text)
            st.success(f"Translated Text:\n{translated}")

            # Copy button
            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(translated)
                st.info("Copied to clipboard!")

            # Speak button
            if st.button("🔊 Speak Out"):
                tts_engine.say(translated)
                tts_engine.runAndWait()
        except Exception as e:
            st.error(f"Translation failed: {e}")
    else:
        st.warning("Please enter some text to translate.")
