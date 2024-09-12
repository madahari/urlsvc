# URL 단축 함수
def shorten_url(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# 스트림릿 UI
st.title("URL 줄이기 서비스")

# 사용자 입력
url = st.text_input("URL을 입력하세요")

# 버튼 클릭 시 URL 단축
if st.button("줄이기"):
    if url:
        try:
            short_url = shorten_url(url)
            st.success(f"단축된 URL: {short_url}")
        except Exception as e:
            st.error("URL을 줄이는 중 오류가 발생했습니다. URL을 확인해주세요.")
    else:
        st.warning("URL을 입력해주세요.")
