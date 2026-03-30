<template>
  <div class="mortgage-page">
    <Header />

    <section class="mortgage-hero">
      <div class="hero-copy">
        <span class="eyebrow">Ипотечные решения</span>
        <h1>Подберем ипотеку под объект, бюджет и ваш сценарий покупки</h1>

        <div class="hero-points">
          <p>Ставка от <strong>7,9%</strong> годовых</p>
          <p>Срок до <strong>30 лет</strong></p>
          <p>Первоначальный взнос от <strong>15%</strong></p>
        </div>

        <p class="hero-description">
          Сопровождаем клиента от предварительного одобрения до сделки: подбираем банк, объясняем условия и собираем
          наиболее выгодный сценарий под конкретный объект.
        </p>

        <div class="hero-actions">
          <button type="button">Получить одобрение</button>
          <a href="#banks">Смотреть банки</a>
        </div>
      </div>

      <div class="hero-visual">
        <img :src="heroImage" alt="Ипотека на выгодных условиях" />

        <div class="visual-card">
          <span>Средний срок решения</span>
          <strong>от 1 рабочего дня</strong>
          <p>Быстро понимаем лимит, ежемесячный платеж и реальные варианты по объекту.</p>
        </div>
      </div>
    </section>

    <section class="mortgage-highlights">
      <article v-for="item in highlights" :key="item.label" class="highlight-card">
        <span>{{ item.label }}</span>
        <strong>{{ item.value }}</strong>
      </article>
    </section>

    <section id="banks" class="banks-section">
      <div class="section-head">
        <div>
          <h2>Партнерские банки</h2>
          <p>Работаем с банками, которые дают понятные условия и хорошо проводят сделки по городской недвижимости.</p>
        </div>
      </div>

      <div class="banks-grid">
        <article v-for="bank in banks" :key="bank.name" class="bank-card">
          <div class="bank-logo">
            <img :src="bank.image" :alt="bank.name" />
          </div>
          <p>{{ bank.name }}</p>
        </article>
      </div>
    </section>

    <section class="benefits-section">
      <div class="section-head">
        <div>
          <h2>Что мы берем на себя</h2>
          <p>Не просто отправляем заявку в банк, а выстраиваем понятный маршрут до одобрения и сделки.</p>
        </div>
      </div>

      <div class="benefits-grid">
        <article v-for="item in benefits" :key="item.title" class="benefit-card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.description }}</p>
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
import heroImage from '@/assets/ipoteka.png'
import alfaBankImage from '@/assets/banks/alfa.png'
import gazpromBankImage from '@/assets/banks/gazprom.png'
import rosselhozBankImage from '@/assets/banks/rosselhoz.png'
import sberBankImage from '@/assets/banks/sber.png'
import vtbBankImage from '@/assets/banks/vtb.png'

const banks = [
  { name: 'Сбер', image: sberBankImage },
  { name: 'ВТБ', image: vtbBankImage },
  { name: 'Альфа-Банк', image: alfaBankImage },
  { name: 'Газпромбанк', image: gazpromBankImage },
  { name: 'Россельхозбанк', image: rosselhozBankImage },
]

const highlights = [
  { label: 'Одобрение заранее', value: 'до выбора квартиры' },
  { label: 'Работаем с первичкой и вторичкой', value: 'один маршрут сделки' },
  { label: 'Сравниваем программы', value: 'а не один банк' },
]

const benefits = [
  {
    title: 'Подбор программы под лот',
    description: 'Смотрим не только ставку, но и требования банка к конкретному объекту и типу сделки.',
  },
  {
    title: 'Экономия времени',
    description: 'Сразу собираем понятный пакет документов и убираем лишние итерации с банками.',
  },
  {
    title: 'Сопровождение до выдачи',
    description: 'Держим коммуникацию с банком, продавцом и юристами до самого подписания документов.',
  },
]
</script>

<style scoped>
.mortgage-page {
  background: #f9f9f9;
}

.mortgage-hero {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(360px, 0.8fr);
  gap: 32px;
  padding: 44px 10% 28px;
}

.hero-copy {
  display: grid;
  align-content: center;
  gap: 20px;
}

