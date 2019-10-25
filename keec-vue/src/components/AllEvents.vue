<template>
  <HomeSlot #main>
    <div class="context-header"><h2>План роботи центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


export default {
  name: 'AllEvents',

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
