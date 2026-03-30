<template>
  <div class="house-page">
    <Header />

    <section class="house-section gallery-section">
      <HouseGallerySwiper title="ЖК ИЖОРА RESIDENCE" />
    </section>

    <section class="house-section overview-section">
      <div class="overview-layout">
        <div class="overview-main">
          <div class="breadcrumbs">Главная / Объекты / ЖК ИЖОРА RESIDENCE</div>

          <div class="title-row">
            <div>
              <h1>ЖК ИЖОРА RESIDENCE</h1>
              <p class="subtitle">Клубный дом бизнес-класса в центре Москвы с приватным двором и сервисной управляющей компанией.</p>
            </div>

            <div class="status-badges">
              <span>Бизнес-класс</span>
              <span>Сдача в 2026</span>
              <span>Ипотека от 7,9%</span>
            </div>
          </div>

          <div class="facts-grid">
            <article v-for="fact in facts" :key="fact.label" class="fact-card">
              <span>{{ fact.label }}</span>
              <strong>{{ fact.value }}</strong>
            </article>
          </div>

          <section class="text-block">
            <h2>Описание объекта</h2>
            <p>
              ЖК ИЖОРА RESIDENCE создан для покупателей, которым важны локация, приватность и качественная среда.
              Здесь сочетаются продуманная архитектура, камерное количество квартир на этаже и сервисный подход,
              который обычно ждут от премиальных проектов.
            </p>
            <p>
              До метро можно дойти пешком за несколько минут, рядом деловой центр, рестораны, фитнес и городская
              инфраструктура. Внутри проекта доступны квартиры с отделкой, семейные планировки и инвестиционные
              форматы под аренду.
            </p>
          </section>

          <section class="text-block">
            <h2>Почему этот объект смотрится сильнее рынка</h2>

            <div class="advantages-grid">
              <article v-for="item in advantages" :key="item.title" class="advantage-card">
                <h3>{{ item.title }}</h3>
                <p>{{ item.description }}</p>
              </article>
            </div>
          </section>
        </div>

        <aside class="offer-card">
          <div class="offer-price">от 15 000 000 ₽</div>
          <p class="offer-meta">от 40,3 м² • 1–4 комнаты</p>

          <div class="offer-list">
            <div v-for="point in offerPoints" :key="point.label" class="offer-item">
              <span>{{ point.label }}</span>
              <strong>{{ point.value }}</strong>
            </div>
          </div>

          <button type="button">Записаться на показ</button>
          <router-link to="/mortgage" class="secondary-link">Рассчитать ипотеку</router-link>
        </aside>
      </div>
    </section>

    <section class="house-section plans-section" @click="handlePlansClick">
      <PropertyCarousel />
    </section>

    <section class="house-section services-section">
      <HouseServices />
    </section>

    <ContactForm />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'

import Header from '@/components/Header.vue'
import HouseGallerySwiper from '@/components/HouseGallerySwiper.vue'
import HouseServices from '@/components/HouseServices.vue'
import PropertyCarousel from '@/components/PropertyCarousel.vue'
import ContactForm from '@/components/ContactForm.vue'
import Footer from '@/components/Footer.vue'

const router = useRouter()

const facts = [
  { label: 'Локация', value: 'Тверской район' },
  { label: 'Метро', value: 'Маяковская • 7 мин' },
  { label: 'Формат', value: 'Квартиры и апартаменты' },
  { label: 'Отделка', value: 'White box / дизайнерская' },
]

const advantages = [
  {
    title: 'Редкий формат',
    description: 'Клубный объем предложения без перегруженного двора и с приватной инфраструктурой для резидентов.',
  },
  {
    title: 'Сильная локация',
    description: 'Рядом офисы, рестораны, транспорт и все, что нужно для жизни и аренды в центральной части города.',
  },
  {
    title: 'Гибкие сценарии покупки',
    description: 'Можно подобрать семейную планировку, инвестиционный лот или квартиру с готовой отделкой.',
  },
]

const offerPoints = [
  { label: 'Срок сдачи', value: 'IV квартал 2026' },
  { label: 'Форматы', value: '1–4 комнаты' },
  { label: 'Планировки', value: '8 вариантов' },
]

const handlePlansClick = (event: MouseEvent) => {
  const target = event.target as HTMLElement | null
  const card = target?.closest('.card')

  if (!card) {
    return
  }

  router.push('/apartment')
}
</script>

<style scoped>
.house-page {
  background: #f9f9f9;
}

.house-section {
  padding: 0 10% 56px;
}

.gallery-section {
  padding-bottom: 32px;
}

.overview-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.75fr) 360px;
  gap: 28px;
  align-items: start;
}

.overview-main {
  display: grid;
  gap: 28px;
}

