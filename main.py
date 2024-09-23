import streamlit as st

st.title('나의 첫 웹 서비스 만들기!!')

# 사용자 입력 받기
name = st.text_input('이름을 입력해주세요 : ')
blood = st.selectbox('혈액형을 선택해주세요:', [
    'A', 'B', 'O', 'AB'
    
])

# blood 설명 데이터 (더 자세히)
blood_data = {
    'A': {
        '특징': ' A형 성격은 경쟁에서 지기 싫어하고 스트레스를 잘 받는 강박적인 성격이 특징인데요 화를 잘 내고, 경쟁적이고, 급하고, 공격적이고, 지배적인 모습들을 보이기도 합니다. '
           
    },
    'B': {
        '특징': '이상주의적이고 감정적인 유형으로, 예술적 감각이 뛰어납니다. '
               '강한 내면의 가치를 지니고 있으며, 다른 사람의 감정을 잘 이해하고 공감합니다. '
               '창의적이고 독창적인 아이디어를 많이 가지고 있으며, 예술이나 문학 분야에서 두각을 나타냅니다.',
        '직업': '작가, 예술가, 상담사, 교사, 음악가',
        '잘 맞는 MBTI': ['ENFJ', 'ESFJ']
    },
    'O': {
        '특징': '천부적인 리더십을 지닌 유형으로, 목표 지향적이고 결정력이 뛰어납니다. '
              
    },
    'AB': {
        '특징': '창의적이고 혁신적인 유형으로, 새로운 아이디어와 도전에 열정적입니다. '
              
        
    },
  
}

if st.button('특징 생성'):
    if blood in blood_data:
        특징 = blood_data[mbti]['특징']
       

        st.write(f"{name}님! 당신의 혈액형 유형은 {blood}입니다!")
        st.write(f"**특징**: {특징}")

    else:
        st.write(f"{name}님! 아직 {blood} 유형에 대한 정보가 없습니다.")
st.bar_chart(data=None, *, x=None, y=None, x_label=many, y_label=A,B,O,AB, color=blue, horizontal=False, stack=1, width=1, height=5, use_container_width=True)