.eyebrow {
  width: fit-content;
  border-radius: 999px;
  background: rgba(76, 96, 147, 0.12);
  color: #35508e;
  padding: 8px 12px;
  font-size: 0.92rem;
  font-weight: 600;
}

.hero-copy h1 {
  margin: 0;
  font-family: 'Playfair Display', serif;
  font-size: clamp(2rem, 3.2vw, 3.5rem);
  line-height: 1.02;
  font-weight: 400;
  color: #103754;
}

.hero-points {
  display: grid;
  gap: 8px;
}

.hero-points p {
  margin: 0;
  font-size: clamp(1.15rem, 1.7vw, 1.65rem);
  line-height: 1.15;
  color: #0c3f63;
}

.hero-points strong {
  font-weight: 700;
}

.hero-description {
  max-width: 700px;
  margin: 0;
  line-height: 1.7;
  color: #607081;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.hero-actions button,
.hero-actions a {
  border-radius: 12px;
  padding: 15px 20px;
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
  background: #eef2fb;
  color: #35508e;
}

.hero-visual {
  position: relative;
  min-height: 520px;
  overflow: hidden;
  border-radius: 28px;
  background: #474747;
  box-shadow: 0 18px 40px rgba(44, 62, 80, 0.12);
}

.hero-visual img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.visual-card {
  position: absolute;
  left: 24px;
  right: 24px;
  bottom: 24px;
  display: grid;
  gap: 8px;
  padding: 18px 20px;
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.92);
  backdrop-filter: blur(10px);
}

.visual-card span {
  color: #607081;
}

.visual-card strong {
  font-size: 1.6rem;
  color: #1f2937;
}

.visual-card p {
  margin: 0;
  line-height: 1.6;
  color: #607081;
}

.mortgage-highlights,
.banks-section,
.benefits-section {
  padding: 0 10% 56px;
}

.mortgage-highlights {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.highlight-card {
  display: grid;
  gap: 10px;
  padding: 22px;
  border-radius: 20px;
  background: #ffffff;
  box-shadow: 0 14px 34px rgba(44, 62, 80, 0.08);
}

.highlight-card span {
  color: #607081;
}

.highlight-card strong {
  font-size: 1.3rem;
  color: #1f2937;
}

.section-head {
  margin-bottom: 24px;
}

.section-head h2 {
  margin: 0 0 10px;
  font-family: 'Playfair Display', serif;
  font-size: 2.4rem;
  font-weight: 400;
  color: #2c3e50;
}

.section-head p {
  max-width: 760px;
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.banks-grid {
  display: grid;
  grid-template-columns: repeat(5, minmax(0, 1fr));
  gap: 18px;
}

.bank-card,
.benefit-card {
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(91, 111, 167, 0.08);
}

.bank-card {
  display: grid;
  justify-items: center;
  align-content: center;
  gap: 18px;
  padding: 22px;
  overflow: hidden;
  border-radius: 28px;
  min-height: 220px;
}

.bank-logo {
  display: grid;
  place-items: center;
  width: 150px;
  height: 150px;
  overflow: hidden;
  border-radius: 50%;
  background: #ffffff;
  box-shadow: inset 0 0 0 1px rgba(148, 163, 184, 0.18);
}

.bank-logo img {
  display: block;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bank-card p {
  margin: 0;
  font-size: 1.1rem;
  font-weight: 600;
  color: #334155;
}

.benefits-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 18px;
}

.benefit-card {
  padding: 24px;
  border-radius: 20px;
}

.benefit-card h3 {
  margin: 0 0 12px;
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 400;
  color: #2c3e50;
}

.benefit-card p {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

@media (max-width: 1180px) {
  .mortgage-hero,
  .mortgage-highlights,
  .banks-grid,
  .benefits-grid {
    grid-template-columns: 1fr 1fr;
  }

  .mortgage-hero {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .mortgage-hero,
  .mortgage-highlights,
  .banks-section,
  .benefits-section {
    padding-right: 5%;
    padding-left: 5%;
  }

  .mortgage-highlights,
  .banks-grid,
  .benefits-grid {
    grid-template-columns: 1fr;
  }

  .hero-visual {
    min-height: 340px;
  }
}
</style>
