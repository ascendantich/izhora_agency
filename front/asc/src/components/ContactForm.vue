<template>
<section class="contact">

  <h2>Получить консультацию</h2>

  <div class="contact-wrapper">
    
    <!-- Левая колонка: контактные данные -->
    <div class="contact-info">
      <h3>Позвоните нам</h3>
      <p class="phone">+7 (999) 123-45-67</p>
      
      <h3>Расположение</h3>
      <p class="address">Москва, ул. Тверская, д. 12, офис 34</p>
      
      <h3>Рабочие часы</h3>
      <p class="hours">Пн-Пт: 09:00 — 20:00<br>Сб-Вс: 10:00 — 18:00</p>
    </div>

    <!-- Правая колонка: форма -->
    <form>
      <input placeholder="Ваше имя" />
      <input placeholder="Телефон" />
      <textarea placeholder="Комментарий"></textarea>
      <button type="submit">Отправить</button>
    </form>

  </div>

</section>
</template>

<style scoped>
.contact {
  padding: 40px 10%;
  background: #f9f9f9;
}

.contact h2 {
  font-family: "Playfair Display", serif;
  font-size: 32px;
  margin-bottom: 50px;
  text-align: center;
  color: #2c3e50;
}

/* Две колонки */
.contact-wrapper {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: center;
  align-items: flex-start;
}

/* Левая колонка: контактные данные */
.contact-info {
  flex: 1 1 300px;
  max-width: 400px;
  background: #4C6093;
  color: white;
  padding: 30px 25px;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.contact-info h3 {
  font-family: "Playfair Display", serif;
  font-size: 20px;
    font-weight: bold;
  margin-bottom: 6px;
}

.contact-info p {
  font-size: 14px;
  line-height: 1.5;
}

/* Правая колонка: форма */
form {
  flex: 1 1 350px;
  max-width: 500px;
  display: flex;
  flex-direction: column;
  gap: 18px;
  background: white;
  padding: 30px 25px;
  border-radius: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.08);
}

input, textarea {
  padding: 14px 16px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-size: 14px;
  transition: border-color 0.3s, box-shadow 0.3s;
}

input:focus, textarea:focus {
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59,130,246,0.2);
  outline: none;
}

textarea {
  min-height: 100px;
  resize: vertical;
}

/* Кнопка */
button {
  background: #4C6093;
  color: white;
  font-weight: bold;
  padding: 14px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background: #5875c3;
}

/* Адаптивность */
@media (max-width: 900px) {
  .contact-wrapper {
    flex-direction: column;
  }
}
</style>