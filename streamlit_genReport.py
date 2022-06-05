import streamlit as st
import lab_safety_report as bogus
import datetime as dat



st.title('허례는 허식으로 대응함이 인지상정')

d = st.date_input(
     "원하는 날짜를 선택하시오",
     dat.datetime.now())

company= st.text_input('회사명을 입력하시오', '태권브이연구소')
name = st.text_input('실험실명을 입력하시오', '로봇실험실')
buildingNo = st.text_input('건물번호를 입력하시오', '비너스동 ')      
roomNo = st.text_input('방번호를 입력하시오', '뒷간-001') 
safety_manager = st.text_input('안전관리자를 입력하시오', '정우성')   
boss = st.text_input('보스를 입력하시오', '춘리')    


if st.button('만드러버렷!'):
     generator = bogus.lab_safety_report('./template/lab_safety_report_template.docx',
               company=company,
               name=name,
               buildingNo=buildingNo,
               roomNo=roomNo,
               safety_manager=safety_manager,
               boss=boss
          )
     generator.generate(f'./output/{company}_{d.year}_{d.month}.docx', d.year, d.month, d.day)

     with open(f'./output/{company}_{d.year}_{d.month}.docx', 'rb') as file:
          btn = st.download_button(
             label="Download file",
             data=file,
             file_name=f'{company}_{d.year}_{d.month}.docx',
             mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
           )
