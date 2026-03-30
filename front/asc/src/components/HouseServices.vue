<template>
  <section class="house-services">
    <h2>Дополнительные услуги</h2>

    <div class="service-grid">
      <button v-for="service in services" :key="service" type="button">
        {{ service }}
      </button>
    </div>
  </section>
</template>

<script setup lang="ts">
const services = ['Ремонт', 'Обслуживание', 'Юридическая помощь']
</script>

<style scoped>
.house-services {
  text-align: center;
}

.house-services h2 {
  margin-bottom: 30px;
  font-family: 'Playfair Display', serif;
  font-size: 2.25rem;
  font-weight: 400;
  color: #54515f;
}

.service-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.service-grid button {
  border: none;
  border-radius: 14px;
  background: #5b6fa7;
  color: #fff;
  padding: 18px 24px;
  font-size: 1.15rem;
  font-weight: 600;
  cursor: pointer;
  transition:
    transform 0.2s ease,
    background-color 0.2s ease;
}

.service-grid button:hover {
  background: #4c6093;
  transform: translateY(-2px);
}

@media (max-width: 900px) {
  .service-grid {
    grid-template-columns: 1fr;
  }
}
</style>
