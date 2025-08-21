import streamlit as st
import random

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="🍴 랜덤 점심 추천기",
    page_icon="🍜",
)

# 8 & 9. 버튼 스타일링을 위한 CSS 코드 주입 (수정된 버전)
st.markdown("""
<style>
    /* 각 버튼을 감싸는 컬럼(div)을 flex 컨테이너로 만들어 내부 아이템(버튼)을 가운데 정렬합니다. */
    div[data-testid="stHorizontalBlock"] > div {
        display: flex;
        justify-content: center;
    }

    /* 버튼 자체의 스타일 */
    div[data-testid="stHorizontalBlock"] button {
        font-size: 18px !important;
        border-radius: 10px !important;
        height: 3em;
        padding: 0 2em !important; /* 버튼 너비가 내용에 맞게 조절되도록 좌우 패딩을 추가합니다. */
        border: 1px solid #CCCCCC !important; /* 테두리 추가 */
        transition: background-color 0.3s ease; /* 부드러운 색상 전환 효과 */
        background-color: #F5F5F5 !important; /* 아이보리 계열의 밝은 회색 */
        color: #333333 !important;            /* 어두운 회색 글씨 */
    }
    
    /* 마우스를 올렸을 때의 스타일 */
    div[data-testid="stHorizontalBlock"] button:hover {
        background-color: #E0E0E0 !important; /* 호버 시 약간 어둡게 */
    }

    /* 비활성화된 버튼 스타일 */
    div[data-testid="stHorizontalBlock"] button:disabled {
        background-color: #FAFAFA !important;
        color: #BDBDBD !important;
        border-color: #EEEEEE !important;
        cursor: not-allowed !important;
    }
</style>
""", unsafe_allow_html=True)


# 2. 상단 제목 및 부제목
st.title("🍴 오늘 뭐 먹지?")
st.write("버튼을 눌러 오늘의 점심 메뉴를 랜덤으로 추천받아보세요!")


