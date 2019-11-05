<template>
  <article class="block-container">
    <header>
      <cite>{{block.title}}</cite>
      <time>{{block.post_date}}</time>
    </header>
    <main>
      <img :src="host + block.image" :alt="'Основне зображення' + block.title">
      <div class="block-description">{{block.description}}</div>
    </main>
    <footer>
      <button><a :href="host + block.detail">Детальніше...</a></button>
    </footer>
  </article>
</template>

<script>
  export default {
    name: "ContentBlock",

    props: ['block'],

    data: function () {
      return {
        host: window.location.protocol.concat('//127.0.0.1:8000'),
      };
    },


  }
</script>

<style scoped>
  .block-container {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    flex-direction: column;
    flex-wrap: nowrap;
    -webkit-flex-flow: column nowrap;

    margin: 2vh 0;
  }

  .block-container header {
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    justify-content: space-between;

    padding: 0.8vh 2vw;

    color: #3914AF;

    border-radius: 2vw 2vw 0 0;
    border-bottom: #FFD300 solid 1px;

    -webkit-box-shadow: inset 0 -1px #646464;
    -moz-box-shadow: inset 0 -1px #646464;
    box-shadow: inset 0 -1px #646464;

    background-color: #FFD300;
  }

  .block-container header cite {
    align-self: center;

    font-style: normal;
    font-size: 1.5rem;
  }

  .block-container header time {
    align-self: start;

    font-size: 1rem;
  }

  .block-container main {
    padding: 1.5vh 1.5vw;

    color: #FFE773;
    text-align: left;
    font-size: 1.2rem;

    background-color: #311491;
  }

  .block-container main img {
    width: 30%;
    float: right;
  }

  .block-container footer {
    text-align: left;

    padding: 1.5vh 2vw;

    border-radius: 0 0 2vw 2vw;

    background-color: #FFD300;
  }

  .block-container footer button {
    background-color: #FFE773;
  }

  .block-container footer button a {
    color: #000;
    font-size: 1.1rem;
  }
</style>
