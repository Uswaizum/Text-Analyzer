import streamlit as st

#creating varients
txt=st.text_area (
"Text to analyze",
" ",placeholder="Write Text!",max_chars=100)

#creating a button
analyze_button=st.button('Analyze')

if analyze_button:
    st.write(txt)

 #counting words
    words=txt.split()
    st.write(f"Number of words: {len(words)}")

 #counting characters
    characters=len(txt)
    st.write(f"Number of characters: {characters}")

 #counting sentences
    sentences=txt.split('. ')
    st.write(f"Number of sentences: {len(sentences)}")

 #counting unique words
    unique_words=set(words)
    st.write(f"Number of unique words: {len(unique_words)}")

 #counting vowels
    vowels='aeiouAEIOU'
    vowel_count=sum(1 for char in txt if char in vowels)
    st.write(f"Number of vowels: {vowel_count}")

 #counting consonants
    consonants=sum(1 for char in txt if char not in vowels)
