<template>
  <div class="corporate-page">
    <Header />

    <section class="corporate-hero" :style="heroStyle">
      <div class="hero-overlay">
        <span class="eyebrow">B2B сервис</span>
        <h1>Корпоративные решения для коммерческой недвижимости</h1>
        <p>Индивидуальные условия, юридическая поддержка, быстрый цикл согласования и персональный менеджер.</p>

        <div class="hero-actions">
          <button type="button">Получить предложение</button>
          <router-link to="/documents">Смотреть документы</router-link>
        </div>
      </div>
    </section>

    <section class="metrics-section">
      <article v-for="item in metrics" :key="item.label" class="metric-card">
        <span>{{ item.label }}</span>
        <strong>{{ item.value }}</strong>
      </article>
    </section>

    <section class="offers-section">
      <div class="section-head">
        <div>
          <h2>Что получает корпоративный клиент</h2>
          <p>Страница должна продавать сервис, поэтому здесь важны не только документы, но и понятная ценность для бизнеса.</p>
        </div>
      </div>

      <div class="offers-grid">
        <article v-for="item in offers" :key="item.title" class="offer-card">
          <div class="offer-icon">
            <img :src="item.icon" :alt="item.title" />
          </div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
        </article>
      </div>
    </section>

    <section class="process-section">
      <div class="section-head">
        <div>
          <h2>Как строится работа</h2>
          <p>Структура взаимодействия нужна, чтобы корпоративный клиент сразу видел понятный процесс и контроль сроков.</p>
        </div>
      </div>

      <div class="process-grid">
        <article v-for="step in process" :key="step.number" class="process-card">
          <span class="step-number">{{ step.number }}</span>
          <h3>{{ step.title }}</h3>
          <p>{{ step.description }}</p>
        </article>
      </div>
    </section>

    <ContactForm />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header.vue'
import ContactForm from '@/components/ContactForm.vue'
import Footer from '@/components/Footer.vue'
import heroImage from '@/assets/hero.png'
import graphIcon from '@/assets/icons/graph.svg'
import handshakeIcon from '@/assets/icons/handshake.svg'
import scalesIcon from '@/assets/icons/scales.svg'

const offers = [
  {
    title: 'Правила оферты',
    description: 'Прозрачные условия работы, которые понятны закупкам, юристам и внутренним согласующим.',
    icon: scalesIcon,
  },
  {
    title: 'Договоры о партнерстве',
    description: 'Типовые формы сотрудничества под агентские договоры, сопровождение сделок и пакетные сервисы.',
    icon: handshakeIcon,
  },
  {
    title: 'Условия сотрудничества',
    description: 'Специальные условия для девелоперов, инвесторов и корпоративных клиентов.',
    icon: graphIcon,
  },
]

const metrics = [
  { label: 'Формат работы', value: 'B2B / партнерский' },
  { label: 'Скорость запуска', value: 'от 3 дней' },
  { label: 'Сопровождение', value: 'личный менеджер' },
]

const process = [
  {
    number: '01',
    title: 'Бриф и задачи',
    description: 'Фиксируем тип объектов, юридические ограничения, желаемую экономику и сроки запуска работы.',
  },
  {
    number: '02',
    title: 'Документы и условия',
    description: 'Подбираем подходящую модель договора, согласуем условия сотрудничества и каналы взаимодействия.',
  },
  {
    number: '03',
    title: 'Выход в сделки',
    description: 'Запускаем работу по объектам, ведем клиентов, контролируем статусы и отчетность по каждой воронке.',
  },
]

const heroStyle = {
  backgroundImage: `linear-gradient(rgba(8, 20, 33, 0.42), rgba(8, 20, 33, 0.24)), url(${heroImage})`,
}
</script>

<style scoped>
.corporate-page {
  background: #f9f9f9;
}

.corporate-hero {
  min-height: 540px;
  display: grid;
  place-items: center;
  padding: 60px 10%;
  background-size: cover;
  background-position: center 42%;
}

.hero-overlay {
  max-width: 980px;
  text-align: center;
  color: #ffffff;
}

.eyebrow {
  display: inline-block;
  margin-bottom: 18px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.14);
  padding: 8px 12px;
  font-size: 0.9rem;
  font-weight: 600;
}

.hero-overlay h1 {
  margin: 0 0 16px;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2.2rem, 3.6vw, 3.6rem);
  line-height: 1.04;
  font-weight: 700;
}

.hero-overlay p {
  max-width: 920px;
  margin: 0 auto;
  font-size: 1.24rem;
  line-height: 1.7;
  color: rgba(255, 255, 255, 0.86);
}

.hero-actions {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-top: 26px;
}

.hero-actions button,
.hero-actions a {
  border-radius: 12px;
  padding: 15px 18px;
  text-decoration: none;
  font-weight: 600;
}

.hero-actions button {
  border: none;
  background: #5b6fa7;
  color: #fff;
  cursor: pointer;
}

.hero-actions a {
  background: rgba(255, 255, 255, 0.14);
  color: #fff;
}

.metrics-section,
.offers-section,
.process-section {
  padding: 0 10% 56px;
}

.metrics-section {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
  margin-top: 0;
  padding-top: 32px;
}

.metric-card,
.offer-card,
.process-card {
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(91, 111, 167, 0.08);
}

.metric-card {
  display: grid;
  gap: 8px;
  padding: 22px;
  border-radius: 20px;
}

.metric-card span {
  color: #667085;
}

.metric-card strong {
  font-size: 1.3rem;
  color: #1f2937;
}

.section-head {
  margin-bottom: 24px;
}

.section-head h2 {
  margin: 0 0 10px;
  font-family: 'Playfair Display', serif;
  font-size: 2.35rem;
  font-weight: 400;
  color: #2c3e50;
}

.section-head p {
  max-width: none;
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.offers-grid,
.process-grid {
  display: grid;
  gap: 18px;
}

.offers-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.offer-card {
  display: grid;
  gap: 14px;
  padding: 24px;
  border-radius: 20px;
}

.offer-icon {
  display: grid;
  place-items: center;
  width: 58px;
  height: 58px;
}

.offer-icon img {
  width: 48px;
  height: 48px;
  object-fit: contain;
}

.offer-card h3,
.process-card h3 {
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: 1.65rem;
  font-weight: 400;
  line-height: 1.18;
  color: #2c3e50;
}

.offer-card p,
.process-card p {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.process-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.process-card {
  display: grid;
  gap: 14px;
  padding: 24px;
  border-radius: 20px;
}

.step-number {
  width: fit-content;
  border-radius: 999px;
  background: #eef2fb;
  color: #35508e;
  padding: 8px 12px;
  font-weight: 700;
}

@media (max-width: 1100px) {
  .metrics-section,
  .offers-grid,
  .process-grid {
    grid-template-columns: 1fr;
  }

  .metrics-section {
    padding-top: 28px;
  }
}

@media (max-width: 768px) {
  .corporate-hero,
  .metrics-section,
  .offers-section,
  .process-section {
    padding-right: 5%;
    padding-left: 5%;
  }

  .corporate-hero {
    min-height: 480px;
  }
}
</style>
