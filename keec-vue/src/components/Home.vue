<template>
  <mu-container class="main-container">
    <mu-appbar class="header" color="primary"></mu-appbar>
    <mu-appbar class="header" color="primary">
      <mu-col span="3" class="mu-menu m">Новини</mu-col>
      <mu-col span="3" class="mu-menu m">План роботи</mu-col>
      <mu-col span="3" class="mu-menu m">Додатково</mu-col>
    </mu-appbar>
    <mu-row gutter>
      <mu-col span="9" class="main-container" color="primary"><div class="s"></div></mu-col>
      <mu-col span="3" class="sidebar s" color="primary">
        <mu-row class="last-news" color="primary s"></mu-row>
        <mu-row class="helpful-links" color="primary"></mu-row>
      </mu-col>
    </mu-row>
  </mu-container>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
  .s{
    border: black solid 3px;
    height: 400px;
    background-color: cyan ;
  }
  /*.main-container{*/
    /*margin: 0px;*/
    /*padding: 0px;*/
  /*}*/
</style>
