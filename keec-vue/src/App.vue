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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 5vmin;
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

  html{
    font-size: 1vw;
  }

  @media (max-width: 1000px) {
    html{font-size: 12px;}
  }

  @media (max-width: 600px) {
    html{font-size: 10px;}
  }

  @media (max-width: 400px) {
    html{font-size: 8px;}
  }
</style>