# 4. 각 카테고리별 메뉴 데이터 (유사 메뉴 추천을 위한 'tags'와 'description' 추가)
menu_data = {
    '한식': [
        {'name': '김치찌개', 'tags': ['찌개', '국물', '매콤'], 'description': '돼지고기와 김치를 넣어 얼큰하게 끓인 한국의 대표적인 찌개입니다.'},
        {'name': '비빔밥', 'tags': ['밥', '야채'], 'description': '밥 위에 여러 가지 나물, 고기, 계란 등을 올려 고추장이나 간장으로 비벼 먹는 음식입니다.'},
        {'name': '불고기', 'tags': ['고기', '볶음', '달콤'], 'description': '얇게 썬 소고기를 간장 양념에 재워 구워 먹는 달콤한 맛의 요리입니다.'},
        {'name': '삼겹살', 'tags': ['고기', '구이'], 'description': '돼지고기의 삼겹살 부위를 불판에 구워 쌈 채소와 함께 즐기는 인기 메뉴입니다.'},
        {'name': '제육볶음', 'tags': ['고기', '볶음', '매콤'], 'description': '얇게 썬 돼지고기를 고추장 양념에 볶아낸 매콤한 음식입니다.'},
        {'name': '갈비탕', 'tags': ['탕', '국물', '고기'], 'description': '소갈비를 푹 끓여 만든 맑고 진한 국물의 탕 요리입니다.'},
        {'name': '순두부찌개', 'tags': ['찌개', '국물', '매콤'], 'description': '부드러운 순두부를 넣어 얼큰하게 끓인 찌개입니다.'},
        {'name': '된장찌개', 'tags': ['찌개', '국물', '구수'], 'description': '된장을 풀어 각종 채소, 두부, 고기 등을 넣고 끓인 구수한 찌개입니다.'},
        {'name': '보쌈', 'tags': ['고기', '수육'], 'description': '돼지고기를 삶아 얇게 썰어 김치나 쌈장과 함께 먹는 요리입니다.'},
        {'name': '낙지볶음', 'tags': ['해산물', '볶음', '매콤'], 'description': '낙지를 매콤한 양념에 채소와 함께 볶아낸 요리입니다.'},
        {'name': '뼈해장국', 'tags': ['탕', '국물', '고기'], 'description': '돼지 등뼈를 푹 고아 만든 얼큰하고 든든한 국밥입니다.'},
        {'name': '설렁탕', 'tags': ['탕', '국물', '고기'], 'description': '소의 뼈와 고기를 오랜 시간 끓여 만든 뽀얀 국물의 탕입니다.'},
        {'name': '닭볶음탕', 'tags': ['탕', '고기', '매콤'], 'description': '닭고기를 감자, 당근 등과 함께 매콤한 양념에 졸여 만든 요리입니다.'},
    ],
    '중식': [
        {'name': '짜장면', 'tags': ['면', '소스'], 'description': '춘장에 볶은 돼지고기와 채소를 면 위에 올려 비벼 먹는 한국식 중화요리입니다.'},
        {'name': '짬뽕', 'tags': ['면', '국물', '매콤', '해산물'], 'description': '각종 해산물과 채소를 매콤하게 끓인 국물에 면을 말아 먹는 요리입니다.'},
        {'name': '마파두부', 'tags': ['밥', '소스', '매콤'], 'description': '다진 고기와 두부를 매콤한 두반장 소스에 볶아 밥과 함께 먹는 사천 요리입니다.'},
        {'name': '탕수육', 'tags': ['고기', '튀김', '소스', '달콤'], 'description': '돼지고기를 튀겨 새콤달콤한 소스를 부어 먹는 인기 중화요리입니다.'},
        {'name': '깐풍기', 'tags': ['고기', '튀김', '소스', '매콤'], 'description': '닭고기를 튀겨 매콤하고 새콤한 소스에 볶아낸 요리입니다.'},
        {'name': '꿔바로우', 'tags': ['고기', '튀김', '소스', '달콤'], 'description': '넓적한 돼지고기 튀김에 새콤달콤한 소스를 곁들인 중국 동북 지방의 요리입니다.'},
        {'name': '유산슬', 'tags': ['볶음', '해산물'], 'description': '가늘게 채 썬 고기와 해산물, 채소를 볶아 만든 부드러운 요리입니다.'},
        {'name': '양장피', 'tags': ['야채', '해산물', '소스'], 'description': '다양한 채소, 해산물, 고기를 전분으로 만든 피와 함께 겨자 소스에 비벼 먹는 냉채 요리입니다.'},
        {'name': '볶음밥', 'tags': ['밥', '볶음'], 'description': '밥에 계란, 채소, 고기 등을 넣고 기름에 볶아 만든 간단한 식사 메뉴입니다.'},
        {'name': '딤섬', 'tags': ['만두'], 'description': '전분 피에 고기나 해산물 소를 넣어 쪄낸 작은 만두 요리입니다.'},
        {'name': '마라탕', 'tags': ['탕', '국물', '매콤'], 'description': '얼얼하고 매운 맛의 국물에 원하는 재료를 넣어 끓여 먹는 탕 요리입니다.'},
        {'name': '고추잡채', 'tags': ['볶음', '고기', '야채'], 'description': '피망과 돼지고기를 길게 채 썰어 볶은 요리로, 주로 꽃빵과 함께 먹습니다.'},
        {'name': '울면', 'tags': ['면', '국물', '해산물'], 'description': '해산물과 채소를 넣은 걸쭉한 국물에 면을 말아 먹는 부드러운 중화요리입니다.'},
    ],
    '일식': [
        {'name': '초밥', 'tags': ['밥', '날것', '해산물'], 'description': '식초로 간을 한 밥 위에 신선한 생선이나 해산물을 올려 만든 일본의 대표 요리입니다.'},
        {'name': '라멘', 'tags': ['면', '국물', '고기'], 'description': '돼지뼈나 닭뼈로 우린 국물에 면과 다양한 고명을 올려 먹는 일본식 면 요리입니다.'},
        {'name': '돈카츠', 'tags': ['고기', '튀김'], 'description': '두툼한 돼지고기에 빵가루를 입혀 튀겨낸 일본식 커틀릿입니다.'},
        {'name': '우동', 'tags': ['면', '국물'], 'description': '굵고 쫄깃한 면발을 따뜻한 국물과 함께 먹는 일본의 대중적인 면 요리입니다.'},
        {'name': '가라아게', 'tags': ['고기', '튀김'], 'description': '닭고기를 간장 양념에 재워 전분을 묻혀 튀겨낸 일본식 닭튀김입니다.'},
        {'name': '가츠동', 'tags': ['밥', '고기', '튀김', '덮밥'], 'description': '돈카츠를 소스와 함께 끓여 계란을 풀고 밥 위에 얹어 먹는 덮밥 요리입니다.'},
        {'name': '오야코동', 'tags': ['밥', '고기', '덮밥'], 'description': '닭고기와 양파를 간장 소스에 익혀 계란을 풀고 밥 위에 얹은 덮밥입니다.'},
        {'name': '규동', 'tags': ['밥', '고기', '덮밥'], 'description': '얇게 썬 소고기를 양파와 함께 달콤한 간장 소스에 졸여 밥 위에 얹은 덮밥입니다.'},
        {'name': '타코야키', 'tags': ['해산물', '간식'], 'description': '문어를 넣은 밀가루 반죽을 동그랗게 구워 소스와 가쓰오부시를 뿌려 먹는 간식입니다.'},
        {'name': '사시미', 'tags': ['날것', '해산물'], 'description': '신선한 생선을 얇게 썰어 간장에 찍어 먹는 일본식 회 요리입니다.'},
        {'name': '메밀소바', 'tags': ['면', '차가운'], 'description': '메밀로 만든 면을 차가운 간장 육수에 찍어 먹는 시원한 면 요리입니다.'},
        {'name': '오코노미야키', 'tags': ['부침', '소스'], 'description': '밀가루 반죽에 양배추, 고기, 해산물 등을 넣고 철판에 부쳐 먹는 일본식 부침개입니다.'},
        {'name': '텐동', 'tags': ['밥', '튀김', '덮밥'], 'description': '밥 위에 다양한 종류의 튀김을 올리고 간장 소스를 뿌려 먹는 덮밥입니다.'},
    ],
    '양식': [
        {'name': '파스타', 'tags': ['면', '소스'], 'description': '밀가루 반죽으로 만든 면을 다양한 소스와 함께 조리한 이탈리아 요리입니다.'},
        {'name': '피자', 'tags': ['빵', '치즈'], 'description': '얇은 도우 위에 토마토 소스, 치즈, 다양한 토핑을 올려 구운 이탈리아의 대표 요리입니다.'},
        {'name': '스테이크', 'tags': ['고기', '구이'], 'description': '두툼하게 썬 소고기를 그릴이나 팬에 구워낸 서양식 육류 요리입니다.'},
        {'name': '햄버거', 'tags': ['빵', '고기', '패스트푸드'], 'description': '구운 고기 패티를 동그란 빵 사이에 채소, 소스와 함께 넣어 만든 음식입니다.'},
        {'name': '리조또', 'tags': ['밥', '치즈'], 'description': '쌀을 버터나 오일에 볶다가 육수를 부어 졸여 만든 이탈리아식 쌀 요리입니다.'},
        {'name': '치킨샐러드', 'tags': ['야채', '고기'], 'description': '신선한 채소 위에 구운 닭가슴살과 드레싱을 곁들인 가벼운 식사입니다.'},
        {'name': '라자냐', 'tags': ['면', '치즈', '소스'], 'description': '넓적한 파스타 면 사이에 고기 소스와 치즈를 겹겹이 쌓아 오븐에 구운 요리입니다.'},
        {'name': '까르보나라', 'tags': ['면', '소스', '치즈'], 'description': '계란, 치즈, 베이컨을 이용해 만든 고소하고 크리미한 파스타입니다.'},
        {'name': '오믈렛', 'tags': ['계란', '밥'], 'description': '계란을 풀어 부친 요리로, 안에 치즈나 채소 등 다양한 재료를 넣을 수 있습니다.'},
        {'name': '스프', 'tags': ['국물'], 'description': '고기, 채소 등을 끓여 만든 국물 요리로, 식전 애피타이저로 즐겨 먹습니다.'},
        {'name': '감바스 알 아히요', 'tags': ['해산물', '오일'], 'description': '새우와 마늘을 올리브 오일에 끓여낸 스페인의 대표적인 타파스 요리입니다.'},
        {'name': '필라프', 'tags': ['밥', '볶음'], 'description': '쌀을 버터에 볶은 후 육수를 부어 지은 볶음밥의 일종입니다.'},
        {'name': '클램차우더', 'tags': ['국물', '해산물'], 'description': '조갯살과 감자, 양파 등을 넣어 끓인 크리미한 미국의 스프 요리입니다.'},
    ],
    '분식': [
        {'name': '떡볶이', 'tags': ['떡', '매콤', '소스'], 'description': '떡을 고추장 양념에 어묵, 채소와 함께 끓여 먹는 한국의 대표적인 길거리 음식입니다.'},
        {'name': '순대', 'tags': ['분식'], 'description': '돼지 창자에 당면, 채소, 선지 등을 채워 쪄낸 음식입니다.'},
        {'name': '오뎅', 'tags': ['국물', '분식'], 'description': '생선 살을 갈아 만든 어묵을 꼬치에 꿰어 따뜻한 국물과 함께 먹는 음식입니다.'},
        {'name': '튀김', 'tags': ['튀김', '분식'], 'description': '오징어, 새우, 채소 등에 튀김옷을 입혀 기름에 튀겨낸 간식입니다.'},
        {'name': '김밥', 'tags': ['밥', '분식'], 'description': '밥과 다양한 재료를 김으로 말아 만든 간편한 식사 메뉴입니다.'},
        {'name': '라볶이', 'tags': ['떡', '면', '매콤', '소스'], 'description': '라면과 떡볶이를 함께 끓여 더욱 푸짐하게 즐기는 음식입니다.'},
        {'name': '핫도그', 'tags': ['빵', '튀김', '간식'], 'description': '소시지를 꼬치에 꿰어 밀가루 반죽을 입혀 튀긴 후 설탕과 케첩을 뿌려 먹는 간식입니다.'},
        {'name': '치즈볼', 'tags': ['치즈', '튀김', '간식'], 'description': '동그란 빵 안에 모짜렐라 치즈가 가득 들어있는 달콤하고 짭짤한 튀김 간식입니다.'},
        {'name': '쫄면', 'tags': ['면', '매콤', '야채'], 'description': '쫄깃한 면발을 매콤새콤한 양념장에 채소와 함께 비벼 먹는 분식 메뉴입니다.'},
        {'name': '계란빵', 'tags': ['빵', '계란', '간식'], 'description': '빵 반죽 위에 계란 하나를 통째로 올려 구운 달콤하고 고소한 길거리 간식입니다.'},
        {'name': '라면', 'tags': ['면', '국물'], 'description': '인스턴트 면을 뜨거운 물에 끓여 먹는 가장 대중적인 간편식입니다.'},
        {'name': '만두', 'tags': ['만두', '분식'], 'description': '다진 고기와 채소를 밀가루 피에 싸서 찌거나 구워 먹는 음식입니다.'},
        {'name': '주먹밥', 'tags': ['밥', '분식'], 'description': '밥에 여러 재료를 섞어 손으로 동글게 뭉쳐 만든 간편한 식사입니다.'},
    ]
}

