<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Правова база центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


  export default {
    name: 'Legals',

    components: {
      HomeSlot,
    },

    data: function () {
      return {}
    },
  };
</script>

<style scoped>

</style>
