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
      return {
        legal_list: '',
        legal_type_list: '',
      }
    },

    created() {
      $.ajax({
        url: "http://127.0.0.1:8000/public/legal/",
        type: 'GET',
        data: {},
        success: function(response){
          this.legal_list = response.legal_list;
          this.legal_type_list = response.legal_type_list;
        },
      });
    },
  };
</script>

<style scoped>

</style>
