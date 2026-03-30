<template>
  <section class="house-gallery">
    <h1>{{ title }}</h1>

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
      class="house-gallery-swiper"
    >
      <SwiperSlide v-for="slide in slides" :key="slide.id">
        <div class="slide-card">
          <img :src="slide.image" :alt="slide.alt" />
        </div>
      </SwiperSlide>
    </Swiper>
  </section>
</template>

<script setup lang="ts">
import { Swiper, SwiperSlide } from 'swiper/vue'
import { FreeMode, Mousewheel, Scrollbar } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/free-mode'
import 'swiper/css/scrollbar'

import houseImage from '@/assets/house.png'

withDefaults(
  defineProps<{
    title?: string
  }>(),
  {
    title: 'Название объекта',
  },
)

const slides = [
  { id: 1, image: houseImage, alt: 'Фотография объекта 1' },
  { id: 2, image: houseImage, alt: 'Фотография объекта 2' },
  { id: 3, image: houseImage, alt: 'Фотография объекта 3' },
  { id: 4, image: houseImage, alt: 'Фотография объекта 4' },
]

const breakpoints = {
  768: {
    slidesPerView: 2.2,
    spaceBetween: 18,
  },
  1100: {
    slidesPerView: 3,
    spaceBetween: 20,
  },
}
</script>

<style scoped>
.house-gallery {
  padding: 48px 0 28px;
}

.house-gallery h1 {
  margin-bottom: 28px;
  text-align: center;
  font-family: 'Playfair Display', serif;
  font-size: 2.5rem;
  font-weight: 400;
  color: #54515f;
}

.house-gallery-swiper {
  padding-bottom: 28px;
}

.slide-card {
  overflow: hidden;
  border-radius: 16px;
  background: #474747;
}

.slide-card img {
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

@media (max-width: 767px) {
  .house-gallery {
    padding-top: 32px;
  }

  .house-gallery h1 {
    font-size: 2rem;
  }

  .slide-card img {
    height: 280px;
  }
}
</style>
