import streamlit as st
import streamlit.components.v1 as htmlviewer  # HTML viewer 모듈

st.set_page_config(layout="wide")
st.title('This is Juri Webapp!!')

# index.html 불러오기 (Content #2 용)
with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()

col1, col2 = st.columns((4, 1))

with col1:
    # ✅ Content #1
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    # ✅ Content #2
    with st.expander('Content #2...'):
        htmlviewer.html(html, height=1000, scrolling=True)

    # ✅ Content #3 (백석 시 감정 분석 HTML만 삽입)
    with st.expander("Content #3: 백석 시 기반 CT 감정 분석 활동"):
        st.markdown("### 🎨 백석 시 감정 분석 및 시각화 활동")

        with open('baekseokct.html', 'r', encoding='utf-8') as f:
            baekseok_html = f.read()

        htmlviewer.html(baekseok_html, height=1100, scrolling=True)

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

# 하단 copyright
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang</font>', unsafe_allow_html=True)
