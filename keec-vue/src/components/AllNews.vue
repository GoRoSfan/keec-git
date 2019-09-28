<template>
  <HomeSlot #main>
    <div class="info-topic"><h1>Новини центру</h1></div>
    <div class="all-news-container">
      <div v-for="one_new in news_list" class="news-container">
        <div class="news-header">
          <div class="news-title">{{one_new.title}}</div>
          <div class="news-date">{{one_new.post_date}}</div>
        </div>
        <div class="news-context">
          <div class="news-description">{{one_new.description}}</div>
          <div class="news-image">
            <img :src="'http://127.0.0.1:8000' + one_new.image" alt="">
          </div>
        </div>
        <div class="news-footer">
          <div class="news-detail">
            <a :href="'http://127.0.0.1:8000' + one_new.detail">detail</a>
          </div>
        </div>
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
  h1{
    margin: 0;

    color: #ffd792;
    font-size: 1.25em;
  }

  .info-topic{
    padding-left: 15px;

    text-align: center;

    border: #fff solid 0;

    background-color: #133568;
  }

  .news-container{
    margin-top: 1em;

    color: #ffd792;

    border: #000 solid 1px;
    border-left-width: 0;
    border-right-width: 0;

    background-color: #133568;
  }

  .news-title{
    float: left;
  }

  .news-date{
    float: right;
  }

  .news-context{
    clear: both;
  }
</style>
