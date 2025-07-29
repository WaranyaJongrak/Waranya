import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

def generate_text(prompt):
    # คำหลักที่เกี่ยวกับดอกไม้
    flower_keywords = [
        "ดอกไม้", "ช่อดอกไม้", "แจกัน", "กลิ่นหอม", "ร้านดอกไม้",
        "ดอกกุหลาบ", "ดอกลิลลี่", "จัดดอกไม้", "บูเก้", "ฟลอริสต์","ดอก"
    ]

    # ตรวจสอบว่ามีคำที่เกี่ยวกับดอกไม้หรือไม่
    if not any(keyword in prompt.lower() for keyword in flower_keywords):
        return "🌸 ขอโทษค่ะ ฉันเป็นผู้ช่วยร้านดอกไม้ ฉันสามารถช่วยตอบคำถามเกี่ยวกับดอกไม้ได้เท่านั้นนะคะ 😊"

    # ถ้าเกี่ยวข้องกับดอกไม้ ก็ให้โมเดลตอบ
    full_prompt = f"คุณเป็นพนักงานร้านขายดอกไม้ที่สุภาพและเชี่ยวชาญ ช่วยตอบคำถามต่อไปนี้อย่างมืออาชีพ: {prompt}"
    response = model.generate_content(full_prompt)
    return response.text
