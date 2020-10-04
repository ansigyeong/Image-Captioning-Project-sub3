<template>
  <div class="bg">
    <Navbar/>
    <div class="bin"></div>
  </div>
</template>

<script>
import Navbar from "../components/common/Navigation"
import '@/assets/css/background1.css'

export default {
  components: {
        Navbar,
    },
  name: 'vocAnswerDetail',
}
</script>

<style scoped>
    .bin{
        height: 70px;
    }
    @media(max-width: 480px){
        h1{
            font-size: 30px;
        }
    }
</style>