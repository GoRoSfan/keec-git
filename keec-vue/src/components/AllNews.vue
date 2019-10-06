<template>
  <HomeSlot #main>
    <div class="info-topic"><h1>Новини центру</h1></div>
    <div class="all-news-container">
      <div v-for="one_new in news_list" class="news-container">
        <div class="news-header">
          <div class="news-title">{{one_new.title}}</div>
          <div class="news-date">{{one_new.post_date}}</div>
          <div class="boxing"></div>
        </div>
        <div class="news-context">
          <div class="news-image">
            <img :src="host + one_new.image" alt="Фотографія до новини" style="width: 100%">
          </div>
          <div class="news-description">{{one_new.description}} {{text}}</div>
        </div>
        <div class="news-footer">
          <div class="news-detail">
            <a :href="host + one_new.detail">detail</a>
          </div>
        </div>
      </div>
      <mu-flex justify-content="center" style="margin: 32px 0;">
        <mu-pagination :total="50" :current.sync="current_page" @change=""></mu-pagination>
      </mu-flex>
    </div>
  </HomeSlot>
</template>

<script>
import HomeSlot from './Home';

export default {
  name: 'AllNews',

  components: {

    HomeSlot,

  },

  data() {
    return {
      news_list: '',
      host: window.location.protocol.concat('//127.0.0.1:8000'),
      text: 'LA Bu dA'.repeat(30),
      current_page: 1,
    };
  },

  created() {
    $.ajax({
      url: 'http://127.0.0.1:8000/public/news/',
      type: 'GET',
      data: {
        'current_page': this.current_page,

      },
      success: (response) => {
        this.news_list = response.data.data;
      },
    });
  },

  methods:{

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
    border-radius: 10px;

    background-color: #133568;
  }

  .news-container{
    margin-top: 1em;

    color: #ffd792;

    border: #000 solid 0;
    border-radius: 13px;



    background-color: #133568;
  }

  .news-header{
    background-color: #ffc64e;

    color: #556688;

    border: #000 solid 0;
    border-radius: 10px 10px 0 0;
  }

  .news-title{
    float: left;

    margin: 0 2% 0 2%;
  }

  .news-date{
    float: right;

    margin: 0 2% 0 2%;
  }

  .boxing{
    clear: both;
  }

  .news-context{
    clear: both;
  }

  .news-image{
    width: 30%;
    float: right;
  }

  .news-footer{
    clear: right;
  }
</style>
