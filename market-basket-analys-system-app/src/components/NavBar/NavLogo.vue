<template>
  <router-link class="nav-link navbar-brand" :to="path">{{
    title
  }}</router-link>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
    path: {
      type: String,
      required: true,
    },
  },
};
</script>

<style>
</style>