import streamlit as st

# 타이틀
st.title("안녕하세요. 스파르타 코딩클럽입니다.")
st.title('스마일 :sunglass:')

st.header("헤더입니다.")

st.subheader("이것은 subheader")

st.caption("캡션을 한번 넣어보겠습니다.")

sample_code = '''def function(): print("Hello World)'''

st.code(sample_code, language)