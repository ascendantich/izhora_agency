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
    const response = await fetch('http://127.0.0.1:8000/objects')
    if (response.ok) {
      objectsList.value = await response.json()
      // Если объекты есть, выбираем первый по умолчанию
      if (objectsList.value.length > 0) {
        formData.value.object_id = objectsList.value[0].Object_ID
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
        <p class="phone">+7 (999) 123-45-67</p>
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
          <option v-for="obj in objectsList" :key="obj.Object_ID" :value="obj.Object_ID">
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
.contact {
  padding: clamp(32px, 4vw, 56px) clamp(16px, 7vw, 10%);
  background: #f9f9f9;
  position: relative;
}

.contact h2 {
  margin: 0 0 clamp(22px, 4vw, 44px);
  text-align: center;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: clamp(1.9rem, 3.4vw, 2.35rem);
  font-weight: 500;
  color: #2c3e50;
}

.contact-wrapper {
  width: 100%;
  display: grid;
  grid-template-columns: minmax(280px, 0.9fr) minmax(320px, 1.1fr);
  gap: clamp(16px, 2.4vw, 34px);
  align-items: stretch;
}

.contact-info {
  width: 100%;
  background: #4c6093;
  color: #fff;
  padding: clamp(20px, 2.6vw, 30px) clamp(18px, 2.2vw, 25px);
  border-radius: 16px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 14px;
}

.contact-info h3 {
  margin: 0;
  line-height: 1.2;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: clamp(1.1rem, 1.8vw, 1.3rem);
  font-weight: 700;
}

.contact-info p {
  margin: 0;
  line-height: 1.55;
  font-size: clamp(0.9rem, 1.35vw, 0.98rem);
}

form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 14px;
  background: #fff;
  padding: clamp(20px, 2.6vw, 30px) clamp(18px, 2.2vw, 25px);
  border-radius: 16px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
}

input,
select,
textarea {
  width: 100%;
  box-sizing: border-box;
  border: 1px solid #d0d5dd;
  border-radius: 8px;
  padding: 14px 16px;
  font-size: 0.95rem;
  font-family: inherit;
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus,
select:focus,
textarea:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2);
  outline: none;
}

textarea {
  min-height: 112px;
  resize: vertical;
}

button {
  width: 100%;
  border: none;
  border-radius: 8px;
  padding: 14px;
  background: #4c6093;
  color: #fff;
  font-weight: 700;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background: #5875c3;
}

@media (max-width: 1024px) {
  .contact-wrapper {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .contact {
    padding-right: 4%;
    padding-left: 4%;
  }

  .contact h2 {
    margin-bottom: 32px;
  }

  .contact-wrapper {
    gap: 14px;
  }

  form {
    gap: 12px;
  }

  textarea {
    min-height: 100px;
  }
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.6);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.modal-content {
  background: white;
  padding: 40px;
  border-radius: 15px;
  text-align: center;
  max-width: 350px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
}

.icon-check {
  width: 50px;
  height: 50px;
  background: #4c6093;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 15px;
  font-size: 24px;
}

.modal-content h3 {
  margin-bottom: 10px;
  color: #2c3e50;
  font-weight: 700;
}

.modal-btn {
  width: 100%;
  margin-top: 20px;
}
</style>
