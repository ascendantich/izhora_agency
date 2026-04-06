<script setup lang="ts">
import { ref, onMounted } from 'vue'

// Описываем интерфейс объекта для TypeScript
interface Property {
  id: number;
  title: string;
  price: string;
  rooms: string;
  address: string;
  metro: string;
  image: string;
  badge: string;
}

const properties = ref<Property[]>([])
const isLoading = ref(true)

// Загрузка данных из БД
const fetchProperties = async () => {
  try {
    isLoading.value = true
    // Запрашиваем данные с эндпоинта /properties
    const response = await fetch('http://localhost:8000/properties')
    if (response.ok) {
      properties.value = await response.json()
    } else {
      console.error("Ошибка сервера:", response.status)
    }
  } catch (error) {
    console.error("Не удалось загрузить объекты:", error)
  } finally {
    isLoading.value = false
  }
}

onMounted(() => {
  fetchProperties()
})
</script>

<template>
  <section class="properties">
    <h2>Популярные объекты</h2>

    <div v-if="isLoading" class="loading">Загрузка объектов...</div>

    <div v-else class="cards">
      <div class="card" v-for="property in properties" :key="property.id">
        
        <div class="card-image">
          <div v-if="property.badge" class="badge">{{ property.badge }}</div>
          <img :src="property.image" :alt="property.title" />
        </div>

        <div class="card-info">
          <div class="price">{{ property.price }}</div>
          <h3>{{ property.rooms }} — {{ property.title }}</h3>
          <p class="address">{{ property.address }}</p>
          <p class="metro" v-if="property.metro">
            Ближайшее метро: {{ property.metro }}
          </p>
        </div>

      </div>
    </div>

    <div v-if="!isLoading && properties.length === 0" class="empty">
      По вашему запросу ничего не найдено.
    </div>
  </section>
</template>

<style scoped>
.properties {
  padding: 40px 10%;
  background: #f9f9f9;
}

.properties h2 {
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 32px;
  font-weight: 500;
  color: #2c3e50;
  margin-bottom: 32px;
  text-align: center;
}

.loading, .empty {
  text-align: center;
  padding: 40px;
  color: #777;
}

/* Сетка карточек */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

/* Карточка */
.card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 25px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  position: relative;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

/* Бейдж (Проверено) */
.badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: rgba(255, 255, 255, 0.9);
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: bold;
  color: #4C6093;
  z-index: 2;
}

/* Картинка */
.card-image {
  position: relative;
}

.card-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  display: block;
}

/* Нижняя подложка */
.card-info {
  padding: 16px;
  background: #fff;
}

/* Цена */
.card-info .price {
  font-weight: bold;
  font-size: 22px;
  color: #111;
  margin-bottom: 4px;
}

/* Заголовок */
.card-info h3 {
  font-family: "Playfair Display", serif;
  font-size: 18px;
  margin-bottom: 4px;
}

/* Адрес */
.card-info .address {
  font-size: 14px;
  color: #555;
  margin-bottom: 4px;
}

/* Метро */
.card-info .metro {
  font-size: 13px;
  color: #777;
}
</style>