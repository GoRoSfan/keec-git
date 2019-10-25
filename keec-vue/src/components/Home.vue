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
    <nav class="menu-list">
      <router-link tag="div" to="/news" class="menu-item">
        <a>Новини</a>
      </router-link>
      <router-link tag="div" to="/events" class="menu-item">
        <a>План роботи</a>
      </router-link>
      <router-link tag="div" to="/about" class="menu-item">
        <a>Про нас</a>
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
  .test{
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

  header{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: center;

    background-color: #003366;
  }

  header h1{
    padding: 0;
    margin: 2vh 1vw;

    font-size: 1.5rem;
    font-weight: 500;
    color: #ffcc99;
  }

  .center-name-image{
    position: absolute;

    /*z-index: 1;*/
    /*width: 5%;*/
  }

  .menu-list{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: space-around;

    padding: 1.5vh 0;
    margin: 0;

    list-style: none;

    color: #556688;
    font-size: 1.5rem;

    background-color: #ffc64e;
  }

  .menu-item a{
    color: #556688;
  }

  .content-container{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: space-between;

    margin-top: 2vh;
  }

  main{
    width: 70%;

    padding: 0;
    margin: 0;
  }

  aside{
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

  aside .context-header{
    display: none;
    margin: 1.5vh 0;

    font-size: 1.2rem;
  }

  .context-header:first-child{
    margin-top: 0;
  }

  @media (max-width: 755px){
    main{width: 100%}

    aside{display: none}
  }
</style>
