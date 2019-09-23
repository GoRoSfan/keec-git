<template>
  <HomeSlot>
    <h1 class="info-topic">Новини центру</h1>
    <mu-flex class="news-container">
      <mu-flex>

      </mu-flex>
    </mu-flex>
  </HomeSlot>
</template>

<script>
  import HomeSlot from '@/components/Home'

  export default {
    name: "AllNews",

    comments:{

      HomeSlot,

    },


    data() {
      return {
        news_list: '',
      }
    },

    created() {

    },
  }
</script>

<style scoped>

</style>
