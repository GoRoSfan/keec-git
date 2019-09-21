<template>
  <mu-container class="main">
    <mu-appbar justify-content="center" z-depth="0">text text text text text text text text</mu-appbar>
    <mu-appbar class="header-menu" z-depth="0">
      <mu-flex class="menu-list">
        <mu-flex justify-content="center" class="menu-item" fill>
          <mu-menu>
            Новини
          </mu-menu>
        </mu-flex>
        <mu-flex justify-content="center" class="menu-item" fill>
          <mu-menu>
            План роботи
          </mu-menu>
        </mu-flex>
        <mu-flex justify-content="center" class="menu-item" fill>
          <mu-menu>
            Додатково
          </mu-menu>
        </mu-flex>
      </mu-flex>
    </mu-appbar>
    <mu-flex class="content-container">
      <mu-flex class="theme-container test">
        <slot></slot>
      </mu-flex>
      <mu-flex justify-content="end" fill>
        <mu-flex class="sidebar test" justify-content="start">
          <mu-flex class="last-news"></mu-flex>
          <mu-flex class="helpful-links"></mu-flex>
        </mu-flex>
      </mu-flex>

    </mu-flex>
  </mu-container>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
  .test{
    min-height: 100px;
    background-color: cyan ;
  }

  .content-container{
    margin-top: 10px;

  }

  .theme-container{
    width: 75%;
  }

  .sidebar{
    justify-self: end;
    width: 95%;
  }

  .menu-item{
    line-height: 1.2;
  }
</style>
