<template>
  <div>
    <Header />

    <!-- Основной блок о команде -->
    <section class="team">
      <h2>Наша команда</h2>
      <p class="team-subtitle">Профессионалы, которым можно доверять</p>

      <div class="team-grid">
        <div v-for="member in teamMembers" :key="member.name" class="team-card">
          <div class="card-image">
            <img :src="member.photo" :alt="member.name" />
          </div>
          <div class="card-info">
            <h3>{{ member.name }}</h3>
            <p class="position">{{ member.position }}</p>
            <p class="experience">Опыт: {{ member.experience }} лет</p>
            <p class="phone">{{ member.phone }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Новая секция: Почему мы -->
    <section class="values">
      <h2>Почему выбирают нас</h2>
      <div class="values-grid">
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/cup.svg" alt="Кубок">
          </div>
          <h3>15 лет на рынке</h3>
          <p>Работаем с недвижимостью с 2010 года, знаем все тонкости рынка</p>
        </div>
        
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/scales.svg" alt="Весы">
          </div>
          <h3>Юридическая чистота</h3>
          <p>Каждую сделку проверяют опытные юристы. Никаких рисков</p>
        </div>
        
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/handshake.svg" alt="Рукопожатие">
          </div>
          <h3>Индивидуальный подход</h3>
          <p>Ищем варианты точно под ваш запрос и бюджет</p>
        </div>
        
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/lightning.svg" alt="Молния">
          </div>
          <h3>Быстрые сделки</h3>
          <p>Помогаем купить или продать недвижимость в среднем за 2 недели</p>
        </div>
        
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/graph.svg" alt="График">
          </div>
          <h3>Актуальная база</h3>
          <p>Только проверенные объекты без посредников и скрытых комиссий</p>
        </div>
        
        <div class="value-item">
          <div class="value-icon">
            <img src="../assets/icons/support.svg" alt="Поддержка">
          </div>
          <h3>Поддержка 24/7</h3>
          <p>На связи на всех этапах — от показа до получения ключей</p>
        </div>
      </div>
    </section>

    <ContactForm />
    <Footer />
  </div>
</template>

<script setup>
import Header from "../components/Header.vue"
import ContactForm from "../components/ContactForm.vue"
import Footer from "../components/Footer.vue"

// Данные команды
const teamMembers = [
  {
    name: 'Анна Иванова',
    position: 'Генеральный директор',
    experience: 15,
    phone: '+7 (999) 123-45-67',
    photo: '/src/assets/anna.png'
  },
  {
    name: 'Петр Смирнов',
    position: 'Руководитель отдела продаж',
    experience: 10,
    phone: '+7 (999) 234-56-78',
    photo: '/src/assets/petr.png'
  },
  {
    name: 'Елена Козлова',
    position: 'Ведущий риэлтор',
    experience: 12,
    phone: '+7 (999) 345-67-89',
    photo: '/src/assets/elena.png'
  },
  {
    name: 'Дмитрий Новиков',
    position: 'Риэлтор по коммерции',
    experience: 8,
    phone: '+7 (999) 456-78-90',
    photo: '/src/assets/dmitry.png'
  }
]
</script>

<style scoped>
/* Секция команды */
.team {
  padding: 60px 10%;
  background: #f9f9f9;
  text-align: center;
}

.team h2 {
  font-family: "Playfair Display", serif;
  font-size: 36px;
  margin-bottom: 12px;
  color: #2c3e50;
}

.team-subtitle {
  font-size: 18px;
  color: #666;
  margin-bottom: 48px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

/* Карточка сотрудника */
.team-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: left;
}

.team-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}

.card-image {
  height: 320px;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center 20%;
  transition: transform 0.5s;
}

.team-card:hover .card-image img {
  transform: scale(1.05);
}

.card-info {
  padding: 20px;
}

.card-info h3 {
  font-family: "Playfair Display", serif;
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 4px;
  color: #2c3e50;
}

.card-info .position {
  font-size: 15px;
  color: #3B82F6;
  font-weight: 500;
  margin-bottom: 8px;
}

.card-info .experience,
.card-info .phone {
  font-size: 14px;
  color: #555;
  margin-bottom: 4px;
}

.card-info .phone {
  font-weight: 500;
  color: #2c3e50;
}

/* Новая секция: Почему мы */
.values {
  padding: 80px 10%;
  background: #f9f9f9;
  text-align: center;
}

.values h2 {
  font-family: "Playfair Display", serif;
  font-size: 36px;
  margin-bottom: 50px;
  color: #2c3e50;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 40px;
  max-width: 1200px;
  margin: 0 auto;
}

.value-item {
  padding: 30px 20px;
  background: #ffffff;
  border-radius: 16px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.value-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.value-icon {
  margin-bottom: 20px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.value-icon img {
  width: 50px;
  height: 50px;
  object-fit: contain;
}

.value-item h3 {
  font-family: "Playfair Display", serif;
  font-size: 22px;
  margin-bottom: 12px;
  color: #2c3e50;
}

.value-item p {
  font-size: 16px;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* Адаптивность */
@media (max-width: 768px) {
  .team, .values {
    padding: 40px 5%;
  }
  
  .team h2, .values h2 {
    font-size: 28px;
  }
  
  .values-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .value-item {
    padding: 25px 15px;
  }
  
  .value-icon img {
    width: 40px;
    height: 40px;
  }
}
</style>