# 화면에 표시될 카테고리 이름 (데이터 키와 표시 텍스트 분리)
category_display = {
    '한식': '한식 🍚', '중식': '중식 🥡', '일식': '일식 🍣',
    '양식': '양식 🍝', '분식': '분식 🍢'
}
# 표시 이름으로 실제 키를 찾기 위한 역방향 맵
category_map_reverse = {v: k for k, v in category_display.items()}


# 세션 상태 초기화
if 'recommended_menu_obj' not in st.session_state:
    st.session_state.recommended_menu_obj = None
if 'selected_category_key' not in st.session_state:
    st.session_state.selected_category_key = list(menu_data.keys())[0]

# 추천 함수
def recommend_menu(category_key):
    """선택된 카테고리에서 메뉴 객체를 랜덤으로 추천하는 함수"""
    menu_obj = random.choice(menu_data[category_key])
    st.session_state.recommended_menu_obj = menu_obj
    st.session_state.selected_category_key = category_key

# 3. 카테고리 선택 (selectbox)
st.subheader("1. 원하는 음식 카테고리를 선택하세요.")
selected_display_name = st.selectbox(
    "카테고리 선택",
    options=list(category_display.values()),
    label_visibility="collapsed"
)
# 사용자가 선택한 표시 이름(e.g., '한식 🍚')으로 실제 데이터 키(e.g., '한식')를 찾습니다.
selected_category_key = category_map_reverse[selected_display_name]