.breadcrumbs {
  font-size: 0.92rem;
  color: #7a8190;
}

.title-row {
  display: grid;
  gap: 18px;
}

.title-row h1 {
  margin: 0 0 10px;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 3rem;
  font-weight: 500;
  color: #2c3e50;
}

.subtitle {
  max-width: 780px;
  margin: 0;
  line-height: 1.7;
  color: #5f6b7a;
}

.status-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.status-badges span {
  border-radius: 999px;
  background: #edf2fb;
  color: #35508e;
  padding: 10px 14px;
  font-weight: 600;
}

.facts-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 14px;
}

.fact-card {
  display: grid;
  gap: 8px;
  padding: 18px;
  border-radius: 16px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.06);
}

.fact-card span {
  font-size: 0.9rem;
  color: #7a8190;
}

.fact-card strong {
  font-size: 1.05rem;
  color: #1f2937;
}

.text-block {
  display: grid;
  gap: 16px;
}

.text-block h2 {
  margin: 0;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 2.1rem;
  font-weight: 500;
  color: #2c3e50;
}

.text-block p {
  margin: 0;
  line-height: 1.8;
  color: #5f6b7a;
}

.advantages-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.advantage-card {
  padding: 22px;
  border-radius: 18px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.06);
}

.advantage-card h3 {
  margin: 0 0 10px;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 1.5rem;
  font-weight: 500;
  color: #2c3e50;
}

.advantage-card p {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.offer-card {
  position: sticky;
  top: 20px;
  display: grid;
  gap: 18px;
  padding: 24px;
  border-radius: 22px;
  background: #ffffff;
  box-shadow: 0 18px 40px rgba(44, 62, 80, 0.12);
}

.offer-price {
  font-size: 2.4rem;
  font-weight: 700;
  color: #111827;
}

.offer-meta {
  margin: -10px 0 0;
  color: #667085;
}

.offer-list {
  display: grid;
  gap: 14px;
}

.offer-item {
  display: flex;
  justify-content: space-between;
  gap: 14px;
  padding-bottom: 12px;
  border-bottom: 1px solid #edf1f7;
}

.offer-item span {
  color: #667085;
}

.offer-item strong {
  text-align: right;
  color: #111827;
}

.offer-card button,
.secondary-link {
  border: none;
  border-radius: 12px;
  padding: 15px 18px;
  text-align: center;
  text-decoration: none;
  font-weight: 600;
}

.offer-card button {
  background: #5b6fa7;
  color: #fff;
  cursor: pointer;
}

.secondary-link {
  background: #eef2fb;
  color: #35508e;
}

.plans-section {
  padding-top: 0;
}

.plans-section :deep(.card) {
  cursor: pointer;
}

.plans-section :deep(.properties) {
  padding: 0;
  background: transparent;
}

.plans-section :deep(.properties h2) {
  margin-bottom: 14px;
  font-size: 0;
}

.plans-section :deep(.properties h2)::after {
  content: 'Доступные планировки';
  display: block;
  font-family: "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
  font-size: 2.25rem;
  font-weight: 500;
  line-height: 1.1;
  color: #2c3e50;
}

.plans-section :deep(.properties h2)::before {
  content: 'Выберите формат квартиры, чтобы посмотреть детальную планировку, стоимость и условия покупки.';
  display: block;
  margin-bottom: 18px;
  font-family: Arial, sans-serif;
  font-size: 1rem;
  line-height: 1.6;
  color: #6b7280;
}

.plans-section :deep(.cards) {
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 16px;
}

.plans-section :deep(.card:nth-child(n + 5)) {
  display: none;
}

.plans-section :deep(.card-image img) {
  height: 230px;
}

.plans-section :deep(.card-info) {
  padding: 12px 14px 14px;
}

.plans-section :deep(.card-info .price) {
  font-size: 1.55rem;
}

.plans-section :deep(.card-info .address),
.plans-section :deep(.card-info .metro) {
  display: none;
}

.services-section {
  padding-top: 0;
}

@media (max-width: 1260px) {
  .overview-layout {
    grid-template-columns: 1fr;
  }

  .offer-card {
    position: static;
  }

  .facts-grid,
  .advantages-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

  .plans-section :deep(.cards) {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (max-width: 768px) {
  .house-section {
    padding-right: 5%;
    padding-left: 5%;
    padding-bottom: 40px;
  }

  .title-row h1 {
    font-size: 2.3rem;
  }

  .plans-section :deep(.properties h2)::after {
    font-size: 2rem;
    line-height: 1.06;
  }

  .facts-grid,
  .advantages-grid,
  .plans-section :deep(.cards) {
    grid-template-columns: 1fr;
  }
}
</style>
