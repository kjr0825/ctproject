import streamlit as st

# 페이지 설정 (wide로 설정해서 화면 넓게)
st.set_page_config(
    page_title="Juri Webapp",
    layout="wide"
)

# 타이틀
st.title("This is Juri Webapp!!")

# 드롭다운 박스 3개 (Content 1, 2, 3)
with st.expander("Content #1..."):
    st.write("여기에 첫 번째 콘텐츠 내용을 입력하세요.")

with st.expander("Content #2..."):
    st.write("여기에 두 번째 콘텐츠 내용을 입력하세요.")

with st.expander("Content #3..."):
    st.write("여기에 세 번째 콘텐츠 내용을 입력하세요.")

# Tips 드롭다운
with st.expander("Tips.."):
    st.write("여기에 팁이나 참고자료를 입력하세요.")

# Footer (아래 저작권 표시)
st.markdown(
    "<br><hr><p style='text-align:center; color:blue;'>(c)copyright. all rights reserved by skykang</p>",
    unsafe_allow_html=True
)
