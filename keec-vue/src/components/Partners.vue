<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Команда центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


  export default {
    name: 'Partners',

    components: {
      HomeSlot,
    },

    data: function () {
      return {
        partner_list: '',
      }
    },

    created() {
      $.ajax({
        url: "http://127.0.0.1:8000/public/partners/",
        type: 'GET',
        data: {},
        success: function(response){
          this.partner_list = response.data;
        },
      });
    },
  };
</script>

<style scoped>

</style>
