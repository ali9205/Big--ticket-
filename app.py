import streamlit as st
import pandas as pd
import numpy as np

# إعداد الصفحة
st.set_page_config(page_title="Big Ticket AI Analyzer", page_icon="🎫")

st.title("🎫 مُحلل Big Ticket الذكي")
st.markdown("---")

# وظيفة لمحاكاة البيانات التاريخية (يمكنك تحديثها لاحقاً بملف CSV حقيقي)
def get_mock_history():
    # عينة لأرقام فازت سابقاً (أرقام عشوائية كمثال)
    return [504321, 128990, 334567, 98122, 445671, 221009, 156743, 398221]

history = get_mock_history()

# واجهة المستخدم
st.subheader("🔍 أدخل أرقام التذاكر المتاحة")
tickets_input = st.text_input("أدخل الأرقام مفصولة بفاصلة (مثال: 123456, 654321)", "")

if tickets_input:
    try:
        available_tickets = [t.strip() for t in tickets_input.split(',')]
        results = []
        
        # تحليل إحصائي بسيط بناءً على المتوسط وتوزيع الخانات
        mean_hist = np.mean(history)
        
        for ticket_str in available_tickets:
            ticket = int(ticket_str)
            # حساب درجة القرب من النمط التاريخي
            distance_score = 100 - (abs(ticket - mean_hist) / mean_hist * 100)
            
            # تحليل الخانة الأخيرة (غالباً ما يراقبها اللاعبون)
            last_digit = ticket_str[-1]
            
            results.append({
                "رقم التذكرة": ticket_str,
                "درجة التوافق الإحصائي": f"{max(0, min(99, distance_score)):.2f}%",
                "الخانة الأخيرة": last_digit
            })
        
        # ترتيب النتائج حسب الأعلى توافقاً
        df_results = pd.DataFrame(results).sort_values(by="درجة التوافق الإحصائي", ascending=False)
        
        st.write("### 🏆 الترتيب المقترح:")
        st.table(df_results)
        
        st.info("💡 نصيحة: التذاكر ذات النسبة الأعلى هي الأقرب لمتوسط أرقام الفوز التاريخية.")
        
    except ValueError:
        st.error("يرجى التأكد من إدخال أرقام صحيحة فقط.")

st.markdown("---")
st.caption("هذا التطبيق للأغراض التحليلية فقط ولا يضمن الفوز.")
