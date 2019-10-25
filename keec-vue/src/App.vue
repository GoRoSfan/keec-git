<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
  html {
    min-width: 240px;

    font-size: 15px;
  }


  body{
    margin: 0;
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    justify-content: center;

    background-color: #ffcc99;
  }

  h2{
    margin: 0;

    font-size: 1.4rem;
    font-weight: 400;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 5vmin;
  }

  .context-header{
    text-align: center;
    color: #ffcc99;

    border-radius: 2.5vw 0;
    background-color: #133568;
  }

  @media (max-width: 1180px) {
    html{font-size: 12px;}
  }

  @media (max-width: 600px) {
    html{font-size: 10px;}
  }

  @media (max-width: 400px) {
    html{font-size: 8px;}
  }
</style>
