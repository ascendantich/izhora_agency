<template>
  <footer class="footer">

    <div class="footer-container">

      <div class="footer-column">
        <h3>ИЖОРА</h3>
        <p>Агентство недвижимости. Помогаем купить и продать жильё.</p>
      </div>

      <div class="footer-column">
        <h4>Навигация</h4>
        <ul>
          <li><a href="/">Главная</a></li>
          <li><a href="/properties">Объекты</a></li>
          <li><a href="/about">О компании</a></li>
          <li><a href="/contact">Контакты</a></li>
        </ul>
      </div>

      <div class="footer-column">
        <h4>Контакты</h4>
        <p>Телефон: +7 (999) 123-45-67</p>
        <p>Email: info@izhora.ru</p>
      </div>

    </div>

    <div class="footer-bottom">
      © 2026 ИЖОРА. Все права защищены
    </div>

  </footer>
</template>

<script setup lang="ts">
</script>

<style scoped>

.footer {
  background: #111;
  color: white;
  padding: 60px 10% 30px;
}

.footer-container {
  display: flex;
  justify-content: space-between;
  gap: 40px;
  margin-bottom: 40px;
}

.footer-column {
  max-width: 250px;
}

.footer-column h3,
.footer-column h4 {
  margin-bottom: 15px;
}

.footer-column ul {
  list-style: none;
  padding: 0;
}

.footer-column li {
  margin-bottom: 8px;
}

.footer-column a {
  color: #ccc;
  text-decoration: none;
}

.footer-column a:hover {
  color: white;
}

.footer-bottom {
  border-top: 1px solid #333;
  padding-top: 20px;
  text-align: center;
  color: #888;
}

</style>