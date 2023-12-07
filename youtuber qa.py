import time, os

# 프로그램이 종료되지 않고 실행, 파일을 가져와서 지울때
# pip install gTTS
# pip install playsound==1.2.2
# pip install SpeechRecognition
# Pip install PyAudio

import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


# 음성 인식 (듣기)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language="ko")
        print("[이해현] " + text)
        answer(text)
    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError as e:
        print("요청 실패 : {0}".format(e))  # Api Key 오류, 네트워크 단절 등


# 대답
def answer(input_text):
    answer_text = ""
    if "무엇을" in input_text:
        answer_text = "유튜버 조코딩이라는 사람에 대해 알아볼 거라고 하셨습니다."
    elif "누구니" in input_text:
        answer_text = (
            "본명 조동근, 고려대학교 생명과학대학 환경생태공학을 전공했으며 첫 업로드는 2019년 2월 20일로써 현재진행중인 유튜버입니다."
        )
    elif "주력" in input_text:
        answer_text = "코딩의 기초와 웹, 앱 프로그래밍을 컨텐츠가 주력 컨텐츠입니다."
    elif "고마워" in input_text:
        answer_text = "별 말씀을요. 또 궁금하신 사항이 있다면 언제든지 물어봐주세요!"
    elif "끝낼게" in input_text:
        answer_text = "다음에 또 만나요~"
        stop_listening(wait_for_stop=False)  # 더 이상 듣지 않음
    else:
        answer_text = "다시 한번 말씀해주시겠어요?"
    speak(answer_text)


# 소리내어 읽기(TTS)
def speak(text):
    print("[조로봇]" + text)
    file_name = "voice.mp3"
    tts = gTTS(text=text, lang="ko")
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):  # voice.mp3 파일 삭제
        os.remove(file_name)


r = sr.Recognizer()
m = sr.Microphone()  # 마이크 인식

speak("무엇을 도와드릴까요?")
stop_listening = r.listen_in_background(m, listen)  # 사람처럼 계속 귀를 열어둔다
# stop_listening(wait_for_stop=False) # 더이상 듣지 않음

while True:
    time.sleep(0.1)
