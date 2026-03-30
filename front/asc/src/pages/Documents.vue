<template>
  <div class="documents-page">
    <Header />

    <section class="documents-hero">
      <span class="eyebrow">Материалы и регламенты</span>
      <h1>Документы</h1>
      <p class="documents-subtitle">
        Важные материалы по сопровождению сделок, условиям обслуживания и работе агентства.
      </p>
    </section>

    <section class="documents-section">
      <div class="documents-grid">
        <article v-for="item in documents" :key="item.title" class="document-card">
          <div class="document-top">
            <div class="document-icon">
              <img :src="item.icon" :alt="item.title" />
            </div>

            <span class="document-tag">{{ item.tag }}</span>
          </div>

          <h2>{{ item.title }}</h2>
          <p class="document-text">{{ item.description }}</p>

          <a class="download-button" :href="item.href" download>
            <img :src="pdfIcon" alt="" aria-hidden="true" />
            <span>Скачать pdf</span>
          </a>
        </article>
      </div>
    </section>

    <section class="documents-note">
      <div class="note-card">
        <h2>Нужен документ под конкретную сделку?</h2>
        <p>Подскажем, какой файл нужен именно в вашем сценарии, и быстро отправим актуальную версию менеджером.</p>
      </div>
    </section>

    <Footer />
  </div>
</template>

<script setup lang="ts">
import Header from '@/components/Header.vue'
import Footer from '@/components/Footer.vue'
import documentIcon from '@/assets/icons/document.svg'
import infoAboutIcon from '@/assets/icons/info_about.svg'
import pdfIcon from '@/assets/icons/pdf.svg'
import policyIcon from '@/assets/icons/policy.svg'

const documents = [
  {
    title: 'О компании',
    description: 'Краткая информация об агентстве, специализации и формате сопровождения сделок.',
    tag: 'Компания',
    icon: infoAboutIcon,
    href: '#',
  },
  {
    title: 'Политика конфиденциальности',
    description: 'Порядок обработки персональных данных и правила работы с пользовательской информацией.',
    tag: 'Юридический документ',
    icon: policyIcon,
    href: '#',
  },
  {
    title: 'Договор возмездного оказания услуг',
    description: 'Базовый договор на сопровождение, консультации и агентские услуги по объектам недвижимости.',
    tag: 'Сделка и сопровождение',
    icon: documentIcon,
    href: '#',
  },
]
</script>

<style scoped>
.documents-page {
  min-height: 100vh;
  background: #f9f9f9;
}

.documents-hero,
.documents-section,
.documents-note {
  padding: 0 10%;
}

.documents-hero {
  display: grid;
  justify-items: center;
  text-align: center;
  padding-top: 56px;
  padding-bottom: 34px;
}

.eyebrow {
  margin-bottom: 16px;
  border-radius: 999px;
  background: rgba(76, 96, 147, 0.12);
  color: #35508e;
  padding: 8px 12px;
  font-size: 0.92rem;
  font-weight: 600;
}

.documents-hero h1 {
  margin: 0 0 14px;
  font-family: 'Playfair Display', serif;
  font-size: 3.1rem;
  font-weight: 400;
  color: #54515f;
}

.documents-subtitle {
  max-width: 760px;
  margin: 0;
  line-height: 1.7;
  color: #7a7f8e;
}

.documents-section {
  padding-bottom: 108px;
}

.documents-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 28px;
  max-width: 1200px;
  margin: 0 auto;
}

.document-card,
.note-card {
  background: #ffffff;
  box-shadow: 0 16px 36px rgba(91, 111, 167, 0.08);
}

.document-card {
  display: flex;
  flex-direction: column;
  min-height: 360px;
  padding: 24px;
  border-radius: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.document-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.document-top {
  display: flex;
  justify-content: space-between;
  align-items: start;
  gap: 16px;
  margin-bottom: 18px;
}

.document-icon {
  display: grid;
  place-items: center;
  width: 76px;
  height: 76px;
}

.document-icon img {
  width: 64px;
  height: 64px;
  object-fit: contain;
}

.document-tag {
  border-radius: 999px;
  background: #eef2fb;
  color: #35508e;
  padding: 8px 12px;
  font-size: 0.88rem;
  font-weight: 600;
}

.document-card h2 {
  margin: 0 0 12px;
  font-family: 'Playfair Display', serif;
  font-size: 1.65rem;
  line-height: 1.12;
  color: #2c3e50;
}

.document-text {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.download-button {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  align-self: stretch;
  width: 100%;
  margin-top: auto;
  border-radius: 12px;
  background: #5b6fa7;
  color: #fff;
  padding: 14px 18px;
  text-align: center;
  text-decoration: none;
  font-weight: 600;
  transition: background-color 0.2s ease, transform 0.2s ease;
}

.download-button img {
  width: 18px;
  height: 18px;
  object-fit: contain;
}

.download-button:hover {
  background: #4c6093;
  transform: translateY(-1px);
}

.documents-note {
  padding-bottom: 120px;
}

.note-card {
  max-width: 1200px;
  margin: 0 auto;
  padding: 28px;
  border-radius: 22px;
}

.note-card h2 {
  margin: 0 0 12px;
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 400;
  color: #2c3e50;
}

.note-card p {
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

@media (max-width: 1100px) {
  .documents-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .documents-hero,
  .documents-section,
  .documents-note {
    padding-right: 5%;
    padding-left: 5%;
  }

  .documents-section {
    padding-bottom: 72px;
  }

  .documents-note {
    padding-bottom: 80px;
  }

  .documents-hero h1 {
    font-size: 2.4rem;
  }
}
</style>
