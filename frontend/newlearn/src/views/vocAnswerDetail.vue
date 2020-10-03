<template>
  <div>
    <Navbar/>
    <div class="bin"></div>
  </div>
</template>

<script>
import Navbar from "../components/common/Navigation"

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