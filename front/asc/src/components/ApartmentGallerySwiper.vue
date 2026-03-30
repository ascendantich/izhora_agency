<template>
  <section class="apartment-gallery">
    <div class="gallery-layout">
      <div class="gallery-column">
        <h1>Фотографии объекта</h1>

        <Swiper
          :modules="[Scrollbar, Mousewheel, FreeMode]"
          :slides-per-view="1.15"
          :space-between="18"
          :breakpoints="breakpoints"
          :free-mode="true"
          :mousewheel="{ forceToAxis: true, releaseOnEdges: true }"
          :scrollbar="{ draggable: true }"
          grab-cursor
          watch-overflow
          class="apartment-gallery-swiper"
        >
          <SwiperSlide v-for="slide in slides" :key="slide.id">
            <div class="slide-card">
              <img :src="slide.image" :alt="slide.alt" />
            </div>
          </SwiperSlide>
        </Swiper>
      </div>

      <aside class="plan-column">
        <h2>Планировка</h2>

        <article class="plan-card">
          <img :src="planImage" alt="Выбранная планировка" />
        </article>
      </aside>
    </div>
  </section>
</template>

<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import { FreeMode, Mousewheel, Scrollbar } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/free-mode'
import 'swiper/css/scrollbar'

import heroImage from '@/assets/hero.png'
import planImage from '@/assets/house.png'

const slides = [
  { id: 1, image: heroImage, alt: 'Фотография дома 1' },
  { id: 2, image: heroImage, alt: 'Фотография дома 2' },
  { id: 3, image: heroImage, alt: 'Фотография дома 3' },
  { id: 4, image: heroImage, alt: 'Фотография дома 4' },
]

const breakpoints = {
  768: {
    slidesPerView: 1.35,
    spaceBetween: 18,
  },
  1100: {
    slidesPerView: 2,
    spaceBetween: 20,
  },
}
</script>

<style scoped>
.apartment-gallery {
  padding: 48px 0 28px;
}

.gallery-layout {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(280px, 1fr);
  gap: 20px;
  align-items: start;
}

.gallery-column h1,
.plan-column h2 {
  margin-bottom: 28px;
  font-family: 'Playfair Display', serif;
  font-weight: 400;
  color: #54515f;
}

.gallery-column h1 {
  font-size: 2.4rem;
}

.plan-column h2 {
  font-size: 2.35rem;
  text-align: center;
}

.apartment-gallery-swiper {
  padding-bottom: 28px;
}

.slide-card,
.plan-card {
  overflow: hidden;
  border-radius: 16px;
}

.slide-card {
  background: #474747;
}

.plan-card {
  background: #8b8b8b;
}

.slide-card img,
.plan-card img {
  display: block;
  width: 100%;
  height: 420px;
  object-fit: cover;
}

:deep(.swiper-scrollbar) {
  left: 0;
  width: 100%;
  height: 5px;
  background: rgba(148, 163, 184, 0.28);
}

:deep(.swiper-scrollbar-drag) {
  background: #3f3f46;
}

@media (max-width: 900px) {
  .gallery-layout {
    grid-template-columns: 1fr;
  }

  .gallery-column h1,
  .plan-column h2 {
    text-align: left;
  }

  .plan-column {
    max-width: 420px;
  }
}

@media (max-width: 767px) {
  .apartment-gallery {
    padding-top: 32px;
  }

  .gallery-column h1 {
    font-size: 2rem;
  }

  .plan-column h2 {
    font-size: 1.85rem;
  }

  .slide-card img,
  .plan-card img {
    height: 280px;
  }
}
</style>
