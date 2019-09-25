<template>
  <HomeSlot #main>
    <h1 class="info-topic">Новини центру</h1>
    <div class="news-container">
      <div v-for="one_new in news_list">
        <span>{{one_new}}</span>
      </div>
    </div>
  </HomeSlot>
</template>

<script>
import HomeSlot from '../components/Home';

export default {
  name: 'AllNews',

  components: {

    HomeSlot,

  },

  data() {
    return {
      news_list: '',
    };
  },

  created() {
    $.ajax({
      url: 'http://127.0.0.1:8000/public/news/',
      type: 'GET',
      success: (response) => {
        this.news_list = response.data.data;
      },
    });
  },
};
</script>

<style scoped>

</style>
