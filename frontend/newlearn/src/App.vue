<template>
  <v-app id="app">
      <router-view :key="$route.fullPath"></router-view>
  </v-app>
</template>

<script >
export default {
  name: 'App',
};
</script>



