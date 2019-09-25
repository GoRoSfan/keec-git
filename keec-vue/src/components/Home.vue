<template>
  <mu-container class="main">
    <mu-appbar justify-content="center" z-depth="0">
      text text text text text text text text
    </mu-appbar>
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
    <div class="content-container">
      <div class="theme-container test">
        <slot name="main"></slot>
      </div>
      <div>
        <div class="sidebar test">
          <div class="last-news"></div>
          <div class="helpful-links"></div>
        </div>
      </div>

    </div>
  </mu-container>
</template>

<script>
export default {
  name: 'Home',
};
</script>

<style scoped>
  .test{
    /*min-height: 100px;*/
    background-color: #bbf5ff;
  }

  .header-menu{
    background-color: #ffc64e;
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
