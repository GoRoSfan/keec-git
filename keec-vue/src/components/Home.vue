<template>
  <mu-container class="main-container">
    <mu-col span="12" justify-content="center">text text text text text text text text</mu-col>
    <mu-appbar class="header" color="primary">
      <mu-flex class="menu-list">
        <mu-flex justify-content="center" class="menu-item" fill>
          <mu-menu class="">
            Новини
          </mu-menu>
        </mu-flex>
        <mu-flex justify-content="center" class="menu-item" fill>План роботи</mu-flex>
        <mu-flex justify-content="center" class="menu-item" fill>Додатково</mu-flex>
      </mu-flex>
    </mu-appbar>
    <mu-row>
      <mu-col span="9" class="main-container s" color="primary"></mu-col>
      <mu-flex class="" direction="row-reverse" fill>
        <mu-col span="9" class="sidebar s" color="primary" align-self="end">
          <mu-row class="last-news" color="primary"></mu-row>
          <mu-row class="helpful-links" color="primary"></mu-row>
        </mu-col>
      </mu-flex>
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

  .sidebar{
    height: 150px;
    justify-self: right;
  }

  .menu-item{
    line-height: 1.2;
  }
  /*.main-container{*/
    /*margin: 0px;*/
    /*padding: 0px;*/
  /*}*/
</style>
