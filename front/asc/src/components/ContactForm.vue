<script setup>
import { ref, onMounted } from 'vue'

// 1. Состояние формы
const formData = ref({
  name: '',
  phone: '',
  // Сюда запишется ID выбранного объекта
  object_id: null 
})

// 2. Список объектов для выпадающего списка
const objectsList = ref([])
// Состояние загрузки (чтобы показать "Загрузка..." пока список качается)
const isLoadingObjects = ref(true)

// 3. Функция загрузки списка объектов с бэкенда
const fetchObjects = async () => {
  try {
    isLoadingObjects.value = true
    const response = await fetch('http://127.0.0.1:8000/objects')
    if (response.ok) {
      objectsList.value = await response.json()
      // По умолчанию выбираем первый объект из списка
      if (objectsList.value.length > 0) {
        formData.value.object_id = objectsList.value[0].Object_ID
      }
    } else {
      console.error('Ошибка загрузки объектов:', response.statusText)
    }
  } catch (error) {
    console.error('Ошибка соединения при загрузке объектов:', error)
  } finally {
    isLoadingObjects.value = false
  }
}

// Запускаем загрузку объектов один раз при монтировании компонента
onMounted(() => {
  fetchObjects()
})

// 4. Функция отправки формы (та же, что и раньше)
const submitForm = async () => {
  try {
    // ВАЖНО: Проверяем, выбран ли объект
    if (!formData.value.object_id) {
      alert('Пожалуйста, выберите объект из списка!')
      return
    }

    const response = await fetch('http://127.0.0.1:8000/submit-form', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        fio: formData.value.name,
        phone: formData.value.phone,
        // Передаем реальный ID выбранного объекта
        object_id: formData.value.object_id 
      })
    })

    if (response.ok) {
      const result = await response.json()
      alert(`Заявка принята! Ей займется сотрудник ID: ${result.assigned_worker_id}`)
      
      // Очистка полей, но объект оставляем выбранным
      formData.value.name = ''
      formData.value.phone = ''
    } else {
      const errorData = await response.json()
      alert('Ошибка: ' + (errorData.detail || 'Не удалось отправить заявку'))
    }
  } catch (error) {
    console.error('Ошибка соединения при отправке:', error)
    alert('Сервер бэкенда не отвечает. Проверь консоль!')
  }
}
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
        <input 
          v-model="formData.name" 
          placeholder="Ваше имя" 
          required 
        />
        <input 
          v-model="formData.phone" 
          placeholder="Телефон" 
          required 
          type="tel"
        />

        <div class="select-wrapper">
          <label for="object-select">Выберите объект:</label>
          <select 
            id="object-select"
            v-model="formData.object_id"
            class="object-select"
            required
            :disabled="isLoadingObjects || objectsList.length === 0"
          >
            <option v-if="isLoadingObjects" disabled value="">Загрузка списка...</option>
            
            <option v-else-if="objectsList.length === 0" disabled value="">Объекты не найдены в БД!</option>
            
            <option 
              v-for="obj in objectsList" 
              :key="obj.Object_ID" 
              :value="obj.Object_ID"
            >
              {{ obj.name }} ({{ obj.district }} р-н)
            </option>
          </select>
        </div>

        <button type="submit">Отправить</button>
      </form>

    </div>
  </section>
</template>

<style scoped>
/* Твои старые стили остаются без изменений */
.contact { padding: 40px 10%; background: #f9f9f9; }
.contact h2 { font-family: "Playfair Display", serif; font-size: 32px; margin-bottom: 50px; text-align: center; color: #2c3e50; }
.contact-wrapper { display: flex; flex-wrap: wrap; gap: 40px; justify-content: center; align-items: flex-start; }
.contact-info { flex: 1 1 300px; max-width: 400px; background: #4C6093; color: white; padding: 30px 25px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); display: flex; flex-direction: column; gap: 16px; }
.contact-info h3 { font-family: "Playfair Display", serif; font-size: 20px; font-weight: bold; margin-bottom: 6px; }
.contact-info p { font-size: 14px; line-height: 1.5; }
form { flex: 1 1 350px; max-width: 500px; display: flex; flex-direction: column; gap: 18px; background: white; padding: 30px 25px; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.08); }
input { padding: 14px 16px; border-radius: 8px; border: 1px solid #ccc; font-size: 14px; transition: border-color 0.3s, box-shadow 0.3s; }
input:focus { border-color: #3b82f6; box-shadow: 0 0 0 3px rgba(59,130,246,0.2); outline: none; }
button { background: #4C6093; color: white; font-weight: bold; padding: 14px; border: none; border-radius: 8px; cursor: pointer; transition: background-color 0.3s ease; margin-top: 10px; }
button:hover { background: #5875c3; }
@media (max-width: 900px) { .contact-wrapper { flex-direction: column; } }

/* НОВЫЕ СТИЛИ ДЛЯ ВЫПАДАЮЩЕГО СПИСКА */
.select-wrapper {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.select-wrapper label {
  font-size: 14px;
  color: #555;
  padding-left: 4px;
}

.object-select {
  padding: 14px 16px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 14px;
  background-color: white;
  cursor: pointer;
  appearance: none; /* Убираем стандартную стрелку браузера */
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 16px center;
  background-size: 16px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

.object-select:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
  outline: none;
}

.object-select:disabled {
  background-color: #f1f1f1;
  cursor: not-allowed;
  opacity: 0.7;
}
</style>