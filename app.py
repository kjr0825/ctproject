import streamlit as st
import streamlit.components.v1 as htmlviewer  # HTML viewer 모듈 추가

st.title('This is Juri Webapp!!')

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()
    f.close()

col1, col2 = st.columns((4,1))

with col1:
    # Content #1
    with st.expander('Content #1...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content..')
        st.video(url)

    # Content #2
    with st.expander('Content #2...'):
        htmlviewer.html(html, height=1000, scrolling=True)

    # ✅ Content #3 (새로 추가됨!)
    with st.expander('Content #3...'):
        st.subheader("추가된 콘텐츠 영역")
        st.write("이곳에 원하는 설명, 이미지, 위젯 등을 넣을 수 있어요.")
        st.text_input("예: 이름 입력창")
        st.button("클릭해보기")

with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by skykang</font>', unsafe_allow_html=True)
