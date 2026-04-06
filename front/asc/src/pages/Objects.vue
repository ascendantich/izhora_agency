<template>
  <div class="objects-page">
    <Header />

    <section class="objects-section">
      <div class="objects-topbar">
        <div>
          <h1>Объекты недвижимости</h1>
          <p>Подборка актуальных квартир, домов и коммерческих помещений с проверенными данными.</p>
        </div>

        <div class="results-pill">{{ properties.length }} предложений</div>
      </div>

      <div class="catalog-layout">
        <aside class="filters-card">
          <h2>Подбор</h2>

          <label class="filter-field">
            <span>Тип объекта</span>
            <select v-model="filters.type">
              <option>Все объекты</option>
              <option>Квартиры</option>
              <option>Дома</option>
              <option>Коммерция</option>
            </select>
          </label>

          <label class="filter-field">
            <span>Бюджет</span>
            <select v-model="filters.budget">
              <option>Любой</option>
              <option>До 10 млн ₽</option>
              <option>10–20 млн ₽</option>
              <option>20+ млн ₽</option>
            </select>
          </label>

          <label class="filter-field">
            <span>Комнат</span>
            <select v-model="filters.rooms">
              <option>Любое количество</option>
              <option>1 комната</option>
              <option>2 комнаты</option>
              <option>3+ комнаты</option>
            </select>
          </label>

          <label class="filter-field">
            <span>Локация</span>
            <input 
              type="text" 
              v-model="filters.location" 
              placeholder="Москва, район, метро" 
            />
          </label>
     
          <button @click="fetchProperties" class="filter-button" >Показать варианты</button>
          
        </aside>

        <div class="cards-column">
          <router-link
            v-for="property in properties"
            :key="property.id"
            to="/house"
            class="property-card"
          >
            <div class="card-media">
              <img :src="property.image" :alt="property.title" />
              <span class="card-badge">{{ property.badge }}</span>
            </div>

            <div class="card-content">
              <div class="card-header">
                <div>
                  <div class="price">{{ property.price }}</div>
                  <h2>{{ property.title }}</h2>
                </div>
                <div class="area">{{ property.area }}</div>
              </div>

              <p class="address">{{ property.address }}</p>
              <p class="metro">{{ property.metro }}</p>

              <div class="card-footer">
                <span>{{ property.rooms }}</span>
                <span>{{ property.status }}</span>
              </div>
            </div>
          </router-link>
        </div>
      </div>
    </section>
    <ContactForm />
    <Footer />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
import ContactForm from "../components/ContactForm.vue"

// Полный интерфейс объекта недвижимости (соответствует твоему шаблону)
interface Property {
  id: number;
  title: string;
  price: string;
  image: string;
  location: string;
  address: string;
  area: string;
  status: string;
  badge?: string; // Добавлено
  metro?: string; // Добавлено
  rooms: string;  // Добавлено
}

// Типизируем фильтры
interface Filters {
  type: string;
  budget: string;
  rooms: string;
  location: string;
}

const properties = ref<Property[]>([])

const filters = ref<Filters>({
  type: 'Все объекты',
  budget: 'Любой',
  rooms: 'Любое количество',
  location: ''
})

const fetchProperties = async (): Promise<void> => {
  try {
    const params = new URLSearchParams({
      type: filters.value.type,
      budget: filters.value.budget,
      rooms: filters.value.rooms,
      location: filters.value.location
    })

    const response = await fetch(`http://localhost:8000/properties?${params.toString()}`)
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }
    
    const data: Property[] = await response.json()
    properties.value = data
  } catch (error) {
    console.error("Ошибка при загрузке данных:", error)
  }
}

onMounted(() => {
  // Читаем параметры из URL (window.location.search) для работы поиска с главной страницы
  const urlParams = new URLSearchParams(window.location.search);
  const locationFromUrl = urlParams.get('location');
  const typeFromUrl = urlParams.get('type');

  if (locationFromUrl) {
    filters.value.location = locationFromUrl;
  }
  if (typeFromUrl) {
    filters.value.type = typeFromUrl;
  }

  fetchProperties()
})
</script>

<style scoped>
.objects-page {
  min-height: 100vh;
  background: #f9f9f9;
}

.objects-section {
  padding: 44px 10% 72px;
}

