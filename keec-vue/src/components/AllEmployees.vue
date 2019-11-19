<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Команда центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


  export default {
    name: 'AllEmployees',

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
