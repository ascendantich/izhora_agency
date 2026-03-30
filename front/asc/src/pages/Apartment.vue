<template>
  <div class="apartment-page">
    <Header />

    <section class="apartment-section gallery-section">
      <ApartmentGallerySwiper />
    </section>

    <section class="apartment-section summary-section">
      <div class="summary-layout">
        <div class="summary-main">
          <div class="breadcrumbs">Объекты / ЖК ИЖОРА RESIDENCE / 3-комнатная квартира 40,3 м²</div>

          <div class="heading-block">
            <div>
              <h1>3-комнатная квартира, 40,3 м²</h1>
              <p class="address">Москва, ул. Тверская, д. 12, кв. 34</p>
            </div>

            <div class="chips">
              <span>С отделкой</span>
              <span>Показ онлайн</span>
              <span>Без комиссии</span>
            </div>
          </div>

          <div class="stats-grid">
            <article v-for="item in stats" :key="item.label" class="stat-card">
              <span>{{ item.label }}</span>
              <strong>{{ item.value }}</strong>
            </article>
          </div>

          <section class="content-block">
            <h2>Описание квартиры</h2>
            <p>
              Планировка подойдет для жизни в центре или для инвестиционной покупки под аренду. Квартира компактная,
              но грамотно организованная: отдельные спальни, общая зона кухни-гостиной и сценарий хранения без
              перегруженных коридоров.
            </p>
            <p>
              В лоте предусмотрены большие окна, подготовка под кондиционирование и качественный white box, который
              можно быстро адаптировать под собственный интерьер. Это как раз тот формат, который хорошо выглядит в
              рекламе и легко продается на вторичном рынке.
            </p>
          </section>

          <section class="content-block">
            <h2>Что важно покупателю</h2>

            <div class="feature-list">
              <article v-for="item in features" :key="item.title" class="feature-card">
                <h3>{{ item.title }}</h3>
                <p>{{ item.description }}</p>
              </article>
            </div>
          </section>
        </div>

        <aside class="deal-card">
          <div class="deal-price">15 000 000 ₽</div>
          <p class="deal-subtitle">372 208 ₽ за м²</p>

          <div class="deal-points">
            <div v-for="item in dealPoints" :key="item.label" class="deal-row">
              <span>{{ item.label }}</span>
              <strong>{{ item.value }}</strong>
            </div>
          </div>

          <button type="button">Оставить заявку</button>
          <router-link to="/mortgage" class="secondary-link">Ипотека и рассрочка</router-link>
        </aside>
      </div>
    </section>

    <section class="apartment-section services-section">
      <HouseServices />
    </section>

    <ContactForm />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header.vue'
import ApartmentGallerySwiper from '@/components/ApartmentGallerySwiper.vue'
import HouseServices from '@/components/HouseServices.vue'
import ContactForm from '@/components/ContactForm.vue'
import Footer from '@/components/Footer.vue'

const stats = [
  { label: 'Комнат', value: '3' },
  { label: 'Площадь', value: '40,3 м²' },
  { label: 'Этаж', value: '8 из 16' },
  { label: 'Метро', value: 'Маяковская' },
]

const features = [
  {
    title: 'Продуманная планировка',
    description: 'Логичное деление на приватную и общую зоны, без лишних транзитных площадей.',
  },
  {
    title: 'Хорошая ликвидность',
    description: 'Формат и площадь подходят как для личного проживания, так и для аренды в центре.',
  },
  {
    title: 'Готовность к ремонту',
    description: 'White box сокращает сроки отделки и помогает быстрее выйти на сделку или переезд.',
  },
]

const dealPoints = [
  { label: 'Срок сдачи', value: 'IV квартал 2026' },
  { label: 'Отделка', value: 'White box' },
  { label: 'Формат сделки', value: 'ДДУ / ипотека' },
]
</script>

<style scoped>
.apartment-page {
  background: #f9f9f9;
}

.apartment-section {
  padding: 0 10% 56px;
}

.gallery-section {
  padding-bottom: 36px;
}

.summary-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.8fr) 360px;
  gap: 28px;
  align-items: start;
}

.summary-main {
  display: grid;
  gap: 28px;
}

.breadcrumbs {
  font-size: 0.92rem;
  color: #7a8190;
}

.heading-block {
  display: grid;
  gap: 18px;
}

.heading-block h1 {
  margin: 0 0 10px;
  font-family: 'Playfair Display', serif;
  font-size: 2.75rem;
  font-weight: 400;
  color: #2c3e50;
}

.address {
  margin: 0;
  color: #5f6b7a;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.chips span {
  border-radius: 999px;
  background: #edf2fb;
  color: #35508e;
  padding: 10px 14px;
  font-weight: 600;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
}

.stat-card {
  display: grid;
  gap: 8px;
  padding: 18px;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.06);
}

.stat-card span {
  font-size: 0.9rem;
  color: #7a8190;
}

.stat-card strong {
  font-size: 1.05rem;
  color: #1f2937;
}

.content-block {
  display: grid;
  gap: 16px;
}

.content-block h2 {
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: 2.1rem;
  font-weight: 400;
  color: #2c3e50;
}

.content-block p {
  margin: 0;
  line-height: 1.8;
  color: #5f6b7a;
}

.feature-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.feature-card {
  padding: 22px;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.06);
}

.feature-card h3 {
  margin: 0 0 10px;
  font-family: 'Playfair Display', serif;
  font-size: 1.45rem;
  font-weight: 400;
  color: #2c3e50;
}

.feature-card p {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.deal-card {
  position: sticky;
  top: 20px;
  display: grid;
  gap: 18px;
  padding: 24px;
  border-radius: 22px;
  background: #ffffff;
  box-shadow: 0 18px 40px rgba(44, 62, 80, 0.12);
}

.deal-price {
  font-size: 2.4rem;
  font-weight: 700;
  color: #111827;
}

.deal-subtitle {
  margin: -10px 0 0;
  color: #667085;
}

.deal-points {
  display: grid;
  gap: 14px;
}

.deal-row {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid #edf1f7;
}

.deal-row span {
  color: #667085;
}

.deal-row strong {
  text-align: right;
  color: #111827;
}

.deal-card button,
.secondary-link {
  border: none;
  border-radius: 12px;
  padding: 15px 18px;
  text-align: center;
  text-decoration: none;
  font-weight: 600;
}

.deal-card button {
  background: #5b6fa7;
  color: #fff;
  cursor: pointer;
}

.secondary-link {
  background: #eef2fb;
  color: #35508e;
}

.services-section {
  padding-top: 0;
}

@media (max-width: 1260px) {
  .summary-layout {
    grid-template-columns: 1fr;
  }

  .deal-card {
    position: static;
  }

  .stats-grid,
  .feature-list {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 768px) {
  .apartment-section {
    padding-right: 5%;
    padding-left: 5%;
    padding-bottom: 40px;
  }

  .heading-block h1 {
    font-size: 2.2rem;
  }

  .stats-grid,
  .feature-list {
    grid-template-columns: 1fr;
  }
}
</style>
