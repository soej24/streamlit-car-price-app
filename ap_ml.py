import streamlit as st
import numpy as np
import sklearn
import joblib


def run_ml() :
    st.subheader('자동차 구매 가능 금액 예측')

    # print(sklearn.__version__) sklearn 버젼 확인

    # 예측하기 위해서 필요한 파일들을 불러와야 한다.
    # 이 예에서는 인공지능파일, X 스케일러 파일, Y 스케일러 파일 3개를 불러와야 한다.

    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    # 성별, 나이, 연봉, 카드빚, 자산을 입력받도록 만드세요.

    gender = st.radio('셩별 입력', ['남자', '여'])
    if gender == '여자' :
        gender = 0;
    else :
        gender =1;

    age = st.number_input('나이를 입력', 0, 120)
    salary = st.number_input('연봉을 입력', 0)
    debt = age = st.number_input('카드빚 입력', 0)    
    worth = age = st.number_input('자산을 입력', 0)    

    if st.button('자동차 구매 금액 예측') :

        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([gender, age, salary, debt, worth]) # 유저가 입력한 것은 변수에 저장되어 있음

        # 2. 학습할때 사용한 X 의 피처 스케일러를 이용해서, 피처스케일링 한다.
        # 먼저 데이터를 2차원으로 만들어 준다.
        new_data = new_data.reshape(1,5)
        new_data = scaler_X.transform( new_data )

        # 3. 인공지능에게 예측해달라고 한다.
        y_pred = regressor.predict(new_data)

        # 4. 예측한 값을, 원상복구 시킨다.
        y_pred = scaler_y.inverse_transform(y_pred)

        y_pred = round(y_pred[0,0])

        st.write( '이 사람의 구매 가능 금액은' + str(y_pred) + '달라입니다.')