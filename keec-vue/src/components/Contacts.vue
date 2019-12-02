<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Контактна база центру</h2></div>

  </HomeSlot>
</template>

<script>
  import HomeSlot from './Home';


  export default {
    name: 'Contacts',

    components: {
      HomeSlot,
    },

    data: function () {
      return {
        contact_list: '',
      }
    },

    created() {
      $.ajax({
        url: "http://127.0.0.1:8000/public/contact/",
        type: 'GET',
        data: {},
        success: function(response){
          this.contact_list = response.data;
        },
      });
    },
  };
</script>

<style scoped>

</style>
