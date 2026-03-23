<template>
  <header class="header">
    <a href="/" class="logo">
      <img src="@/assets/logo.svg" alt="ИЖОРА">
    </a>

    <nav>
      <router-link to="/" exact-active-class="active">Купить</router-link>
      <router-link to="/rent" exact-active-class="active">Снять</router-link>
      <router-link to="/new" exact-active-class="active">Новостройки</router-link>
      <router-link to="/about" exact-active-class="active">О нас</router-link>
      <router-link to="/contact" exact-active-class="active">Контакты</router-link>
    </nav>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  padding: 10px 10%;
  background: white;
}

.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.logo img {
  height: 56px;
  width: auto;
}

nav a {
  text-decoration: none;
  color: #4C6093;
  transition: 0.4s;
  padding: 8px 8px;
  border-radius: 999px;
  margin-left: 20px;
}

nav a:hover {
  background-color: rgba(61, 136, 255, 0.1);
    color: #3769E9;
}

nav {
  display: flex;
  align-items: center;
}
</style>