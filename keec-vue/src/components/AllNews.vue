<template>
  <HomeSlot #main>
    <div class="context-header"><h2>Новини центру</h2></div>
    <div class="all-news-container">
      <article v-for="one_new in news_list" class="news-container">
        <div class="news-header">
          <cite>{{one_new.title}}</cite>
          <time>{{one_new.post_date}}</time>
        </div>
        <div class="news-main">
          <img :src="host + one_new.image" alt="Фотографія до новини" class="news-image">
          <div class="news-description">{{one_new.description}} {{text}}</div>
        </div>
        <div class="news-footer">
          <div></div>
          <mu-button id="news-detail" :href="host + one_new.detail">detail</mu-button>
        </div>
      </article>
    </div>
    <mu-flex justify-content="center" style="margin: 32px 0;">
      <mu-pagination :total="total_news" :current.sync="current_page" @change="page_change"></mu-pagination>
    </mu-flex>
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
      total_news: 40,
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
        this.news_list = response.data;
      },
    });
  },

  methods:{
    page_change: function (event) {
      $.ajax({
      url: 'http://127.0.0.1:8000/public/news/',
      type: 'GET',
      data: {
        'current_page': this.current_page,

      },
      success: (response) => {
        this.news_list = response.data;
      },
    });
    }
  },
};
</script>

<style scoped>
  h2{
    margin: 0;

    font-size: 1.4rem;
    font-weight: 400;
  }

  .all-news-container{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    flex-direction: column;
    flex-wrap: nowrap;
    -webkit-flex-flow: column nowrap;
  }

  .news-container{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    flex-direction: column;
    flex-wrap: nowrap;
    -webkit-flex-flow: column nowrap;

    margin-top: 2vmin;
  }

  article .news-header{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    justify-content: space-between;

    padding: 0.8vh 2vw;

    color: #556688;

    border-radius: 2vw 2vw 0 0;
    border-bottom: #ffc64e solid 1px;

    -webkit-box-shadow: inset 0 -1px #646464;
    -moz-box-shadow: inset 0 -1px #646464;
    box-shadow: inset 0 -1px #646464;

    background-color: #ffc64e;
  }

  article .news-header cite{
    align-self: center;

    font-style: normal;
    font-size: 1.5rem;
  }

  article .news-header time{
    align-self: start;

    font-size: 1rem;
  }

  article .news-main{
    padding: 1.5vh 1.5vw;

    color: #ffcc99;
    text-align: left;
    font-size: 1.2rem;
    
    background-color: #133568;
  }

  article .news-main .news-image{
    width: 30%;
    float: right;
  }

  article .news-footer{
    display: -webkit-box;
    display: -moz-box;
    display: -ms-flexbox;
    display: -webkit-flex;
    display: flex;

    -webkit-flex-flow: row wrap;
    flex-flow: row wrap;
    justify-content: space-around;

    padding: 1.5vh 0;

    border-radius: 0 0 2vw 2vw;

    background-color: #ffc64e;
  }
  
  article .news-footer #news-detail{
    background-color: #ffcc99;
  }

  article .news-footer #news-detail a{
    color: #556688;
    font-size: 1.2rem;
  }
</style>
