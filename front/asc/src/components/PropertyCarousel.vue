<template>
<section class="properties">

  <h2>Популярные объекты</h2>

  <div class="cards">
    <div class="card" v-for="i in 12" :key="i">

      <!-- Картинка -->
      <div class="card-image">
        <img src="../assets/house.png" alt="Объект недвижимости"/>
      </div>

      <!-- Информация с подложкой -->
      <div class="card-info">
        <div class="price">15 000 000 ₽</div>
        <h3>3-комнатная квартира</h3>
        <p class="address">Москва, ул. Тверская, д. 12, кв. 34</p>
        <p class="metro">Ближайшее метро: Маяковская</p>
      </div>

    </div>
  </div>

</section>
</template>

<style scoped>
.properties {
  padding: 40px 10%;
  background: #f9f9f9;
}

.properties h2 {
  font-family: "Playfair Display", serif;
  font-size: 32px;
  color: #2c3e50;
  margin-bottom: 32px;
  text-align: center;
}

/* Сетка карточек */
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

/* Карточка */
.card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 25px rgba(0,0,0,0.1);
  transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.15);
}

/* Картинка */
.card-image img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

/* Нижняя подложка */
.card-info {
  padding: 4px 16px 16px;
  position: relative;
  background: #fff;
}

/* Цена на верхней подложке */
.card-info .price {
  font-weight: bold;
  font-size: 24px;

  color: #111;
}

/* Заголовок */
.card-info h3 {
  font-family: "Playfair Display", serif;
  font-size: 18px;
  margin-bottom: 4px;
}

/* Адрес */
.card-info .address {
  font-size: 14px;
  color: #555;
  margin-bottom: 2px;
}

/* Ближайшее метро */
.card-info .metro {
  font-size: 13px;
  color: #777;
}
</style>