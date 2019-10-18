<template>
  <mu-container class="main" id="main">
    <div class="center-name">
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
    </div>
    <div class="menu-list">
      <router-link tag="div" to="/news" class="menu-item">
        <a>Новини</a>
      </router-link>
      <router-link tag="div" to="/events" class="menu-item">
        <a>План роботи</a>
      </router-link>
      <router-link tag="div" to="/about" class="menu-item">
        <a>Про нас</a>
      </router-link>
    </div>
    <div class="content-container">
      <div class="theme-container">
        <slot name="main"></slot>
      </div>
      <div class="sidebar">
        <div class="sub-header">Актуальна інформація</div>
        <div class="last-news"></div>
        <div class="sub-header">Корисні ресурси</div>
        <div class="helpful-links"></div>
      </div>
    </div>
  </mu-container>
</template>

<script>
export default {
  name: 'Home',

  data() {
    return {
      test_tt: 'fafa',
    }
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

  .center-name{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    justify-content: center;

    background-color: #003366;
  }

  .center-name h1{
    padding: 0;
    margin: 3vmin 1vmin;

    font-size: 1.5rem;
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

    padding: 2vmin 0;
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

    margin-top: 2vw;
  }

  .theme-container{
    width: 70%;

    padding: 0;
    margin: 0;
    border: black solid 0;
  }

  .sidebar{
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

  .sub-header{
    margin: 2vmin 0;

    text-align: center;

    border-radius: 10px 0;

    color: #ffcc99;
    font-size: 1.2rem;



    background-color: #133568;
  }


  .sub-header:first-child{
    margin-top: 0;
  }

  @media (max-width: 755px){
    .theme-container{width: 100%}

    .sidebar{display: none}
  }
</style>
