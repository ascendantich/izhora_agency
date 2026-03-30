<template>
  <header class="header">
    <router-link to="/" class="logo" aria-label="ИЖОРА — главная">
      <img src="@/assets/logo.svg" alt="ИЖОРА" />
    </router-link>

    <nav class="nav">
      <router-link to="/">Главная</router-link>
      <router-link to="/objects">Объекты</router-link>
      <router-link to="/mortgage">Ипотека</router-link>
      <router-link to="/corporate">Корпоративным</router-link>
      <router-link to="/documents">Документы</router-link>
      <router-link to="/about">О нас</router-link>
    </nav>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 24px;
  padding: 10px 10%;
  background: white;
}

.logo {
  display: flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
}

.logo img {
  height: 56px;
  width: auto;
}

.nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-items: center;
  gap: 8px;
}

.nav a {
  text-decoration: none;
  color: #4c6093;
  transition: 0.3s;
  padding: 8px 12px;
  border-radius: 999px;
  font-size: 0.98rem;
}

.nav a:hover {
  background-color: rgba(61, 136, 255, 0.1);
  color: #3769e9;
}

@media (max-width: 980px) {
  .header {
    padding-right: 5%;
    padding-left: 5%;
    align-items: flex-start;
    flex-direction: column;
  }

  .nav {
    width: 100%;
    justify-content: flex-start;
  }
}
</style>
