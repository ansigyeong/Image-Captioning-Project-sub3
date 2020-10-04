<template>
  <div class="home">
    <Navbar></Navbar>

    <div class="bin"></div>
    <p class="first">Develop your English ability.</p>
    <p class="second">With Newlearn</p>
  </div>
</template>

<script>

import Navbar from "../components/common/Navigation"

export default {
  name: 'Home',
  components: {
    Navbar,
  }
}
</script>

<style socped>
  .bin{
    height: 70px;
  }
  .first{
    font-size: 50px;
    margin: 60px;
  }
  .second{
    align-content: right;
    font-size: 50px;
    margin: 60px;
  }
</style>