st.write("---")

# 5 & 7. "추천 받기"와 "다시 추천" 버튼
st.subheader("2. 버튼을 눌러 메뉴를 추천받으세요.")
col1, col2 = st.columns(2)

with col1:
    if col1.button("추천 받기 🎲"):
        recommend_menu(selected_category_key)

with col2:
    if col2.button("다시 추천 🔄", disabled=(st.session_state.recommended_menu_obj is None)):
        recommend_menu(st.session_state.selected_category_key)

# 6. 추천 결과 및 유사 메뉴 표시
if st.session_state.recommended_menu_obj:
    st.write("---")
    
    recommended_menu = st.session_state.recommended_menu_obj
    category_key = st.session_state.selected_category_key
    
    display_name = category_display[category_key]
    emoji = display_name.split(' ')[1] if ' ' in display_name else '😋'

    # 메인 추천 메뉴 표시
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h3>오늘의 추천 메뉴는...</h3>
            <p style="font-size: 32px; font-weight: bold;">
                👉 {recommended_menu['name']} {emoji}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # 추천 메뉴에 대한 간단한 설명 (expander 사용)
    with st.expander(f"**{recommended_menu['name']}**은(는) 어떤 음식인가요? 🤔"):
        st.write(recommended_menu.get('description', '아직 설명이 준비되지 않았어요.'))

    # 유사 메뉴 찾기 및 표시
    recommended_tags = set(recommended_menu['tags'])
    all_menus_in_category = menu_data[category_key]
    
    similar_menus = []
    for menu in all_menus_in_category:
        if menu['name'] != recommended_menu['name']:
            if not recommended_tags.isdisjoint(menu['tags']):
                similar_menus.append(menu['name'])
    
    if similar_menus:
        st.write("---")
        st.subheader("🤔 이런 메뉴는 어떠세요?")
        
        num_to_show = min(len(similar_menus), 3)
        suggestions = random.sample(similar_menus, num_to_show)
        
        cols = st.columns(num_to_show)
        for i, suggestion in enumerate(suggestions):
            with cols[i]:
                st.info(f"**{suggestion}**")

