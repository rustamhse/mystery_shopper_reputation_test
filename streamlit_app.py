import streamlit as st

# Метрики
m_reg_period = 219
m_task_duration_sec = 311
m_shops = 6
m_templates = 5
m_rewarded_tasks = 27
m_days_from_last_activity = 75
m_tts_tickets = 2

w_reg_period = 10
w_task_duration_sec = 25
w_shops = 15
w_templates = 10
w_rewarded_tasks = 20
w_days_from_last_activity = 10
w_tts_tickets = 10

norm = 0.5

st.title("Репутация пользователя в КТП")

actual_reg_period = st.slider("Сколько я дней в КТП?", 0, 365, 1)
actual_task_duration_sec = st.slider("Сколько секунд я в среднем трачу на проверку? (За последние 30 дней)", 0, 600, 30)
actual_shops = st.slider("Сколько магазинов я обошёл? (За последние 30 дней)", 0, 20, 1)
actual_templates = st.slider("Сколько видов различных проверок я выполнил? (За последние 30 дней)", 0, 20, 5)
actual_rewarded_tasks = st.slider("Сколько моих анкет приняли? (За последние 30 дней)", 0, 100, 10)
actual_days_from_last_activity = st.slider("Сколько дней прошло с последней проверки?", 1, 100, 30)
actual_tts_tickets = st.slider("Сколько TTS-тикетов было создано по моим анкетам? (За последние 30 дней)", 0, 10, 0)

total_reg_period          = norm / m_reg_period          * w_reg_period          * actual_reg_period
total_task_duration_sec   = norm / m_task_duration_sec   * w_task_duration_sec   * actual_task_duration_sec
total_shops               = norm / m_shops               * w_shops               * actual_shops
total_templates           = norm / m_templates           * w_templates           * actual_templates
total_rewarded_tasks      = norm / m_rewarded_tasks      * w_rewarded_tasks      * actual_rewarded_tasks
raw_days_score = 5 * (m_days_from_last_activity / actual_days_from_last_activity)
total_days_from_activity = min(10, max(0, raw_days_score))
total_tts_tickets         = norm / m_tts_tickets         * w_tts_tickets         * actual_tts_tickets

score = (
    total_reg_period
  + total_task_duration_sec
  + total_shops
  + total_templates
  + total_rewarded_tasks
  + total_days_from_activity
  + total_tts_tickets
)

st.metric("Мой уровень репутации: ", f"{score:.2f}")