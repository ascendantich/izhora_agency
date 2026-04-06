<script setup>
import { ref, onMounted } from 'vue'

// Основное состояние формы
const formData = ref({
  name: '',
  phone: '',
  object_id: null 
})

const objectsList = ref([])
const isLoadingObjects = ref(true)
const showSuccessModal = ref(false)

// 1. Загружаем список объектов из БД
const fetchObjects = async () => {
  try {
    isLoadingObjects.value = true
    // Важно: используем адрес из докера или localhost
    const response = await fetch('http://localhost:8000/objects') 
    
    if (response.ok) {
      const data = await response.json()
      objectsList.value = data
      
      // Исправлено: проверяем наличие данных и используем правильный ключ 'id'
      if (data.length > 0) {
        // Пробуем взять id или Object_ID (смотря что пришло с бэка)
        formData.value.object_id = data[0].id || data[0].Object_ID
      }
    }
  } catch (error) {
    console.error('Ошибка загрузки объектов:', error)
  } finally {
    isLoadingObjects.value = false
  }
}

onMounted(() => {
  fetchObjects()
})

// 2. Отправка формы на бэкенд
const submitForm = async () => {
  // Исправлено: берем данные из formData.value
  const payload = {
    full_name: formData.value.name, 
    phone: formData.value.phone,
    object_id: Number(formData.value.object_id) // Гарантируем число
  };

  console.log("Отправляем на сервер:", payload);

  try {
    const response = await fetch('http://127.0.0.1:8000/submit-form', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    
    const result = await response.json();

    if (response.ok) {
      console.log("Успех:", result);
      // Показываем поп-ап
      showSuccessModal.value = true;
      // Очищаем форму (кроме объекта)
      formData.value.name = '';
      formData.value.phone = '';
    } else {
      console.error("Ошибка сервера:", result.detail);
      alert("Ошибка при отправке: " + (result.detail || "неизвестная ошибка"));
    }
  } catch (error) {
    console.error("Критическая ошибка:", error);
    alert("Не удалось связаться с сервером. Проверь, запущен ли Docker.");
  }
};
</script>

<template>
  <section class="contact">
    <h2>Получить консультацию</h2>

    <div class="contact-wrapper">
      <div class="contact-info">
        <h3>Позвоните нам</h3>
        <p class="phone">+7 (920) 666-68-91</p>
        <h3>Расположение</h3>
        <p class="address">Москва, ул. Тверская, д. 12, офис 34</p>
        <h3>Рабочие часы</h3>
        <p class="hours">Пн-Пт: 09:00 — 20:00<br>Сб-Вс: 10:00 — 18:00</p>
      </div>

      <form @submit.prevent="submitForm">
        <input v-model="formData.name" placeholder="Ваше имя" required />
        <input v-model="formData.phone" placeholder="Телефон" required type="tel" />

        <select v-model="formData.object_id" required :disabled="isLoadingObjects">
          <option v-if="isLoadingObjects" disabled value="">Загрузка...</option>
          <option v-for="obj in objectsList" :key="obj.id" :value="obj.id">
            {{ obj.name }}
          </option>
        </select>

        <button type="submit">Отправить</button>
      </form>
    </div>

    <div v-if="showSuccessModal" class="modal-overlay" @click.self="showSuccessModal = false">
      <div class="modal-content">
        <div class="icon-check">✓</div>
        <h3>Ваша заявка принята!</h3>
        <p>С вами свяжутся в ближайшее время <br> <strong>&lt;3</strong></p>
        <button class="modal-btn" @click="showSuccessModal = false">Отлично</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Стили оставляем без изменений, они у тебя отличные */
.contact { padding: 40px 10%; background: #f9f9f9; position: relative; }
.contact h2 { font-family: "Playfair Display", serif; font-size: 32px; margin-bottom: 50px; text-align: center; color: #2c3e50; }
.contact-wrapper { display: flex; flex-wrap: wrap; gap: 40px; justify-content: center; align-items: flex-start; }
.contact-info { flex: 1 1 300px; max-width: 400px; background: #4C6093; color: white; padding: 30px 25px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); display: flex; flex-direction: column; gap: 16px; }
.contact-info h3 { font-family: "Playfair Display", serif; font-size: 20px; font-weight: bold; margin-bottom: 6px; }
.contact-info p { font-size: 14px; line-height: 1.5; }
form { flex: 1 1 350px; max-width: 500px; display: flex; flex-direction: column; gap: 18px; background: white; padding: 30px 25px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); }
input, select { padding: 14px 16px; border-radius: 8px; border: 1px solid #ccc; font-size: 14px; transition: border-color 0.3s; }
input:focus, select:focus { border-color: #3b82f6; outline: none; }
button { background: #4C6093; color: white; font-weight: bold; padding: 14px; border: none; border-radius: 8px; cursor: pointer; transition: background-color 0.3s ease; }
button:hover { background: #5875c3; }
@media (max-width: 900px) { .contact-wrapper { flex-direction: column; } }

.modal-overlay {
  position: fixed; top: 0; left: 0; width: 100%; height: 100%;
  background: rgba(0, 0, 0, 0.6); display: flex; justify-content: center; align-items: center; z-index: 9999;
}
.modal-content {
  background: white; padding: 40px; border-radius: 15px; text-align: center; max-width: 350px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}
.icon-check { width: 50px; height: 50px; background: #4C6093; color: white; border-radius: 50%; 
              display: flex; align-items: center; justify-content: center; margin: 0 auto 15px; font-size: 24px; }
.modal-content h3 { margin-bottom: 10px; color: #2c3e50; font-weight: bold; }
.modal-btn { width: 100%; margin-top: 20px; }
</style>