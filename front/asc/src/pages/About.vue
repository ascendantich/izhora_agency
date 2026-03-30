<template>
  <div class="about-page">
    <Header />

    <section class="team-section top-team">
      <div class="section-head centered">
        <h2>Наша команда</h2>
        <p>Профессионалы, которым можно доверять.</p>
      </div>

      <div class="team-grid">
        <article v-for="member in teamMembers" :key="member.name" class="team-card">
          <div class="card-image">
            <img :src="member.photo" :alt="member.name" />
          </div>
          <div class="card-info">
            <h3>{{ member.name }}</h3>  
            <p class="position">{{ member.position }}</p>
            <p class="experience">Опыт: {{ member.experience }} лет</p>
            <p class="phone">{{ member.phone }}</p>
          </div>
        </article>
      </div>
    </section>

    <section class="metrics-section">
      <article v-for="item in metrics" :key="item.label" class="metric-card">
        <span>{{ item.label }}</span>
        <strong>{{ item.value }}</strong>
      </article>
    </section>

    <section class="values-section">
      <div class="section-head centered">
        <h2>Почему выбирают нас</h2>
      </div>

      <div class="values-grid">
        <article v-for="item in values" :key="item.title" class="value-item">
          <div class="value-icon">
            <img :src="item.icon" :alt="item.title" />
          </div>
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
import annaPhoto from '@/assets/anna.png'
import dmitryPhoto from '@/assets/dmitry.png'
import elenaPhoto from '@/assets/elena.png'
import petrPhoto from '@/assets/petr.png'
import cupIcon from '@/assets/icons/cup.svg'
import graphIcon from '@/assets/icons/graph.svg'
import handshakeIcon from '@/assets/icons/handshake.svg'
import lightningIcon from '@/assets/icons/lightning.svg'
import scalesIcon from '@/assets/icons/scales.svg'
import supportIcon from '@/assets/icons/support.svg'

const metrics = [
  { label: 'На рынке', value: '15 лет' },
  { label: 'Формат', value: 'Жилая и коммерческая недвижимость' },
  { label: 'Сопровождение', value: 'от первого звонка до ключей' },
]

const teamMembers = [
  {
    name: 'Анна Иванова',
    position: 'Генеральный директор',
    experience: 15,
    phone: '+7 (999) 123-45-67',
    photo: annaPhoto,
  },
  {
    name: 'Петр Смирнов',
    position: 'Руководитель отдела продаж',
    experience: 10,
    phone: '+7 (999) 234-56-78',
    photo: petrPhoto,
  },
  {
    name: 'Елена Козлова',
    position: 'Ведущий риэлтор',
    experience: 12,
    phone: '+7 (999) 345-67-89',
    photo: elenaPhoto,
  },
  {
    name: 'Дмитрий Новиков',
    position: 'Риэлтор по коммерции',
    experience: 8,
    phone: '+7 (999) 456-78-90',
    photo: dmitryPhoto,
  },
]

const values = [
  {
    title: '15 лет на рынке',
    description: 'Работаем с недвижимостью с 2010 года, знаем все тонкости рынка.',
    icon: cupIcon,
  },
  {
    title: 'Юридическая чистота',
    description: 'Каждую сделку проверяют опытные юристы. Никаких рисков.',
    icon: scalesIcon,
  },
  {
    title: 'Индивидуальный подход',
    description: 'Подбираем стратегию под бюджет, сроки, формат покупки и реальную цель клиента.',
    icon: handshakeIcon,
  },
  {
    title: 'Быстрые сделки',
    description: 'Собираем процесс так, чтобы не тратить время на хаотичные показы и лишние согласования.',
    icon: lightningIcon,
  },
  {
    title: 'Актуальная база',
    description: 'Работаем только с понятными объектами и даем честную картину по каждому предложению.',
    icon: graphIcon,
  },
  {
    title: 'Поддержка 24/7',
    description: 'Остаемся на связи на всех этапах: от первых просмотров до выдачи ключей.',
    icon: supportIcon,
  },
]

</script>

<style scoped>
.about-page {
  background: #f9f9f9;
}

.metrics-section,
.team-section,
.values-section {
  padding: 0 10% 56px;
}

.metrics-section {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 16px;
}

.top-team {
  padding-top: 56px;
}

.metric-card,
.team-card,
.value-item {
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
  font-size: 1.25rem;
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
  max-width: 760px;
  margin: 0;
  line-height: 1.7;
  color: #667085;
}

.section-head.centered {
  text-align: center;
}

.section-head.centered p {
  margin: 0 auto;
}

.values-section .section-head {
  margin-bottom: 52px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 24px;
}

.team-card {
  border-radius: 18px;
  overflow: hidden;
  transition: transform 0.3s, box-shadow 0.3s;
  text-align: left;
}

.team-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
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
  margin: 0 0 6px;
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 400;
  color: #2c3e50;
}

.position {
  font-size: 0.98rem;
  color: #3b82f6;
  font-weight: 600;
  margin: 0 0 10px;
}

.experience,
.phone {
  margin: 0 0 6px;
  color: #5f6b7a;
}

.phone {
  font-weight: 600;
  color: #2c3e50;
}

.values-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 24px;
}

.value-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 34px 24px;
  border-radius: 20px;
  transition: transform 0.3s, box-shadow 0.3s;
}

.value-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.value-icon {
  margin-bottom: 22px;
  height: 72px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.value-icon img {
  width: 64px;
  height: 64px;
  object-fit: contain;
}

.value-item h3 {
  margin: 0 0 12px;
  font-family: 'Playfair Display', serif;
  font-size: 24px;
  color: #2c3e50;
}

.value-item p {
  margin: 0;
  font-size: 16px;
  line-height: 1.7;
  color: #666;
}

@media (max-width: 1200px) {
  .metrics-section,
  .team-grid,
  .values-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }

}

@media (max-width: 768px) {
  .top-team,
  .metrics-section,
  .team-section,
  .values-section {
    padding-right: 5%;
    padding-left: 5%;
  }

  .metrics-section {
    padding-top: 0;
  }

  .metrics-section,
  .team-grid,
  .values-grid {
    grid-template-columns: 1fr;
  }

  .value-item {
    padding: 28px 18px;
  }

  .value-icon {
    height: 60px;
    margin-bottom: 18px;
  }

  .value-icon img {
    width: 52px;
    height: 52px;
  }
}
</style>
