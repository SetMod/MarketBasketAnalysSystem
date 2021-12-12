<template>
  <NavBar />
  <router-view class="container" />
</template>

<script>
import NavBar from "./components/NavBar/NavBar.vue";

export default {
  components: {
    NavBar,
  },
};
</script>


<style>
</style>
