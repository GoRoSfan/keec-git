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
      return {
        events: '',
        count_pages: '',
      }
    },

    created: function () {
      $.ajax({
        url: 'http://127.0.0.1:8000/public/events/',
        type: 'GET',
        data: {
          connection: true,
        },
        success: (response) => {
          this.events = response.data;
        },
      })
    },
  };
</script>

<style scoped>

</style>
