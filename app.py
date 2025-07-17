import streamlit as st
from search_agent import get_recommendations

st.set_page_config(page_title="AI Learning Portal", layout="centered")
st.title("🤖 Cisco AI Learning Assistant")

query = st.text_input("What do you want to learn?", placeholder="e.g., ethical hacking, CCNA, data center networking")

if st.button("Get Learning Resources") and query:
    st.info("Fetching learning paths and content…")
    results = get_recommendations(query)
    if results:
        for source, links in results.items():
            st.subheader(source)
            for item in links:
                st.markdown(f"- [{item['title']}]({item['url']})")
    else:
        st.warning("No results found. Try a broader topic.")