.objects-topbar {
  display: flex;
  justify-content: space-between;
  align-items: end;
  gap: 24px;
  margin-bottom: 28px;
}

.objects-topbar h1 {
  margin: 0 0 10px;
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  font-weight: 400;
  color: #2c3e50;
}

.objects-topbar p {
  max-width: 760px;
  margin: 0;
  color: #6b7280;
  line-height: 1.6;
}

.results-pill {
  flex-shrink: 0;
  border-radius: 999px;
  background: rgba(76, 96, 147, 0.12);
  color: #35508e;
  padding: 10px 16px;
  font-weight: 600;
}

.catalog-layout {
  display: grid;
  grid-template-columns: 300px minmax(0, 1fr);
  gap: 28px;
}

.filters-card {
  position: sticky;
  top: 16px;
  align-self: start;
  display: grid;
  gap: 18px;
  padding: 22px;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.08);
}

.filters-card h2 {
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 400;
  color: #2c3e50;
}

.filter-field {
  display: grid;
  gap: 8px;
}

.filter-field span {
  font-size: 0.95rem;
  font-weight: 600;
  color: #475569;
}

.filter-field select,
.filter-field input {
  width: 100%;
  padding: 13px 14px;
  border: 1px solid #d8dee9;
  border-radius: 12px;
  background: #f8fafc;
  font-size: 0.95rem;
}

.filter-button {
  border: none;
  border-radius: 12px;
  background: #5b6fa7;
  color: #fff;
  padding: 15px 18px;
  font-weight: 600;
  cursor: pointer;
}

.cards-column {
  display: grid;
  gap: 20px;
}

.property-card {
  display: grid;
  grid-template-columns: 320px minmax(0, 1fr);
  gap: 0;
  overflow: hidden;
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.08);
  text-decoration: none;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.property-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 18px 40px rgba(44, 62, 80, 0.14);
}

.card-media {
  position: relative;
  /* Задаем фиксированные размеры контейнера */
  width: 320px;
  height: 240px;
  background: #f0f0f0; /* Цвет фона, если картинка не загрузится */
  overflow: hidden; /* Скрывает все, что не помещается */
}

.card-media img {
  display: block;
  /* Заставляет картинку занимать всю площадь контейнера, 
     независимо от ее реальных размеров */
  width: 100%;
  height: 100%;
  /* Самое важное: сохраняет пропорции, 
     лишнее обрезается (как в CSS background-size: cover) */
  object-fit: cover; 
}

.card-badge {
  position: absolute;
  left: 16px;
  top: 16px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.92);
  color: #334155;
  padding: 8px 12px;
  font-size: 0.9rem;
  font-weight: 600;
}

.card-content {
  display: grid;
  gap: 14px;
  padding: 22px 24px;
  color: #111827;
}

.card-header {
  display: flex;
  justify-content: space-between;
  gap: 16px;
  align-items: start;
}

.price {
  margin-bottom: 6px;
  font-size: 2rem;
  font-weight: 700;
  color: #111827;
}

.card-header h2 {
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: 1.85rem;
  font-weight: 400;
  line-height: 1.08;
  color: #2c3e50;
}

.area {
  flex-shrink: 0;
  border-radius: 14px;
  background: #f3f5fa;
  padding: 10px 14px;
  font-weight: 700;
  color: #35508e;
}

.address,
.metro {
  margin: 0;
  line-height: 1.5;
}

.address {
  color: #374151;
}

.metro {
  color: #667085;
}

.card-footer {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 6px;
}

.card-footer span {
  border-radius: 999px;
  background: #f5f7fb;
  color: #4b5563;
  padding: 8px 12px;
  font-size: 0.92rem;
}

@media (max-width: 1180px) {
  .catalog-layout {
    grid-template-columns: 1fr;
  }

  .filters-card {
    position: static;
  }
}

@media (max-width: 900px) {
  .property-card {
    grid-template-columns: 1fr;
  }

  .card-media {
    min-height: 220px;
  }

  .objects-topbar {
    flex-direction: column;
    align-items: start;
  }
}

@media (max-width: 768px) {
  .objects-section {
    padding-right: 5%;
    padding-left: 5%;
    padding-bottom: 48px;
  }

  .objects-topbar h1 {
    font-size: 2.35rem;
  }

  .card-header {
    flex-direction: column;
  }
}
</style>
