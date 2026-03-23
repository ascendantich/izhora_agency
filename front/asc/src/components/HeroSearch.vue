<template>
<section class="hero">

  <div class="hero-content">

    <h1>Найдите идеальную недвижимость</h1>
    <p>Квартиры, дома и коммерческая недвижимость</p>

    <div class="search-box">

      <input 
        type="text"
        placeholder="Город, район, метро, ЖК"
      />

      <button>
        Найти
      </button>

    </div>

    <div class="categories">

      <button>Купить</button>
      <button>Снять</button>
      <button>Новостройки</button>
      <button>Дома</button>
      <button>Коммерция</button>

    </div>

  </div>

</section>
</template>

<style scoped>

.hero{
  height:80vh;
  background-image: 
    linear-gradient(rgba(0, 0, 0, 0.2), rgba(51, 51, 51, 0.1)),
    url('../assets/hero.png');
  background-size: cover;
  background-size:cover;
  background-position:center 40%;
  display:flex;
  align-items:center;
  justify-content:center;
}

.hero-content{
  text-align:center;
  max-width:800px;
}

.hero h1{
  font-size:48px;
  font-weight: bold;
  color:white;
  margin-bottom:12px;
  line-height: 1.2;
}

.hero p{
  font-size:18px;
  color:white;
  margin-bottom:30px;
}

.search-box{
  display:flex;
  background:white;
  border-radius:12px;
  overflow:hidden;
}

.search-box input{
  flex:1;
  padding:18px;
  border:none;
  font-size:16px;
}

.search-box button{
  padding:18px 30px;
  background:#4C6093;
  color:white;
  border:none;
  transition: background-color 0.3s ease;
}
button:hover {
  background: #5875c3;
}
.categories{
  margin-top:20px;
}

.categories button{
  margin:6px;
  padding:10px 18px;
  border-radius:20px;
  border:none;
  background:#ffffffcc;
}

</style>