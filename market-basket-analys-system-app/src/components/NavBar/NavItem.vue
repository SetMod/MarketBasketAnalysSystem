<template>
  <li class="nav-item">
    <router-link class="nav-link" :to="path">{{ name }}</router-link>
  </li>
</template>

<script>
export default {
  props: {
    name: {
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