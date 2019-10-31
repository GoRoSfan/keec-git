<template>
  <mu-container class="main">
    <header>
      <img
        src=""
        alt="img"
        class="center-name-image"
      >
      <h1>ХЕРСОНСЬКИЙ НАУКОВО-ДОСЛІДНИЦЬКИЙ ЦЕНТР УЧНІВСЬКОЇ ТА СТУДЕНТСЬКОЇ МОЛОДІ</h1>
      <img
        src=""
        alt="img"
        class="center-name-image"
      >
    </header>
    <nav class="main-menu-list">
      <router-link tag="div" to="/news" class="main-menu-item">
        <div class="menu-item-name">Новини</div>
      </router-link>
      <router-link tag="div" to="/about" class="main-menu-item">
        <div class="menu-item-name">Про нас</div>
        <div class="sub-menu-list sub-menu-about">
          <router-link tag="div" to="/events" class="sub-menu-item">
            <div class="menu-item-name">Плани</div>
          </router-link>
          <router-link tag="div" to="/edumaterials" class="sub-menu-item">
            <div class="menu-item-name">Навчальні матеріали</div>
          </router-link>
          <router-link tag="div" to="/partners" class="sub-menu-item">
            <div class="menu-item-name">Партнери</div>
          </router-link>
          <router-link tag="div" to="/team" class="sub-menu-item">
            <div class="menu-item-name">Каманда</div>
          </router-link>
          <router-link tag="div" to="/contact" class="sub-menu-item">
            <div class="menu-item-name">Контакти</div>
          </router-link>
        </div>
      </router-link>
      <div class="main-menu-item">
        <div class="menu-item-name">Учасникам</div>
        <div class="sub-menu-list sub-menu-members">
          <router-link tag="div" to="/for_students" class="sub-menu-item">
            <div class="menu-item-name">Студентам</div>
          </router-link>
          <router-link tag="div" to="/for_parents" class="sub-menu-item">
            <div class="menu-item-name">Батькам</div>
          </router-link>
          <router-link tag="div" to="/for_partners" class="sub-menu-item">
            <div class="menu-item-name">Партнерам</div>
          </router-link>
        </div>
      </div>
      <router-link tag="div" to="/legal" class="main-menu-item">
        <div class="menu-item-name">Правова база</div>
      </router-link>
    </nav>
    <div class="content-container">
      <main>
        <slot name="main"></slot>
      </main>
      <aside>
        <div class="context-header">
          <span>Актуальна інформація</span>
        </div>
        <div class="last-news"></div>
        <div class="context-header">
          <span>Корисні ресурси</span>
        </div>
        <div class="helpful-links"></div>
      </aside>
    </div>
    <footer></footer>
  </mu-container>
</template>

<script>
  export default {
    name: 'Home',

    data() {
      return {
        test_tt: 'fafa',
      };
    },
  };
</script>

<style scoped>
  .test {
  }

  /*.main{*/
  /*display: -webkit-box;*/
  /*display: -moz-box;*/
  /*display: -ms-flexbox;*/
  /*display: -webkit-flex;*/
  /*display: flex;*/

  /*flex-direction: column;*/
  /*flex-wrap: nowrap;*/
  /*-webkit-flex-flow: column nowrap;*/

  /*width: 90vw;*/
  /*}*/

  header {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: center;

    background-color: #003366;
  }

  header h1 {
    padding: 0;
    margin: 2vh 1vw;

    font-size: 1.5rem;
    font-weight: 500;
    color: #ffcc99;
  }

  header .center-name-image {
    position: absolute;

    /*z-index: 1;*/
    /*width: 5%;*/
  }

  .main-menu-list {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: stretch;

    margin: 0;

    list-style: none;

    color: #556688;
    font-size: 1.3rem;

    background-color: #ffc64e;
  }

  .main-menu-list .main-menu-item {
    position: relative;

    padding: 1.5vh 2vw;

    border: solid #000 0;
    border-right-width: 3px;

    cursor: pointer;

    -webkit-transition: 0.5s ease-in-out;
    -moz-transition: 0.5s ease-in-out;
    -o-transition: 0.5s ease-in-out;
    transition: 0.5s ease-in-out;
  }

  .main-menu-list .main-menu-item:first-child {
    border-left-width: 3px;
  }

  .main-menu-list .main-menu-item:hover {
    padding: 1.5vh 5vw;

    background-color: #ffa453;
  }

  .main-menu-list .menu-item-name {
    color: #556688;
  }

  .main-menu-list .sub-menu-list {
    visibility: hidden;
    opacity: 0;

    position: absolute;
    top: 100%;
    left: 0;

    width: 100%;

    text-align: left;
    background-color: #003366;;

    z-index: 10;

    -webkit-transition: 0.5s ease-in-out;
    -moz-transition: 0.5s ease-in-out;
    -o-transition: 0.5s ease-in-out;
    transition: 0.5s ease-in-out;
  }

  .main-menu-list .main-menu-item:hover .sub-menu-list {
    visibility: visible;
    opacity: 1;
  }

  .main-menu-list .sub-menu-item {
    padding: 1vh 1vw;

    border-bottom: 2px solid #fff;

    cursor: pointer;
  }

  .main-menu-list .sub-menu-item:hover{
    padding: 2vh 1vw;

    background-color: #002953;
  }
  
  .main-menu-list .sub-menu-item .menu-item-name{
    color: #ffcc99;
  }

  .content-container {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: space-between;

    margin-top: 2vh;
  }

  main {
    width: 70%;

    padding: 0;
    margin: 0;
  }

  aside {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    flex-direction: column;
    flex-wrap: nowrap;
    -webkit-flex-flow: column nowrap;

    width: 25%;
    min-height: 70vh;
  }

  aside .context-header {
    display: none;
    margin: 1.5vh 0;

    font-size: 1.2rem;
  }

  .context-header:first-child {
    margin-top: 0;
  }

  @media (max-width: 755px) {
    main {
      width: 100%
    }

    aside {
      display: none
    }
  }
</style>
