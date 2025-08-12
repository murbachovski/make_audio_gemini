import streamlit as st
import asyncio
import concurrent.futures
import os
import base64
import wave
from google import genai
from google.genai import types

GENAI_API_KEY = os.environ['GENAI_API_KEY']

client = genai.Client(api_key=GENAI_API_KEY,
                      http_options={'api_version': 'v1alpha'})

OUTPUT_FILE = "space_sound.wav"
CHANNELS = 1
SAMPLE_WIDTH = 2
FRAME_RATE = 44100

def set_background_image(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}") !important;
            background-size: cover !important;
            background-position: center !important;
            background-repeat: no-repeat !important;
            background-attachment: fixed !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

async def generate_music(duration, prompt_text):
    try:
        async with client.aio.live.music.connect(model='models/lyria-realtime-exp') as session:
            await session.set_weighted_prompts(
                prompts=[types.WeightedPrompt(
                    text=prompt_text,
                    weight=1.0
                )]
            )
            await session.set_music_generation_config(
                config=types.LiveMusicGenerationConfig(bpm=70, temperature=0.8)
            )
            await session.play()

            max_frames = FRAME_RATE * duration
            written_frames = 0

            with wave.open(OUTPUT_FILE, 'wb') as wf:
                wf.setnchannels(CHANNELS)
                wf.setsampwidth(SAMPLE_WIDTH)
                wf.setframerate(FRAME_RATE)

                async for message in session.receive():
                    if written_frames >= max_frames:
                        break

                    if not getattr(message, "server_content", None):
                        continue
                    audio_chunks = getattr(message.server_content, "audio_chunks", None)
                    if not audio_chunks:
                        continue

                    chunk = audio_chunks[0]
                    audio_data = getattr(chunk, "data", None)

                    if isinstance(audio_data, str):
                        audio_data = base64.b64decode(audio_data)
                    elif isinstance(audio_data, memoryview):
                        audio_data = bytes(audio_data)
                    elif audio_data is None:
                        continue

                    frames_in_chunk = len(audio_data) // (CHANNELS * SAMPLE_WIDTH)
                    remaining_frames = max_frames - written_frames

                    if frames_in_chunk > remaining_frames:
                        bytes_to_write = remaining_frames * CHANNELS * SAMPLE_WIDTH
                        wf.writeframes(audio_data[:bytes_to_write])
                        written_frames += remaining_frames
                        break
                    else:
                        wf.writeframes(audio_data)
                        written_frames += frames_in_chunk

        return True
    except Exception as e:
        st.error(f"음악 생성 중 에러 발생: {e}")
        return False

def run_generate_music_sync(duration, prompt_text):
    return asyncio.run(generate_music(duration, prompt_text))

def main():
    set_background_image("./back.jpg")

    st.title("AI 음악 생성 🤖 ")
    
    st.divider()
    
    st.info("음악 스타일을 설명하는 프롬프트를 입력하세요: (영어 입력이 더욱 성능이 좋습니다.)")
    
    prompt_text = st.text_area(
        "",
        value="Ethereal space ambient with dreamy synth pads and soft cosmic textures",
        height=170
    )
    
    st.markdown(
    """
    <style>
    hr {
        border: none;
        border-top: 2px solid orange !important;  /* OO색 실선, 두께 2px */
        margin: 1rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    st.divider()

    st.markdown(
        """
        <style>
        /* st.info 텍스트 색상 변경 */
        div[data-testid="stAlert"] > div {
            color: skyblue !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.info("음악 길이 선택")
    
    # 글자 색상 변경
    st.markdown(
    """
    <style>
    div[role="radiogroup"] label > div {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    option = st.radio("", ("10초", "20초", "30초"))

    st.divider()
    
    if st.button("음악 생성"):
        duration = int(option.replace("초", ""))
        st.info(f"'{prompt_text}' 스타일로 {duration}초 길이 음악 생성 중...")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future = executor.submit(run_generate_music_sync, duration, prompt_text)
            success = future.result()

        if success:
            st.success("음악 생성 완료!")
            st.audio(OUTPUT_FILE)

if __name__ == "__main__":
    main()
