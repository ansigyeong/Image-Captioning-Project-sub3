<template>
<div data-app="true" class="vue-tempalte">
  <div class = "App">
    <!-- <div class="vertical-center"> -->
      <!-- <div class="inner-block"> -->
        <router-view :key="$route.fullPath" ></router-view>
      <!-- </div> -->
    <!-- </div> -->
  </div>
</div>
</template>

<script >

export default {
  name: 'App',
};
</script>



