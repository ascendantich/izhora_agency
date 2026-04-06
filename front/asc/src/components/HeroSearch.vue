<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
// Состояние для текста в поле поиска
const searchQuery = ref('')

// Функция для перехода на страницу объектов
const handleSearch = () => {
  // Если поле не пустое, переходим на /objects с параметром location
  // (В прошлом коде твой бэкенд ожидает параметр 'location' для поиска по строке)
  router.push({
    path: '/objects',
    query: { location: searchQuery.value }
  })
}
</script>

<template>
  <section class="hero">
    <div class="hero-content">
      <h1>Найдите идеальную недвижимость</h1>
      <p>Квартиры, дома и коммерческая недвижимость</p>

      <div class="search-box">
        <input 
          v-model="searchQuery"
          type="text"
          placeholder="Город, район, метро, ЖК"
          @keyup.enter="handleSearch"
        />

        <button @click="handleSearch">
          Найти
        </button>
      </div>

      <div class="categories">
        <button @click="router.push({ path: '/objects', query: { type: 'Квартиры' } })">Купить</button>
        <button @click="router.push({ path: '/objects', query: { type: 'Снять' } })">Снять</button>
        <button @click="router.push({ path: '/objects', query: { type: 'Новостройки' } })">Новостройки</button>
        <button @click="router.push({ path: '/objects', query: { type: 'Дома' } })">Дома</button>
        <button @click="router.push({ path: '/objects', query: { type: 'Коммерция' } })">Коммерция</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  height: 80vh;
  background-image: 
    linear-gradient(rgba(8, 20, 33, 0.42), rgba(8, 20, 33, 0.24)),
    url('../assets/hero.png');
  background-size: cover;
  background-size:cover;
  background-position:center 40%;
  display:flex;
  align-items:center;
  justify-content:center;
}

.hero-content{
  text-align:center;
  max-width:800px;
}

.hero h1{
  font-size:48px;
  font-weight: bold;
  color:white;
  margin-bottom:12px;
  line-height: 1.2;
}

.hero p{
  font-size:18px;
  color:white;
  margin-bottom:30px;
}

.search-box {
  display: flex;
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}

.search-box input {
  flex: 1;
  padding: 18px;
  border: none;
  font-size: 16px;
  outline: none;
}

.search-box button {
  padding: 18px 30px;
  background: #4C6093;
  color: white;
  border: none;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
}

.search-box button:hover {
  background: #5875c3;
}

.categories {
  margin-top: 20px;
}

.categories button {
  margin: 6px;
  padding: 10px 18px;
  border-radius: 20px;
  border: none;
  background: #ffffffcc;
  cursor: pointer;
  transition: background 0.3s;
}

.categories button:hover {
  background: #ffffff;
}
</style>
